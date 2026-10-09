
from html.parser import HTMLParser
from pathlib import Path

class HomepageValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = set()

    def handle_starttag(self, tag, attrs):
        self.tags.add(tag)

html = Path("index.html").read_text(encoding="utf-8")

validator = HomepageValidator()
validator.feed(html)
validator.close()

required_tags = {"html", "head", "title", "body", "h1", "p"}
missing_tags = required_tags - validator.tags

if missing_tags:
    raise SystemExit(
        f"Validation failed. Missing tags: {', '.join(sorted(missing_tags))}"
    )

print("HTML validation passed!")
