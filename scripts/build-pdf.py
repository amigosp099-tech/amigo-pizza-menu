import json
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "script.js"
OUTPUT = ROOT / "amigos-pizza-menukort-v2.pdf"
HERO_IMAGE = ROOT / "assets" / "hero-pizza.png"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 30
GUTTER = 22
COLUMN_WIDTH = (PAGE_WIDTH - (MARGIN * 2) - GUTTER) / 2
TOP_Y = PAGE_HEIGHT - 86
BOTTOM_Y = 44

RED = colors.HexColor("#c73725")
RED_DARK = colors.HexColor("#8f1f17")
ORANGE = colors.HexColor("#f15b32")
CREAM = colors.HexColor("#fff7ed")
INK = colors.HexColor("#221a17")
MUTED = colors.HexColor("#6f625d")
LIGHT_LINE = colors.HexColor("#eee2da")


def load_menu():
    source = SCRIPT.read_text(encoding="utf-8")
    match = re.search(r"const menu = (\[.*?\]);\s*const menuRoot", source, re.S)
    if not match:
        raise RuntimeError("Kunne ikke finde menu-data i script.js")

    data = match.group(1)
    data = re.sub(r"\b(category|note|items):", r'"\1":', data)
    return json.loads(data)


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
    scale = min(width / iw, height / ih)
    draw_w = iw * scale
    draw_h = ih * scale
    pdf.drawImage(
        image,
        x + (width - draw_w) / 2,
        y + (height - draw_h) / 2,
        draw_w,
        draw_h,
        preserveAspectRatio=True,
        mask="auto",
    )


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


def draw_cover(pdf):
    draw_background(pdf)
    draw_title(pdf, 72, PAGE_HEIGHT - 120, 1.35)

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 17)
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 214, "PIZZA & DURUM")
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 248, "SANDWICH & PASTA")
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 282, "SPECIALITETER")

    pdf.setFillColor(ORANGE)
    pdf.rect(86, PAGE_HEIGHT - 334, PAGE_WIDTH - 172, 26, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-BoldOblique", 15)
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 326, "Alle retter kan tages med ud af huset")

    fit_image(pdf, HERO_IMAGE, 92, 348, PAGE_WIDTH - 184, 200)

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(PAGE_WIDTH / 2 - 74, 304, "Tlf.")
    pdf.setFont("Helvetica-Bold", 41)
    pdf.drawCentredString(PAGE_WIDTH / 2 + 46, 292, "98 94 11 10")

    pdf.setFillColor(RED)
    pdf.circle(154, 196, 48, fill=1, stroke=0)
    pdf.circle(PAGE_WIDTH - 154, 196, 48, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(154, 212, "Bemærk")
    pdf.drawCentredString(154, 195, "Åbent hele")
    pdf.drawCentredString(154, 178, "året")
    pdf.drawCentredString(PAGE_WIDTH - 154, 214, "SMS")
    pdf.drawCentredString(PAGE_WIDTH - 154, 197, "din bestilling")
    pdf.drawCentredString(PAGE_WIDTH - 154, 180, "42 34 09 15")

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(PAGE_WIDTH / 2, 226, "ÅBNINGSTIDER")
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(PAGE_WIDTH / 2, 194, "MAN - FRE")
    pdf.drawCentredString(PAGE_WIDTH / 2, 164, "KL. 16 - 21")
    pdf.drawCentredString(PAGE_WIDTH / 2, 128, "LØR - SØN")
    pdf.drawCentredString(PAGE_WIDTH / 2, 98, "KL. 12 - 21")

    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawCentredString(PAGE_WIDTH / 2, 54, "Tannisbugtvej 68, 9881 Tversted")


def draw_menu_header(pdf, page_number):
    draw_background(pdf)
    draw_title(pdf, MARGIN, PAGE_HEIGHT - 42, 0.55)

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 39, "Tlf. 98 94 11 10")
    pdf.setFont("Helvetica", 8.5)
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 53, "Man-fre 16-21 | Lør-søn 12-21 | Tannisbugtvej 68")

    pdf.setStrokeColor(RED)
    pdf.setLineWidth(1.4)
    pdf.line(MARGIN, PAGE_HEIGHT - 68, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 68)

    pdf.setFillColor(ORANGE)
    pdf.rect(MARGIN, PAGE_HEIGHT - 82, PAGE_WIDTH - MARGIN * 2, 14, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 7.8)
    pdf.drawCentredString(
        PAGE_WIDTH / 2,
        PAGE_HEIGHT - 78,
        "Alle retter kan tages med ud af huset | Deep pan pizza +25,- | Ekstra tilbehør alm. 15,- / fam. 30,-",
    )

    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 7.5)
    pdf.drawCentredString(PAGE_WIDTH / 2, 22, f"Amigo's Pizza & Grill | Side {page_number}")


