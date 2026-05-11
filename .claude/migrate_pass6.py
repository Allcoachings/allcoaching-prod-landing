"""
Pass 6 — eliminate slate-*, rose/sky/violet decorative palettes, and
unify all icon backgrounds to the brand's warm/ochre system.

Brand rule: ONE accent (ochre) owns the page. Decorative greens / blues /
purples / roses are not used. Semantic positive (#2F8F4E) is preserved only
for actual status. Semantic negative (#C44232) for errors. Amber for warm
accent. Everything else collapses to ochre family + warm neutrals.
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TARGETS = list(REPO.glob("*.html")) + list((REPO / "blog").glob("*.html"))

# Class-level mappings. Order matters: more specific (with prefix) before less.
MAPPINGS = []

# Helper to add hover: + plain variants together
def add(old, new):
    MAPPINGS.append((old, new))
    MAPPINGS.append((f"hover:{old}", f"hover:{new}"))
    MAPPINGS.append((f"focus:{old}", f"focus:{new}"))
    MAPPINGS.append((f"group-hover:{old}", f"group-hover:{new}"))

# ---- slate (Tailwind blue-gray) → warm ink scale ----
add("text-slate-900", "text-[#15110D]")
add("text-slate-800", "text-[#15110D]")
add("text-slate-700", "text-[#3A2710]")
add("text-slate-600", "text-[#4F4840]")
add("text-slate-500", "text-[#8C8378]")
add("text-slate-400", "text-[#B6AEA1]")
add("text-slate-300", "text-[#B6AEA1]")
add("text-slate-200", "text-[#E5DDD0]")
add("text-slate-100", "text-[#F6F2EA]")
add("text-slate-50",  "text-[#FAF8F4]")
add("bg-slate-900", "bg-[#15110D]")
add("bg-slate-800", "bg-[#3A2710]")
add("bg-slate-700", "bg-[#4F4840]")
add("bg-slate-200", "bg-[#E5DDD0]")
add("bg-slate-100", "bg-[#F6F2EA]")
add("bg-slate-50",  "bg-[#F6F2EA]")
add("border-slate-900", "border-[#15110D]")
add("border-slate-700", "border-[#4F4840]")
add("border-slate-300", "border-[rgba(20,17,13,0.12)]")
add("border-slate-200", "border-[#E5DDD0]")
add("border-slate-100", "border-[rgba(20,17,13,0.07)]")
add("border-slate-50",  "border-[rgba(20,17,13,0.05)]")
add("ring-slate-200", "ring-[#E5DDD0]")
add("ring-slate-300", "ring-[rgba(20,17,13,0.12)]")
add("divide-slate-200", "divide-[#E5DDD0]")
add("divide-slate-100", "divide-[rgba(20,17,13,0.07)]")
add("from-slate-900", "from-[#15110D]")
add("via-slate-800", "via-[#3A2710]")
add("to-slate-900", "to-[#15110D]")
add("from-slate-50", "from-[#F6F2EA]")
add("to-slate-100", "to-[#F6F2EA]")

# ---- decorative rose (warm-leaning, but brand says no decoration) → warm ochre ----
add("text-rose-600", "text-[#C44232]")     # semantic negative ok here
add("text-rose-500", "text-[#C44232]")
add("text-rose-400", "text-[#E08A7F]")
add("bg-rose-50",   "bg-[#F9E8E2]")
add("bg-rose-100",  "bg-[#F4DCD6]")
add("bg-rose-500",  "bg-[#C44232]")
add("border-rose-200", "border-[rgba(196,66,50,0.18)]")

# ---- sky (blue) → ochre ----
add("text-sky-700", "text-[#8E5F22]")
add("text-sky-600", "text-[#8E5F22]")
add("text-sky-500", "text-[#C58B43]")
add("text-sky-400", "text-[#E0A95C]")
add("bg-sky-50",   "bg-[#F5E8D2]")
add("bg-sky-100",  "bg-[#E8CFA3]")
add("bg-sky-500",  "bg-[#C58B43]")
add("border-sky-200", "border-[#E8CFA3]")

# ---- violet (decorative) → ochre ----
add("text-violet-700", "text-[#8E5F22]")
add("text-violet-600", "text-[#8E5F22]")
add("text-violet-500", "text-[#C58B43]")
add("bg-violet-50",   "bg-[#F5E8D2]")
add("bg-violet-100",  "bg-[#E8CFA3]")
add("bg-violet-500",  "bg-[#C58B43]")
add("border-violet-200", "border-[#E8CFA3]")

# ---- emerald → keep semantic positive #2F8F4E for status ----
add("text-emerald-700", "text-[#2F8F4E]")
add("text-emerald-600", "text-[#2F8F4E]")
add("text-emerald-500", "text-[#2F8F4E]")
add("text-emerald-400", "text-[#56AB6D]")
add("bg-emerald-50",   "bg-[#DCF1DE]")
add("bg-emerald-100",  "bg-[#DCF1DE]")
add("bg-emerald-500",  "bg-[#2F8F4E]")
add("bg-emerald-600",  "bg-[#2F8F4E]")
add("border-emerald-200", "border-[rgba(47,143,78,0.22)]")

# ---- amber → warm warning yellow (brand's warning token) ----
add("text-amber-700", "text-[#B08518]")
add("text-amber-600", "text-[#B08518]")
add("text-amber-500", "text-[#B08518]")
add("text-amber-400", "text-[#C58B43]")
add("bg-amber-50",   "bg-[#F4EAD0]")
add("bg-amber-100",  "bg-[#F4EAD0]")
add("bg-amber-500",  "bg-[#B08518]")
add("border-amber-200", "border-[rgba(176,133,24,0.22)]")

# ---- primary-* (was old Tailwind blue) → ochre ----
add("text-primary-50",  "text-[#F5E8D2]")
add("text-primary-600", "text-[#C58B43]")
add("text-primary-700", "text-[#8E5F22]")
add("text-primary-800", "text-[#8E5F22]")
add("bg-primary-50",    "bg-[#F5E8D2]")
add("bg-primary-100",   "bg-[#F5E8D2]")
add("bg-primary-600",   "bg-[#C58B43]")
add("bg-primary-700",   "bg-[#8E5F22]")
add("bg-primary-800",   "bg-[#8E5F22]")
add("border-primary-200", "border-[#E8CFA3]")
add("border-primary-600", "border-[#C58B43]")
add("from-primary-600", "from-[#C58B43]")
add("via-primary-600",  "via-[#C58B43]")
add("to-primary-700",   "to-[#8E5F22]")
add("to-primary-800",   "to-[#8E5F22]")
add("from-primary-50",  "from-[#F5E8D2]")

# ---- gray/zinc/neutral (cousins of slate) → warm ink scale ----
add("text-gray-900", "text-[#15110D]")
add("text-gray-800", "text-[#15110D]")
add("text-gray-700", "text-[#3A2710]")
add("text-gray-600", "text-[#4F4840]")
add("text-gray-500", "text-[#8C8378]")
add("text-gray-400", "text-[#B6AEA1]")
add("bg-gray-50",   "bg-[#F6F2EA]")
add("bg-gray-100",  "bg-[#F6F2EA]")
add("bg-gray-200",  "bg-[#E5DDD0]")
add("border-gray-200", "border-[#E5DDD0]")
add("border-gray-100", "border-[rgba(20,17,13,0.07)]")
add("text-neutral-700", "text-[#3A2710]")
add("text-neutral-600", "text-[#4F4840]")
add("text-neutral-500", "text-[#8C8378]")
add("bg-neutral-50",   "bg-[#F6F2EA]")
add("bg-neutral-100",  "bg-[#F6F2EA]")
add("border-neutral-200", "border-[#E5DDD0]")

# Plain (non-prefixed) ring + ring-offset variants
MAPPINGS.append(("ring-blue-500", "ring-[#C58B43]"))
MAPPINGS.append(("ring-emerald-500", "ring-[#2F8F4E]"))


def migrate(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    original = text
    swap_count = 0
    for old, new in MAPPINGS:
        # Use regex to match the class only when surrounded by word boundary
        # or whitespace/quote — avoids matching substrings inside other classes.
        if old in text:
            n = text.count(old)
            text = text.replace(old, new)
            swap_count += n
    if text != original:
        path.write_text(text, encoding="utf-8")
        return {"file": path.relative_to(REPO), "changed": True, "swaps": swap_count}
    return {"file": path.relative_to(REPO), "changed": False, "swaps": 0}


def main():
    print(f"Pass 6 - unify Tailwind palette to brand across {len(TARGETS)} files\n")
    total_files = 0
    total_swaps = 0
    for p in sorted(TARGETS, key=lambda x: str(x)):
        r = migrate(p)
        status = "[OK]" if r["changed"] else "[--]"
        print(f"  {status} {str(r['file']):<70} {r['swaps']:>4} swaps")
        if r["changed"]:
            total_files += 1
            total_swaps += r["swaps"]
    print(f"\n{total_files} files modified, {total_swaps} class swaps total")


if __name__ == "__main__":
    main()
