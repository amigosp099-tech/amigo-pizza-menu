import json
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "script.js"
OUTPUT = ROOT / "amigos-pizza-menukort.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 28
GUTTER = 18
COLUMN_WIDTH = (PAGE_WIDTH - (MARGIN * 2) - GUTTER) / 2
TOP_Y = PAGE_HEIGHT - 98
BOTTOM_Y = 46

RED = colors.HexColor("#c73725")
RED_DARK = colors.HexColor("#8f1f17")
ORANGE = colors.HexColor("#f15b32")
BLUE = colors.HexColor("#2d6fbe")
INK = colors.HexColor("#221a17")
MUTED = colors.HexColor("#66564d")
LINE = colors.HexColor("#dec4b2")


def load_menu():
    source = SCRIPT.read_text(encoding="utf-8")
    match = re.search(r"const menu = (\[.*?\]);\s*const menuRoot", source, re.S)
    if not match:
        raise RuntimeError("Kunne ikke finde menu-data i script.js")

    data = match.group(1)
    data = re.sub(r"\b(category|note|items):", r'"\1":', data)
    return json.loads(data)


def draw_header(pdf, page_number):
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 25, "2025")

    pdf.setFillColor(ORANGE)
    pdf.setFont("Helvetica-Bold", 31)
    pdf.drawString(MARGIN, PAGE_HEIGHT - 38, "AMIGO'S")
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(MARGIN, PAGE_HEIGHT - 62, "PIZZA & GRILL")

    pdf.setFillColor(BLUE)
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(MARGIN, PAGE_HEIGHT - 78, "PIZZA & DURUM · SANDWICH & PASTA · SPECIALITETER")

    pdf.setFillColor(RED_DARK)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 50, "Tlf. 98 94 11 10")
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica", 9)
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 66, "SMS 42 34 09 15")
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 80, "Man-fre 16-21 · Lør-søn 12-21")
    pdf.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 94, "Tannisbugtvej 68, 9881 Tversted")

    pdf.setStrokeColor(RED)
    pdf.setLineWidth(2)
    pdf.line(MARGIN, PAGE_HEIGHT - 88, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 88)

    pdf.setFillColor(ORANGE)
    pdf.rect(MARGIN, PAGE_HEIGHT - 116, PAGE_WIDTH - (MARGIN * 2), 18, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 9.5)
    pdf.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 111, "Alle retter kan tages med ud af huset · Deep pan pizza +25,-")

    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 8)
    pdf.drawCentredString(PAGE_WIDTH / 2, 22, f"Amigo's Pizza & Grill · Side {page_number}")


def new_page(pdf, page_number):
    if page_number > 1:
        pdf.showPage()
    draw_header(pdf, page_number)
    return 0, TOP_Y


def column_x(column):
    return MARGIN + column * (COLUMN_WIDTH + GUTTER)


def next_column_or_page(pdf, column, page_number):
    if column == 0:
        return 1, TOP_Y, page_number
    page_number += 1
    column, y = new_page(pdf, page_number)
    return column, y, page_number


def ensure_space(pdf, column, y, page_number, needed):
    if y - needed >= BOTTOM_Y:
        return column, y, page_number
    return next_column_or_page(pdf, column, page_number)


def draw_section(pdf, section, column, y, page_number):
    column, y, page_number = ensure_space(pdf, column, y, page_number, 30)
    x = column_x(column)

    pdf.setFillColor(RED_DARK)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, section["category"].upper())

    if section.get("note"):
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica-Bold", 7.5)
        pdf.drawRightString(x + COLUMN_WIDTH, y, section["note"])

    pdf.setStrokeColor(RED)
    pdf.setLineWidth(0.75)
    pdf.line(x, y - 4, x + COLUMN_WIDTH, y - 4)
    return column, y - 13, page_number


def draw_item(pdf, item, column, y, page_number):
    number, name, desc, price = item
    x = column_x(column)
    price_width = 52
    number_width = 24 if number else 0
    name_width = COLUMN_WIDTH - price_width - number_width - 10
    name_lines = simpleSplit(name, "Helvetica-Bold", 8.6, name_width)
    desc_lines = simpleSplit(desc, "Helvetica-Oblique", 7.2, COLUMN_WIDTH - number_width - 4) if desc else []
    needed = 5 + len(name_lines) * 10 + len(desc_lines) * 8

    column, y, page_number = ensure_space(pdf, column, y, page_number, needed)
    x = column_x(column)
    text_x = x + number_width

    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 8.6)
    if number:
        pdf.drawString(x, y, f"{number}.")

    current_y = y
    for line in name_lines:
        pdf.drawString(text_x, current_y, line)
        current_y -= 10

    pdf.setFont("Helvetica-Bold", 8.8)
    pdf.drawRightString(x + COLUMN_WIDTH, y, price)

    if desc_lines:
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica-Oblique", 7.2)
        for line in desc_lines:
            pdf.drawString(text_x, current_y + 1, line)
            current_y -= 8

    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(0.35)
    pdf.line(x, current_y + 3, x + COLUMN_WIDTH, current_y + 3)
    return column, current_y - 3, page_number


def build_pdf():
    menu = load_menu()
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4)
    page_number = 1
    column, y = new_page(pdf, page_number)

    for section in menu:
        column, y, page_number = draw_section(pdf, section, column, y, page_number)
        for item in section["items"]:
            column, y, page_number = draw_item(pdf, item, column, y, page_number)
        y -= 7

    pdf.save()
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
