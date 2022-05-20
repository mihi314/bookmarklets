import re
import urllib.parse
from pathlib import Path


def build_link(path):
    with path.open("r") as f:
        quoted_code = urllib.parse.quote(f.read().replace("javascript:", ""))
        return f'<a href="javascript:{quoted_code}">{path.stem}</a>'


with open("README.md", "r") as f:
    readme = f.read()

links = [build_link(path) for path in Path(".").glob("*.js")]

with open("README.md", "w") as f:
    bookmarkles = "\n\n".join(links)
    new_readme = re.sub(
        "(<!--- links start --->).*(<!--- links end --->)",
        f"\\1\n{bookmarkles}\n\\2",
        readme,
        flags=re.DOTALL,
    )
    f.write(new_readme)
