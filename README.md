# Amigo's Pizza & Grill - digitalt menukort

Statisk, mobilvenlig HTML/CSS/JS-side klar til GitHub Pages.

## Filer

- `index.html` - sidens struktur og kontaktinfo
- `styles.css` - Amigo-inspireret rød/orange/blå styling
- `script.js` - menu-data, kategorier og søgning
- `print.html` og `print.css` - printvenligt PDF-layout
- `amigos-pizza-menukort.pdf` - PDF-version til download og print
- `assets/hero-pizza.webp` - komprimeret hero-billede til forsiden
- `assets/hero-pizza.png` - original genereret hero-billede som fallback

## Lokal test i VS Code

1. Åbn VS Code.
2. Vælg `File > Open Folder...`.
3. Åbn mappen `amigo-pizza-menu`.
4. Åbn `index.html`.
5. Højreklik og vælg `Open with Live Server`, hvis du har Live Server installeret.
6. Alternativt kan du dobbeltklikke på `index.html` i Stifinder.

## GitHub Pages

Korteste URL fås ved at lægge indholdet af `amigo-pizza-menu` i roden af et GitHub-repo, der også hedder `amigo-pizza-menu`.

Kommandoer fra VS Code Terminal, når du står inde i `amigo-pizza-menu`:

```powershell
git init
git add .
git commit -m "Add Amigo pizza menu"
git branch -M main
git remote add origin https://github.com/DIT-BRUGERNAVN/amigo-pizza-menu.git
git push -u origin main
```

På GitHub:

1. Gå til repoet `amigo-pizza-menu`.
2. Vælg `Settings`.
3. Vælg `Pages`.
4. Under `Build and deployment`, vælg `Deploy from a branch`.
5. Vælg branch `main` og folder `/root`.
6. Tryk `Save`.

Når siden er live, bliver linket typisk:

```text
https://DIT-BRUGERNAVN.github.io/amigo-pizza-menu/
```

## QR-kode

Når GitHub Pages-linket virker, kan QR-koden laves ud fra den endelige URL. Send linket videre i denne tråd, så kan QR-filen genereres til print.

## Opdater PDF

Hvis menuen ændres i `script.js`, kan PDF'en bygges igen med:

```powershell
pip install reportlab
python scripts/build-pdf.py
```

## Korrekturliste fra billederne

Menuen er læst manuelt fra billederne. Disse punkter bør dobbelttjekkes med et tættere foto:

- Ret nr. 54, 55 og 56 er ikke synlige i de uploadede billeder.
- Nr. 57 `Bøfsandwich` har ingen tydelig ingredienslinje på billedet.
- Nr. 83 `Kebab salat`, nr. 84 `Kylling salat` og burgerne nr. 75-80 har ingen tydelig ingredienslinje på billedet.
- Priser og retter bør korrekturlæses en ekstra gang før QR-koden printes.
