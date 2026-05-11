"""
Pass 3 — eliminate every blue, replace every blue-green gradient with ochre.

User directive: "jaha bhi blue color dikhe fix with brand guideline and also
remove green gradient"

Scope:
- All HTML files (root + blog/)
- styles.css and brand.css (already brand-aligned but double-check)

Preserves third-party brand colors:
- WhatsApp green (#25D366)
- Facebook blue (#1877F2), YouTube red (#FF0000), Telegram (#229ED9),
  X / Twitter (#000), Instagram gradient (#F58529..#515BD4)
- Tailwind class names like 'slate-*' (neutral grays — visually fine on cream)

Idempotent.
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TARGETS = list(REPO.glob("*.html")) + list((REPO / "blog").glob("*.html")) + [
    REPO / "styles.css", REPO / "brand.css",
]
TARGETS = [t for t in TARGETS if t.exists()]

# Ordered replacements — longer/more-specific patterns first so substring rules
# don't eat their longer cousins.
REPLACEMENTS = [
    # ---- Blue→ochre gradient combos (most specific first) ----
    ("linear-gradient(135deg,#1D4ED8,#2E9E4A)",
     "linear-gradient(135deg,#E0A95C 0%,#C58B43 55%,#8E5F22 100%)"),
    ("linear-gradient(135deg, #1D4ED8, #2E9E4A)",
     "linear-gradient(135deg,#E0A95C 0%,#C58B43 55%,#8E5F22 100%)"),
    ("linear-gradient(90deg, #2563EB, #2E9E4A)",
     "linear-gradient(90deg,#E0A95C 0%,#8E5F22 100%)"),
    ("linear-gradient(90deg,#2563EB,#2E9E4A)",
     "linear-gradient(90deg,#E0A95C 0%,#8E5F22 100%)"),
    ("linear-gradient(135deg,#2563EB,#2E9E4A)",
     "linear-gradient(135deg,#E0A95C 0%,#8E5F22 100%)"),
    ("linear-gradient(135deg, #2563EB, #2E9E4A)",
     "linear-gradient(135deg,#E0A95C 0%,#8E5F22 100%)"),
    ("linear-gradient(135deg, #2563EB 0%, #60A5FA 50%, #93C5FD 100%)",
     "linear-gradient(135deg,#E0A95C 0%,#C58B43 55%,#8E5F22 100%)"),
    ("linear-gradient(180deg, rgba(96,165,250,.75) 0%, rgba(37,99,235,.85) 100%)",
     "linear-gradient(180deg, rgba(58,39,16,.75) 0%, rgba(21,17,13,.85) 100%)"),

    # ---- Blue hex codes ----
    ("#2563EB", "#C58B43"),
    ("#1D4ED8", "#8E5F22"),
    ("#60A5FA", "#E0A95C"),
    ("#93C5FD", "#F5E8D2"),
    ("#BFDBFE", "#E8CFA3"),
    ("#DBEAFE", "#E8CFA3"),
    ("#EFF6FF", "#F5E8D2"),
    ("#0B1A3F", "#1A150F"),
    ("#0F172A", "#15110D"),
    ("#1E293B", "#3A2710"),
    ("#3A6FBF", "#8E5F22"),  # info blue → ochre deep (used decoratively here)
    ("#334155", "#4F4840"),
    ("#64748B", "#8C8378"),
    ("#475569", "#4F4840"),
    ("#94A3B8", "#B6AEA1"),
    ("#CBD5E1", "#B6AEA1"),
    ("#E2E8F0", "#E5DDD0"),  # slate-200 → warm line
    ("#F1F5F9", "#F6F2EA"),  # slate-100 → bg-tint
    ("#F8FAFC", "#F6F2EA"),  # slate-50 → bg-tint

    # ---- Standalone old greens (NOT semantic positive) ----
    ("#2E9E4A", "#2F8F4E"),
    ("#46A04A", "#2F8F4E"),
    ("#16A34A", "#2F8F4E"),
    ("#22C55E", "#2F8F4E"),
    ("#DCFCE7", "#DCF1DE"),
    ("#F0FDF4", "#EAF5EC"),

    # ---- Other legacy reds ----
    ("#E63935", "#C44232"),
    ("#DC2626", "#C44232"),
    ("#FEE2E2", "#F4DCD6"),
    ("#FEF9C3", "#F4EAD0"),
    ("#FDE68A", "#E8CFA3"),
    ("#F4B81A", "#B08518"),
    ("#FFF5F5", "#F9E8E2"),
    ("#FFFAFA", "#FCF1ED"),

    # ---- Purple residuals from .pull / .epi if any ----
    ("#8B5CF6", "#C58B43"),
    ("#EDE9FE", "#F5E8D2"),
    ("#F5F3FF", "#FBF4E6"),
    ("#2E1065", "#3A2710"),

    # ---- RGBA blue ----
    ("rgba(37,99,235,", "rgba(197,139,67,"),
    ("rgba(37, 99, 235,", "rgba(197, 139, 67,"),
    ("rgba(29,78,216,", "rgba(142,95,34,"),
    ("rgba(96,165,250,", "rgba(224,169,92,"),
    ("rgba(191,219,254,", "rgba(232,207,163,"),
    ("rgba(58,111,191,", "rgba(197,139,67,"),

    # ---- RGBA old greens ----
    ("rgba(46,158,74,", "rgba(47,143,78,"),
    ("rgba(34,197,94,", "rgba(47,143,78,"),

    # ---- RGBA old slate ink ----
    ("rgba(15,23,42,", "rgba(38,28,14,"),
    ("rgba(2,6,23,", "rgba(20,17,13,"),
    ("rgba(51,65,85,", "rgba(79,72,64,"),

    # ---- Tailwind utility classes ----
    ("text-blue-700", "text-[#8E5F22]"),
    ("text-blue-600", "text-[#8E5F22]"),
    ("text-blue-500", "text-[#C58B43]"),
    ("text-blue-400", "text-[#E0A95C]"),
    ("text-blue-300", "text-[#E0A95C]"),
    ("text-blue-200", "text-[#E8CFA3]"),
    ("text-blue-100", "text-[#F5E8D2]"),
    ("bg-blue-700", "bg-[#8E5F22]"),
    ("bg-blue-600", "bg-[#8E5F22]"),
    ("bg-blue-500", "bg-[#C58B43]"),
    ("bg-blue-100", "bg-[#F5E8D2]"),
    ("bg-blue-50", "bg-[#F5E8D2]"),
    ("hover:bg-blue-50", "hover:bg-[#F5E8D2]"),
    ("hover:bg-blue-100", "hover:bg-[#E8CFA3]"),
    ("hover:text-blue-700", "hover:text-[#8E5F22]"),
    ("hover:text-blue-600", "hover:text-[#8E5F22]"),
    ("hover:text-blue-500", "hover:text-[#C58B43]"),
    ("border-blue-700", "border-[#8E5F22]"),
    ("border-blue-500", "border-[#C58B43]"),
    ("border-blue-200", "border-[#E8CFA3]"),
    ("border-blue-100", "border-[#F5E8D2]"),
    ("ring-blue-500", "ring-[#C58B43]"),
    ("from-blue-500", "from-[#C58B43]"),
    ("via-blue-500", "via-[#C58B43]"),
    ("to-blue-500", "to-[#C58B43]"),
    ("from-blue-600", "from-[#8E5F22]"),
    ("to-blue-600", "to-[#8E5F22]"),
    ("decoration-blue-500", "decoration-[#C58B43]"),

    # ---- Tailwind green utility classes (only purely-decorative greens) ----
    ("from-green-500", "from-[#C58B43]"),
    ("to-green-500", "to-[#8E5F22]"),
    ("via-green-500", "via-[#C58B43]"),
    ("text-green-500", "text-[#C58B43]"),
    ("bg-green-500", "bg-[#C58B43]"),

    # ---- slate-900 (very common in legacy code) ----
    ("text-slate-900", "text-[#15110D]"),
    ("bg-slate-900", "bg-[#15110D]"),
    ("border-slate-900", "border-[#15110D]"),
]


def migrate(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []
    for old, new in REPLACEMENTS:
        if old in text:
            n = text.count(old)
            text = text.replace(old, new)
            changes.append(f"{n}x {old[:46]}")
    if text != original:
        path.write_text(text, encoding="utf-8")
        return {"file": path.relative_to(REPO), "changed": True, "actions": changes}
    return {"file": path.relative_to(REPO), "changed": False, "actions": []}


def main():
    print(f"Pass 3 - blue elimination + green-gradient removal across {len(TARGETS)} files\n")
    total_changed = 0
    for p in sorted(TARGETS, key=lambda x: str(x)):
        r = migrate(p)
        status = "[OK]" if r["changed"] else "[--]"
        print(f"  {status} {r['file']}")
        if r["changed"]:
            total_changed += 1
        for a in r["actions"][:8]:  # cap per-file output
            print(f"      - {a}")
        if len(r["actions"]) > 8:
            print(f"      - ... +{len(r['actions']) - 8} more swaps")
    print(f"\n{total_changed} files modified")


if __name__ == "__main__":
    main()
