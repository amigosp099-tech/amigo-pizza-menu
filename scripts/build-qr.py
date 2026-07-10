from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.graphics.barcode import qr


ROOT = Path(__file__).resolve().parents[1]
MENU_URL = "https://amigos-pizza-menu.netlify.app/"

QR_PNG = ROOT / "Amigo-Pizza-QR-kode.png"
QR_SVG = ROOT / "Amigo-Pizza-QR-kode.svg"
POSTER_PNG = ROOT / "Amigo-Pizza-QR-plakat.png"
POSTER_NO_LINK_PNG = ROOT / "Amigo-Pizza-QR-plakat-uden-link.png"


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def draw_center(draw, text, y, text_font, fill, width):
    bbox = draw.textbbox((0, 0), text, font=text_font)
    x = (width - (bbox[2] - bbox[0])) / 2
    draw.text((x, y), text, font=text_font, fill=fill)


def make_qr():
    widget = qr.QrCodeWidget(MENU_URL)
    widget.qr.make()
    module_count = widget.qr.getModuleCount()
    quiet_zone = 4
    module_size = 28
    size = (module_count + quiet_zone * 2) * module_size

    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)

    rects = []
    for row in range(module_count):
        for col in range(module_count):
            if not widget.qr.isDark(row, col):
                continue
            x = (col + quiet_zone) * module_size
            y = (row + quiet_zone) * module_size
            draw.rectangle((x, y, x + module_size - 1, y + module_size - 1), fill="black")
            rects.append((x, y))

    image.save(QR_PNG, "PNG", optimize=True)

    rect_markup = "\n".join(
        f'  <rect x="{x}" y="{y}" width="{module_size}" height="{module_size}"/>'
        for x, y in rects
    )
    QR_SVG.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
        f'width="{size}" height="{size}">\n'
        f'  <rect width="100%" height="100%" fill="#fff"/>\n'
        f'  <g fill="#000">\n{rect_markup}\n  </g>\n'
        f'</svg>\n',
        encoding="utf-8",
    )


def make_poster(show_link=True):
    width, height = 1400, 2000
    bg = (255, 247, 237)
    charcoal = (33, 26, 24)
    orange = (241, 91, 50)
    red = (199, 55, 37)
    muted = (90, 74, 66)

    image = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, width, 215), fill=charcoal)
    draw_center(draw, "Amigo's Pizza & Grill", 58, font(62, True), (255, 255, 255), width)
    draw_center(draw, "Scan menukortet", 132, font(36, True), (255, 204, 71), width)

    qr_img = Image.open(QR_PNG).convert("RGB").resize((760, 760), Image.Resampling.NEAREST)
    qr_x = (width - qr_img.width) // 2
    qr_y = 330
    draw.rounded_rectangle(
        (qr_x - 58, qr_y - 58, qr_x + qr_img.width + 58, qr_y + qr_img.height + 58),
        radius=18,
        fill=(255, 255, 255),
    )
    image.paste(qr_img, (qr_x, qr_y))

    draw_center(draw, "Se menuen på mobilen", 1210, font(40, True), charcoal, width)

    if show_link:
        draw_center(draw, "amigos-pizza-menu.netlify.app", 1284, font(30, True), muted, width)
        button_y = 1425
    else:
        button_y = 1375

    button = (260, button_y, width - 260, button_y + 118)
    draw.rounded_rectangle(button, radius=16, fill=red)
    draw_center(draw, "Ring 98 94 11 10", button_y + 31, font(42, True), (255, 255, 255), width)

    draw_center(draw, "Tannisbugtvej 68, 9881 Tversted", height - 170, font(30, True), charcoal, width)
    draw_center(draw, "Man-søn 16-21", height - 118, font(28, True), muted, width)
    return image


def main():
    make_qr()
    make_poster(show_link=True).save(POSTER_PNG, "PNG", optimize=True)
    make_poster(show_link=False).save(POSTER_NO_LINK_PNG, "PNG", optimize=True)
    print(MENU_URL)
    print(QR_PNG)
    print(QR_SVG)
    print(POSTER_PNG)
    print(POSTER_NO_LINK_PNG)


if __name__ == "__main__":
    main()