def column_x(column):
    return MARGIN + column * (COLUMN_WIDTH + GUTTER)


def new_menu_page(pdf, page_number):
    if page_number > 1:
        pdf.showPage()
    draw_menu_header(pdf, page_number)
    return 0, TOP_Y


def next_column_or_page(pdf, column, page_number):
    if column == 0:
        return 1, TOP_Y, page_number
    page_number += 1
    column, y = new_menu_page(pdf, page_number)
    return column, y, page_number


def ensure_space(pdf, column, y, page_number, needed):
    if y - needed >= BOTTOM_Y:
        return column, y, page_number
    return next_column_or_page(pdf, column, page_number)


def draw_section(pdf, section, column, y, page_number):
    column, y, page_number = ensure_space(pdf, column, y, page_number, 34)
    x = column_x(column)

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 13)
    pdf.drawString(x, y, section["category"].upper())

    if section.get("note"):
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica-Bold", 7.6)
        pdf.drawRightString(x + COLUMN_WIDTH, y + 1, section["note"])

    pdf.setStrokeColor(RED)
    pdf.setLineWidth(1)
    pdf.line(x, y - 5, x + COLUMN_WIDTH, y - 5)
    return column, y - 15, page_number


def draw_leader(pdf, start_x, end_x, y):
    if end_x <= start_x:
        return
    pdf.setStrokeColor(colors.HexColor("#4d403a"))
    pdf.setLineWidth(0.55)
    pdf.setDash(0.8, 3.1)
    pdf.line(start_x, y, end_x, y)
    pdf.setDash()


def draw_item(pdf, item, column, y, page_number):
    number, name, desc, price = item
    x = column_x(column)
    number_width = 27 if number else 0
    price_width = 52
    text_x = x + number_width
    price_x = x + COLUMN_WIDTH
    name_width = COLUMN_WIDTH - number_width - price_width - 12

    name_lines = simpleSplit(name, "Helvetica-Bold", 8.8, name_width)
    desc_lines = simpleSplit(desc, "Helvetica-Oblique", 7.4, COLUMN_WIDTH - number_width - 6) if desc else []
    needed = 4 + max(1, len(name_lines)) * 10 + len(desc_lines) * 8 + 3

    column, y, page_number = ensure_space(pdf, column, y, page_number, needed)
    x = column_x(column)
    text_x = x + number_width
    price_x = x + COLUMN_WIDTH
    current_y = y

    pdf.setFillColor(INK)
    if number:
        pdf.setFont("Helvetica-Bold", 8.8)
        pdf.drawString(x, current_y, f"{number}.")

    pdf.setFont("Helvetica-Bold", 8.8)
    pdf.drawString(text_x, current_y, name_lines[0])
    name_end = text_x + pdf.stringWidth(name_lines[0], "Helvetica-Bold", 8.8) + 5
    draw_leader(pdf, name_end, price_x - price_width + 5, current_y + 3)
    pdf.drawRightString(price_x, current_y, price)
    current_y -= 10

    for line in name_lines[1:]:
        pdf.drawString(text_x, current_y, line)
        current_y -= 10

    if desc_lines:
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica-Oblique", 7.4)
        for line in desc_lines:
            pdf.drawString(text_x, current_y + 1, line)
            current_y -= 8

    pdf.setStrokeColor(LIGHT_LINE)
    pdf.setLineWidth(0.25)
    pdf.line(x, current_y + 3, x + COLUMN_WIDTH, current_y + 3)
    return column, current_y - 3, page_number


def build_pdf():
    menu = load_menu()
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4)
    pdf.setTitle("Amigo's Pizza & Grill - Menukort")
    pdf.setAuthor("Amigo's Pizza & Grill")

    draw_cover(pdf)
    pdf.showPage()

    page_number = 2
    column, y = new_menu_page(pdf, page_number)

    for section in menu:
        column, y, page_number = draw_section(pdf, section, column, y, page_number)
        for item in section["items"]:
            column, y, page_number = draw_item(pdf, item, column, y, page_number)
        y -= 7

    pdf.save()
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
