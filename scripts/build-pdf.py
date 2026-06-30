import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
HERO_IMAGE = ROOT / "assets" / "hero-pizza.png"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 30
GUTTER = 20
COLUMN_WIDTH = (PAGE_WIDTH - MARGIN * 2 - GUTTER) / 2
TOP_Y = PAGE_HEIGHT - 100
BOTTOM_Y = 42

RED = colors.HexColor("#c73725")
ORANGE = colors.HexColor("#f15b32")
CREAM = colors.HexColor("#fff7ed")
INK = colors.HexColor("#221a17")
MUTED = colors.HexColor("#6f625d")
LIGHT_LINE = colors.HexColor("#eee2da")

LOCALES = {
    "da": {
        "output": ROOT / "menu-da.pdf",
        "title": "Amigo's Pizza & Grill - Dansk menu",
        "cover_lines": ["PIZZA & DURUM", "SANDWICH & PASTA", "SPECIALITETER"],
        "takeaway": "Alle retter kan tages med ud af huset",
        "phone_label": "Tlf.",
        "opening": "ÅBNINGSTIDER",
        "weekdays": "MAN - FRE  KL. 16 - 21",
        "weekend": "LØR - SØN  KL. 12 - 21",
        "notice": ["Bemærk", "Åbent hele", "året"],
        "sms": ["SMS", "din bestilling", "42 34 09 15"],
        "header_info": "Man-fre 16-21 | Lør-søn 12-21 | Tannisbugtvej 68",
        "header_note": "Deep-pan pizza +25,- | Ekstra tilbehør alm. 20,- / fam. 35,-",
        "page": "Side",
    },
    "en": {
        "output": ROOT / "menu-en.pdf",
        "title": "Amigo's Pizza & Grill - English menu",
        "cover_lines": ["PIZZA & DURUM WRAPS", "SANDWICHES & PASTA", "SPECIALTIES"],
        "takeaway": "All dishes are available for takeaway",
        "phone_label": "Tel.",
        "opening": "OPENING HOURS",
        "weekdays": "MON - FRI  4 PM - 9 PM",
        "weekend": "SAT - SUN  12 PM - 9 PM",
        "notice": ["Please note", "Open all", "year"],
        "sms": ["TEXT", "your order", "42 34 09 15"],
        "header_info": "Mon-Fri 4-9 PM | Sat-Sun 12-9 PM | Tannisbugtvej 68",
        "header_note": "Deep-pan pizza +25,- | Extra topping reg. 20,- / fam. 35,-",
        "page": "Page",
    },
}


def load_menu(language):
    path = ROOT / "data" / f"{language}.json"
    return json.loads(path.read_text(encoding="utf-8"))["sections"]


def draw_background(pdf):
    pdf.setFillColor(CREAM)
    pdf.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.roundRect(
        MARGIN - 8,
        MARGIN - 8,
        PAGE_WIDTH - (MARGIN - 8) * 2,
        PAGE_HEIGHT - (MARGIN - 8) * 2,
        8,
        fill=1,
        stroke=0,
    )


def fit_image(pdf, path, x, y, width, height):
    if not path.exists():
        return
    image = ImageReader(str(path))
    iw, ih = image.getSize()
    scale = max(width / iw, height / ih)
    draw_w, draw_h = iw * scale, ih * scale
    pdf.saveState()
    clip = pdf.beginPath()
    clip.rect(x, y, width, height)
    pdf.clipPath(clip, stroke=0, fill=0)
    pdf.drawImage(
        image,
        x + (width - draw_w) / 2,
        y + (height - draw_h) / 2,
        draw_w,
        draw_h,
        mask="auto",
    )
    pdf.restoreState()


def draw_title(pdf, x, y, scale=1.0):
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 34 * scale)
    pdf.drawString(x + 1.2, y - 1.2, "AMIGO'S")
    pdf.setFillColor(ORANGE)
    pdf.drawString(x, y, "AMIGO'S")
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 23 * scale)
    pdf.drawString(x + 1, y - 28 * scale - 1, "PIZZA & GRILL")
    pdf.setFillColor(ORANGE)
    pdf.drawString(x, y - 28 * scale, "PIZZA & GRILL")


def draw_cover(pdf, locale):
    draw_background(pdf)
    draw_title(pdf, 72, PAGE_HEIGHT - 112, 1.35)

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 16)
    for index, line in enumerate(locale["cover_lines"]):
        pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 206 - index * 28, line)

    fit_image(pdf, HERO_IMAGE, 72, 344, PAGE_WIDTH - 144, 196)

    pdf.setFillColor(ORANGE)
    pdf.rect(76, PAGE_HEIGHT - 322, PAGE_WIDTH - 152, 28, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-BoldOblique", 13)
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 313, locale["takeaway"])

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(PAGE_WIDTH / 2, 318, locale["phone_label"])
    pdf.setFont("Helvetica-Bold", 38)
    pdf.drawCentredString(PAGE_WIDTH / 2, 282, "98 94 11 10")

    for x, lines in ((150, locale["notice"]), (PAGE_WIDTH - 150, locale["sms"])):
        pdf.setFillColor(RED)
        pdf.circle(x, 188, 48, fill=1, stroke=0)
        pdf.setFillColor(colors.white)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawCentredString(x, 205, lines[0])
        pdf.drawCentredString(x, 188, lines[1])
        pdf.drawCentredString(x, 171, lines[2])

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 17)
    pdf.drawCentredString(PAGE_WIDTH / 2, 225, locale["opening"])
    pdf.setFont("Helvetica-Bold", 17)
    pdf.drawCentredString(PAGE_WIDTH / 2, 188, locale["weekdays"])
    pdf.drawCentredString(PAGE_WIDTH / 2, 150, locale["weekend"])
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(PAGE_WIDTH / 2, 54, "Tannisbugtvej 68, 9881 Tversted")


