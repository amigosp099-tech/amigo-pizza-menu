# Amigo's Pizza & Grill – digital menu

The GitHub Pages site opens with a Danish/English language selector:

- `index.html` – language selector used by the QR code
- `da/` – Danish digital menu
- `en/` – English digital menu
- `menu-da.pdf` – Danish printable menu
- `menu-en.pdf` – English printable menu
- `data/da.json` and `data/en.json` – menu data used by the website and PDFs

Live site:

<https://amigosp099-tech.github.io/amigo-pizza-menu/>

The existing QR code can still be used because it points to this root address.

## Updating the menus

The current brochure sources are:

- `../menu amigo/amigos_menu_template/index.html`
- `../menu amigo/engelsk version/index.html`

Run the following commands from this repository after changing either source:

```powershell
python scripts/sync-menu.py
python scripts/build-pdf.py
```

The first command updates both JSON files. The second command creates the
matching Danish and English PDFs.

## Local preview

Serve the folder through a local web server so the JSON menu data can load:

```powershell
python -m http.server 8765
```

Then open <http://127.0.0.1:8765/>.
