import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
SOURCES = {
    "da": WORKSPACE / "menu amigo" / "amigos_menu_template" / "index.html",
    "en": WORKSPACE / "menu amigo" / "engelsk version" / "index.html",
}
OUTPUT_DIR = ROOT / "data"


def clean_markup(value):
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(html.unescape(value).split())


def parse_menu(path):
    sections = []
    current = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if 'class="section-title' in line:
            spans = re.findall(r"<span>(.*?)</span>", line)
            if spans:
                category = clean_markup(spans[0])
                note = clean_markup(spans[1]) if len(spans) > 1 else ""
            else:
                match = re.search(r'class="section-title[^"]*">(.*?)</div>', line)
                if not match:
                    continue
                category = clean_markup(match.group(1))
                note = ""

            current = {"category": category, "note": note, "items": []}
            sections.append(current)
            continue

        if 'class="menu-item"' not in line or current is None:
            continue

        number_match = re.search(r'class="no">(.*?)</span>', line)
        name_match = re.search(r'class="name"><b>(.*?)</b>', line)
        desc_match = re.search(r'class="name"><b>.*?</b>\s*<span>(.*?)</span>', line)
        price_markup = line.rsplit('class="price">', 1)[-1].rsplit("</span></div>", 1)[0]

        current["items"].append(
            {
                "number": clean_markup(number_match.group(1)).rstrip(".") if number_match else "",
                "name": clean_markup(name_match.group(1)) if name_match else "",
                "description": clean_markup(desc_match.group(1)) if desc_match else "",
                "price": clean_markup(price_markup),
            }
        )

    return {"sections": [section for section in sections if section["items"]]}


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    for language, source in SOURCES.items():
        if not source.exists():
            raise FileNotFoundError(source)
        payload = parse_menu(source)
        output = OUTPUT_DIR / f"{language}.json"
        output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        item_count = sum(len(section["items"]) for section in payload["sections"])
        print(f"{language}: {len(payload['sections'])} sections, {item_count} items -> {output}")


if __name__ == "__main__":
    main()
