"""Retrofit all blog post Article schemas with canonical Person @id reference.

For each blog post in blog/*.html:
- Find the "author":{...} JSON-LD block (matched by balanced braces)
- Replace with new author block that:
  * References canonical @id at /author/amit-ratan#person
  * References Organization via @id /#organization
  * Includes personal sameAs: LinkedIn /in/allamitk + X @allamitk + Instagram @allamitk
  * Plus AllCoaching about/manifesto/author URLs

This unifies the Person entity graph across all 23 blog posts so AI agents
recognize Amit Ratan as a single canonical entity rather than 23 separate
inline definitions.
"""
import glob, os, sys

NEW_AUTHOR = '''"author":{
      "@id":"https://allcoaching.in/author/amit-ratan#person",
      "@type":"Person",
      "name":"Amit Ratan",
      "jobTitle":"Founder & CEO",
      "worksFor":{"@id":"https://allcoaching.in/#organization"},
      "url":"https://allcoaching.in/author/amit-ratan",
      "image":"https://allcoaching.in/assets/Amit-Ratan.webp",
      "sameAs":[
        "https://www.linkedin.com/in/allamitk/",
        "https://x.com/allamitk",
        "https://www.instagram.com/allamitk/",
        "https://allcoaching.in/about",
        "https://allcoaching.in/manifesto",
        "https://allcoaching.in/author/amit-ratan"
      ]
    }'''

def find_matching_brace(text, open_idx):
    """Given index of '{', find index of matching '}'."""
    depth = 0
    i = open_idx
    while i < len(text):
        c = text[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1

def retrofit_file(path):
    with open(path, 'r', encoding='utf-8') as fp:
        text = fp.read()

    # Find "author":{ — there should be exactly one in the Article schema
    marker = '"author":{'
    idx = text.find(marker)
    if idx < 0:
        return f"SKIP (no author block)"

    # Find the opening brace position
    open_brace = idx + len(marker) - 1
    close_brace = find_matching_brace(text, open_brace)
    if close_brace < 0:
        return f"FAIL (no matching brace)"

    # Replace from "author": to } inclusive
    full_old = text[idx:close_brace+1]
    text = text[:idx] + NEW_AUTHOR + text[close_brace+1:]

    with open(path, 'w', encoding='utf-8', newline='\n') as fp:
        fp.write(text)

    return f"OK (replaced {len(full_old)}B -> {len(NEW_AUTHOR)}B)"

if __name__ == '__main__':
    blog_dir = sys.argv[1] if len(sys.argv) > 1 else 'blog'
    files = sorted(glob.glob(os.path.join(blog_dir, '*.html')))
    files = [f for f in files if not f.endswith('index.html')]

    print(f"Found {len(files)} blog posts to retrofit\n")
    for f in files:
        result = retrofit_file(f)
        print(f"  {os.path.basename(f):60s} {result}")
    print(f"\nDone.")
