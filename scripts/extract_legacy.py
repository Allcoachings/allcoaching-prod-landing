"""
Extract metadata from legacy HTML blog posts into data/legacy-manifest.yaml.

The 28 existing posts in /blog/*.html are not modified. This script reads
them (read-only), pulls title/description/keywords/dates/cover-image/JSON-LD,
combines with a hand-curated category/subcategory mapping, and writes the
result to data/legacy-manifest.yaml.

Run after any new legacy post is added (rare — usually new posts go via
markdown pipeline). Idempotent — preserves human edits in the YAML where
the script can't override (the script REPLACES the manifest on each run,
so any human edits to category/subcategory should go via the mapping below).
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from datetime import datetime
import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "blog"
MANIFEST_OUT = ROOT / "data" / "legacy-manifest.yaml"

# ---------------------------------------------------------------------
# Editorial mapping — hand-curated category/subcategory/tags for each
# legacy slug. Single source for "where does this post belong".
# ---------------------------------------------------------------------

LEGACY_MAPPING: dict[str, dict] = {
    "affordable-lms-for-independent-educators": {
        "category": "platforms-tools",
        "subcategory": "lms-platforms",
        "tags": ["aud-individual-tutor", "format-analysis"],
        "translation_group": "tg-affordable-lms",
    },
    "automate-student-onboarding-for-coaching-app": {
        "category": "operations",
        "subcategory": "onboarding",
        "tags": ["aud-institute-owner", "format-howto"],
        "translation_group": "tg-automate-onboarding",
    },
    "automated-fee-management-software-for-teachers": {
        "category": "operations",
        "subcategory": "fee-management",
        "tags": ["reg-gst", "tech-upi", "aud-institute-owner", "format-analysis"],
        "translation_group": "tg-fee-management",
    },
    "best-free-tools-for-teachers-to-record-lectures": {
        "category": "teaching-content",
        "subcategory": "video-creation",
        "tags": ["aud-individual-tutor", "format-howto"],
        "translation_group": "tg-record-lectures-tools",
    },
    "best-platform-for-selling-pdf-notes-and-test-series": {
        "category": "business-monetization",
        "subcategory": "revenue-streams",
        "tags": ["aud-individual-tutor", "format-comparison"],
        "translation_group": "tg-pdf-notes-test-series",
    },
    "best-upi-payment-gateway-for-online-courses": {
        "category": "operations",
        "subcategory": "payments",
        "tags": ["tech-upi", "reg-gst", "format-comparison"],
        "translation_group": "tg-upi-gateway",
    },
    "best-zero-commission-teaching-platform-india": {
        "category": "platforms-tools",
        "subcategory": "lms-platforms",
        "tags": ["aud-individual-tutor", "format-comparison"],
        "translation_group": "tg-zero-commission",
    },
    "budget-home-studio-setup-for-online-teaching": {
        "category": "teaching-content",
        "subcategory": "studio-setup",
        "tags": ["aud-individual-tutor", "format-howto"],
        "translation_group": "tg-home-studio",
    },
    "classplus-vs-graphy-vs-allcoaching": {
        "category": "platforms-tools",
        "subcategory": "lms-platforms",
        "tags": ["format-comparison", "aud-institute-owner"],
        "translation_group": "tg-classplus-graphy",
    },
    "edtech-marketplace-india-app-fatigue": {
        "category": "business-monetization",
        "subcategory": "industry-trends",
        "tags": ["format-analysis", "aud-institute-owner"],
        "translation_group": "tg-app-fatigue",
    },
    "how-to-conduct-live-classes-on-mobile-apps": {
        "category": "teaching-content",
        "subcategory": "live-classes",
        "tags": ["tech-webrtc", "format-howto"],
        "translation_group": "tg-live-classes-mobile",
    },
    "how-to-create-interactive-mock-tests-online": {
        "category": "teaching-content",
        "subcategory": "mock-tests",
        "tags": ["exam-neet", "exam-jee", "format-howto"],
        "translation_group": "tg-mock-tests",
    },
    "how-to-create-landing-page-for-online-course": {
        "category": "growth-marketing",
        "subcategory": "conversion",
        "tags": ["format-howto"],
        "translation_group": "tg-landing-page",
    },
    "how-to-get-first-500-students-for-coaching-app": {
        "category": "growth-marketing",
        "subcategory": "student-acquisition",
        "tags": ["aud-institute-owner", "format-howto"],
        "translation_group": "tg-first-500-students",
    },
    "how-to-start-online-academy-in-5-steps": {
        "category": "getting-started",
        "subcategory": "first-setup",
        "tags": ["aud-individual-tutor", "format-howto"],
        "translation_group": "tg-start-academy",
    },
    "indian-edtech-laws-and-regulations-for-teachers": {
        "category": "business-monetization",
        "subcategory": "legal-finance",
        "tags": ["reg-gst", "reg-dpdp", "reg-it-act", "format-analysis"],
        "translation_group": "tg-edtech-laws",
    },
    "migrate-offline-coaching-to-online-zero-cost": {
        "category": "getting-started",
        "subcategory": "migration",
        "tags": ["aud-institute-owner", "format-howto"],
        "translation_group": "tg-migrate-offline",
    },
    "monetize-youtube-teaching-channel-via-personal-app": {
        "category": "business-monetization",
        "subcategory": "revenue-streams",
        "tags": ["aud-individual-tutor", "format-howto"],
        "translation_group": "tg-monetize-youtube",
    },
    "multi-language-lms-for-regional-indian-languages": {
        "category": "platforms-tools",
        "subcategory": "multilingual",
        "tags": ["format-analysis"],
        "translation_group": "tg-multi-language-lms",
    },
    "online-coaching-academy-without-coding": {
        "category": "getting-started",
        "subcategory": "no-code",
        "tags": ["aud-individual-tutor", "format-howto"],
        "translation_group": "tg-no-code-academy",
    },
    "online-coaching-business-plan-2026": {
        "category": "business-monetization",
        "subcategory": "business-plans",
        "tags": ["aud-institute-owner", "format-analysis"],
        "translation_group": "tg-business-plan-2026",
    },
    "protect-course-content-from-piracy-for-free": {
        "category": "operations",
        "subcategory": "security",
        "tags": ["tech-drm", "format-howto"],
        "translation_group": "tg-piracy-protection",
    },
    "secure-video-hosting-for-educational-content": {
        "category": "operations",
        "subcategory": "security",
        "tags": ["tech-drm", "format-analysis"],
        "translation_group": "tg-secure-video",
    },
    "sell-online-courses-without-monthly-subscription": {
        "category": "business-monetization",
        "subcategory": "pricing-models",
        "tags": ["aud-individual-tutor", "format-analysis"],
        "translation_group": "tg-no-subscription",
    },
    "seo-strategies-for-online-course-creators": {
        "category": "growth-marketing",
        "subcategory": "seo",
        "tags": ["format-howto"],
        "translation_group": "tg-seo-strategies",
    },
    "student-progress-tracking-analytics-tools-coaching-india": {
        "category": "operations",
        "subcategory": "analytics",
        "tags": ["aud-institute-owner", "format-analysis"],
        "translation_group": "tg-progress-tracking",
    },
    "using-chatgpt-for-course-curriculum-design": {
        "category": "teaching-content",
        "subcategory": "ai-tools",
        "tags": ["tech-ai", "format-howto"],
        "translation_group": "tg-chatgpt-curriculum",
    },
    "white-label-coaching-app-development-cost-india": {
        "category": "platforms-tools",
        "subcategory": "white-label",
        "tags": ["aud-institute-owner", "format-analysis"],
        "translation_group": "tg-white-label-cost",
    },
}

# Existing Hinglish posts (separately tracked)
HINGLISH_MAPPING: dict[str, dict] = {
    "apna-coaching-app-kaise-banaye-free": {
        "category": "getting-started",
        "subcategory": "no-code",
        "tags": ["aud-individual-tutor", "format-howto"],
        "translation_group": "tg-no-code-academy",
    },
    "teachers-ke-liye-best-coaching-app-2026": {
        "category": "platforms-tools",
        "subcategory": "lms-platforms",
        "tags": ["aud-individual-tutor", "format-comparison"],
        "translation_group": "tg-best-coaching-app",
    },
}


# ---------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------

def _text(node) -> str:
    return node.get_text(strip=True) if node else ""


def _attr(node, name, default="") -> str:
    if node is None:
        return default
    return (node.get(name) or default).strip()


def extract_meta(html: str) -> dict:
    """Pull title/description/keywords/dates/cover/wordCount from a legacy post."""
    soup = BeautifulSoup(html, "html.parser")
    head = soup.find("head")

    out: dict = {}

    title = soup.find("title")
    out["title"] = _text(title)

    desc = soup.find("meta", attrs={"name": "description"})
    out["description"] = _attr(desc, "content")

    keywords = soup.find("meta", attrs={"name": "keywords"})
    if keywords:
        kw_raw = _attr(keywords, "content")
        out["keywords"] = [k.strip() for k in kw_raw.split(",") if k.strip()]

    canonical = soup.find("link", attrs={"rel": "canonical"})
    out["canonical"] = _attr(canonical, "href")

    og_image = soup.find("meta", attrs={"property": "og:image"})
    out["cover_image_url"] = _attr(og_image, "content")

    pub = soup.find("meta", attrs={"property": "article:published_time"})
    mod = soup.find("meta", attrs={"property": "article:modified_time"})
    out["published"] = _attr(pub, "content")
    out["modified"] = _attr(mod, "content")

    section = soup.find("meta", attrs={"property": "article:section"})
    out["legacy_article_section"] = _attr(section, "content")

    # Extract first JSON-LD Article schema's wordCount + headline if available
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
        except (json.JSONDecodeError, TypeError):
            continue
        # data can be a single dict or a list
        candidates = data if isinstance(data, list) else [data]
        for c in candidates:
            if not isinstance(c, dict):
                continue
            t = c.get("@type")
            types = t if isinstance(t, list) else [t]
            if any("Article" in (typ or "") for typ in types):
                if "wordCount" in c:
                    out["word_count"] = c["wordCount"]
                if "headline" in c and "headline" not in out:
                    out["headline"] = c["headline"]
                if "datePublished" in c:
                    out["published_from_schema"] = c["datePublished"]
                if "dateModified" in c:
                    out["modified_from_schema"] = c["dateModified"]
                break

    return out


def slug_from_path(path: Path) -> str:
    return path.stem


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def build_manifest() -> dict:
    posts: list[dict] = []

    # English blog posts in /blog/
    for f in sorted(BLOG_DIR.glob("*.html")):
        slug = slug_from_path(f)
        if slug == "index":
            continue  # blog/index.html is the hub, not a post

        mapping = LEGACY_MAPPING.get(slug)
        if not mapping:
            print(f"WARN: no mapping for legacy slug '{slug}' — skipped.", file=sys.stderr)
            continue

        meta = extract_meta(f.read_text(encoding="utf-8"))
        entry = {
            "slug": slug,
            "file": f"blog/{f.name}",
            "type": "blog",
            "language": "en",
            "status": "published",
            "author": "amit-ratan",
            "category": mapping["category"],
            "subcategory": mapping["subcategory"],
            "tags": mapping.get("tags", []),
            "translation_group": mapping["translation_group"],
            "title": meta.get("title", ""),
            "description": meta.get("description", ""),
            "keywords": meta.get("keywords", []),
            "canonical": meta.get("canonical", ""),
            "cover_image_url": meta.get("cover_image_url", ""),
            "published": meta.get("published") or meta.get("published_from_schema", ""),
            "modified": meta.get("modified") or meta.get("modified_from_schema", ""),
            "word_count": meta.get("word_count"),
        }
        # Strip empty optional fields
        entry = {k: v for k, v in entry.items() if v not in (None, "", [])}
        posts.append(entry)

    # Hinglish posts in /hinglish/blog/
    hinglish_dir = ROOT / "hinglish" / "blog"
    if hinglish_dir.is_dir():
        for f in sorted(hinglish_dir.glob("*.html")):
            slug = slug_from_path(f)
            if slug == "index":
                continue
            mapping = HINGLISH_MAPPING.get(slug)
            if not mapping:
                print(f"WARN: no mapping for hinglish slug '{slug}' — skipped.", file=sys.stderr)
                continue
            meta = extract_meta(f.read_text(encoding="utf-8"))
            entry = {
                "slug": slug,
                "file": f"hinglish/blog/{f.name}",
                "type": "blog",
                "language": "hinglish",
                "status": "published",
                "author": "amit-ratan",
                "category": mapping["category"],
                "subcategory": mapping["subcategory"],
                "tags": mapping.get("tags", []),
                "translation_group": mapping["translation_group"],
                "title": meta.get("title", ""),
                "description": meta.get("description", ""),
                "keywords": meta.get("keywords", []),
                "canonical": meta.get("canonical", ""),
                "cover_image_url": meta.get("cover_image_url", ""),
                "published": meta.get("published") or meta.get("published_from_schema", ""),
                "modified": meta.get("modified") or meta.get("modified_from_schema", ""),
                "word_count": meta.get("word_count"),
            }
            entry = {k: v for k, v in entry.items() if v not in (None, "", [])}
            posts.append(entry)

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "generator": "scripts/extract_legacy.py",
        "note": (
            "Auto-generated metadata for legacy HTML posts. The HTML files "
            "themselves are NOT modified — they remain canonical. Edit the "
            "LEGACY_MAPPING dict in extract_legacy.py to change category/tags "
            "for a legacy post, then re-run the script."
        ),
        "total_posts": len(posts),
        "posts": posts,
    }


def main():
    manifest = build_manifest()
    MANIFEST_OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_OUT, "w", encoding="utf-8") as fp:
        yaml.dump(
            manifest,
            fp,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=120,
        )
    print(f"Wrote {MANIFEST_OUT.relative_to(ROOT)} ({manifest['total_posts']} posts).")

    # Print summary by category
    from collections import Counter
    counts = Counter((p["language"], p["category"]) for p in manifest["posts"])
    print("\nBy language × category:")
    for (lang, cat), n in sorted(counts.items()):
        print(f"  {lang:8s} {cat:25s} {n}")


if __name__ == "__main__":
    main()