def draw_menu_header(pdf, page_number, locale):
    draw_background(pdf)
    draw_title(pdf, MARGIN, PAGE_HEIGHT - 42, 0.55)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 39, "Tlf. 98 94 11 10")
    pdf.setFont("Helvetica", 8.2)
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 53, locale["header_info"])
    pdf.setStrokeColor(RED)
    pdf.setLineWidth(1.4)
    pdf.line(MARGIN, PAGE_HEIGHT - 68, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 68)
    pdf.setFillColor(ORANGE)
    pdf.rect(MARGIN, PAGE_HEIGHT - 82, PAGE_WIDTH - MARGIN * 2, 14, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 7.8)
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 78, locale["header_note"])
    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 7.5)
    pdf.drawCentredString(
        PAGE_WIDTH / 2,
        22,
        f"Amigo's Pizza & Grill | {locale['page']} {page_number}",
    )


def column_x(column):
    return MARGIN + column * (COLUMN_WIDTH + GUTTER)


def new_menu_page(pdf, page_number, locale):
    if page_number > 2:
        pdf.showPage()
    draw_menu_header(pdf, page_number, locale)
    return 0, TOP_Y


def next_column_or_page(pdf, column, page_number, locale):
    if column == 0:
        return 1, TOP_Y, page_number
    page_number += 1
    column, y = new_menu_page(pdf, page_number, locale)
    return column, y, page_number


def ensure_space(pdf, column, y, page_number, locale, needed):
    if y - needed >= BOTTOM_Y:
        return column, y, page_number
    return next_column_or_page(pdf, column, page_number, locale)


def draw_section(pdf, section, column, y, page_number, locale):
    column, y, page_number = ensure_space(pdf, column, y, page_number, locale, 58)
    x = column_x(column)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 12.5)
    pdf.drawString(x, y, section["category"].upper())
    if section.get("note"):
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica-Bold", 7.4)
        pdf.drawRightString(x + COLUMN_WIDTH, y + 1, section["note"])
    pdf.setStrokeColor(RED)
    pdf.setLineWidth(1)
    pdf.line(x, y - 5, x + COLUMN_WIDTH, y - 5)
    return column, y - 15, page_number


def draw_item(pdf, item, column, y, page_number, locale):
    number = item["number"]
    name = item["name"]
    description = item["description"]
    price = item["price"]
    number_width = 27 if number else 0
    price_width = 64
    name_width = COLUMN_WIDTH - number_width - price_width - 8
    name_lines = simpleSplit(name, "Helvetica-Bold", 8.6, name_width)
    desc_width = COLUMN_WIDTH - number_width - 6
    desc_lines = simpleSplit(description, "Helvetica-Oblique", 7.2, desc_width) if description else []
    needed = 4 + max(1, len(name_lines)) * 9.5 + len(desc_lines) * 7.7 + 3
    column, y, page_number = ensure_space(pdf, column, y, page_number, locale, needed)

    x = column_x(column)
    text_x = x + number_width
    price_x = x + COLUMN_WIDTH
    current_y = y
    pdf.setFillColor(INK)
    if number:
        pdf.setFont("Helvetica-Bold", 8.6)
        pdf.drawString(x, current_y, f"{number}.")
    pdf.setFont("Helvetica-Bold", 8.6)
    pdf.drawString(text_x, current_y, name_lines[0])
    pdf.drawRightString(price_x, current_y, price)
    current_y -= 9.5
    for line in name_lines[1:]:
        pdf.drawString(text_x, current_y, line)
        current_y -= 9.5
    if desc_lines:
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica-Oblique", 7.2)
        for line in desc_lines:
            pdf.drawString(text_x, current_y + 1, line)
            current_y -= 7.7
    pdf.setStrokeColor(LIGHT_LINE)
    pdf.setLineWidth(0.25)
    pdf.line(x, current_y + 3, x + COLUMN_WIDTH, current_y + 3)
    return column, current_y - 3, page_number


def estimate_item_height(item):
    number_width = 27 if item["number"] else 0
    price_width = 64
    name_width = COLUMN_WIDTH - number_width - price_width - 8
    name_lines = simpleSplit(item["name"], "Helvetica-Bold", 8.6, name_width)
    desc_width = COLUMN_WIDTH - number_width - 6
    desc_lines = (
        simpleSplit(item["description"], "Helvetica-Oblique", 7.2, desc_width)
        if item["description"]
        else []
    )
    return 7 + max(1, len(name_lines)) * 9.5 + len(desc_lines) * 7.7


def build_pdf(language):
    locale = LOCALES[language]
    menu = load_menu(language)
    pdf = canvas.Canvas(str(locale["output"]), pagesize=A4)
    pdf.setTitle(locale["title"])
    pdf.setAuthor("Amigo's Pizza & Grill")
    draw_cover(pdf, locale)
    pdf.showPage()

    page_number = 2
    column, y = new_menu_page(pdf, page_number, locale)
    for section in menu:
        section_height = 21 + sum(estimate_item_height(item) for item in section["items"])
        if section_height <= TOP_Y - BOTTOM_Y:
            column, y, page_number = ensure_space(
                pdf, column, y, page_number, locale, section_height
            )
        column, y, page_number = draw_section(pdf, section, column, y, page_number, locale)
        for item in section["items"]:
            column, y, page_number = draw_item(pdf, item, column, y, page_number, locale)
        y -= 6

    pdf.save()
    print(locale["output"])


def main():
    for language in ("da", "en"):
        build_pdf(language)


if __name__ == "__main__":
    main()
