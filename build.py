import re
import urllib.parse
from pathlib import Path


def build_link(path):
    with path.open("r") as f:
        quoted_code = urllib.parse.quote(f.read().replace("javascript:", ""))
        return f'<a href="javascript:{quoted_code}">{path.stem}</a>'


# Github markdown does not allow links with javascript, so hosting it as html on github pages
with open("index.html", "r") as f:
    template = f.read()

links = [build_link(path) for path in Path(".").glob("*.js")] * 3

with open("index.html", "w") as f:
    bookmarkles = "\n</br>\n".join(links)
    filled = re.sub(
        "(<!--- links start --->).*(<!--- links end --->)",
        f"\\1\n{bookmarkles}\n\\2",
        template,
        flags=re.DOTALL,
    )
    f.write(filled)
