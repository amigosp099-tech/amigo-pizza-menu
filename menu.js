const root = document.querySelector("#menu-root");
const nav = document.querySelector("#category-nav");
const search = document.querySelector("#menu-search");
const language = document.body.dataset.language || "da";
const dataUrl = document.body.dataset.menuData;

const text = {
  da: {
    loading: "Menuen indlæses...",
    empty: "Ingen retter matcher din søgning.",
    error: "Menuen kunne ikke indlæses. Prøv at genindlæse siden."
  },
  en: {
    loading: "Loading menu...",
    empty: "No dishes match your search.",
    error: "The menu could not be loaded. Please reload the page."
  }
}[language];

let menu = [];

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function slugify(value) {
  return value
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)/g, "");
}

function matches(item, category, query) {
  if (!query) return true;
  return [category, item.number, item.name, item.description, item.price]
    .join(" ")
    .toLowerCase()
    .includes(query);
}

function renderNav() {
  nav.innerHTML = menu
    .map((section) => {
      const id = slugify(section.category);
      return `<a href="#${id}">${escapeHtml(section.category)}</a>`;
    })
    .join("");
}

function renderMenu(query = "") {
  const normalized = query.trim().toLowerCase();
  const sections = menu
    .map((section) => ({
      ...section,
      items: section.items.filter((item) => matches(item, section.category, normalized))
    }))
    .filter((section) => section.items.length);

  if (!sections.length) {
    root.innerHTML = `<p class="empty">${escapeHtml(text.empty)}</p>`;
    return;
  }

  root.innerHTML = sections
    .map((section) => {
      const id = slugify(section.category);
      const items = section.items
        .map((item) => {
          const number = item.number
            ? `<span class="item-number">${escapeHtml(item.number)}.</span>`
            : "";
          const description = item.description
            ? `<p class="item-desc">${escapeHtml(item.description)}</p>`
            : "";
          return `
            <article class="menu-item">
              <div>
                <h3 class="item-title">${number}<span class="item-name">${escapeHtml(item.name)}</span></h3>
                ${description}
              </div>
              <div class="item-price">${escapeHtml(item.price)}</div>
            </article>
          `;
        })
        .join("");

      const note = section.note
        ? `<span>${escapeHtml(section.note)}</span>`
        : "";
      return `
        <section id="${id}" class="menu-section">
          <div class="section-heading">
            <h2>${escapeHtml(section.category)}</h2>
            ${note}
          </div>
          <div class="items">${items}</div>
        </section>
      `;
    })
    .join("");
}

async function loadMenu() {
  root.innerHTML = `<p class="loading">${escapeHtml(text.loading)}</p>`;
  try {
    const response = await fetch(dataUrl);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const payload = await response.json();
    menu = payload.sections;
    renderNav();
    renderMenu();
  } catch (error) {
    console.error(error);
    root.innerHTML = `<p class="empty">${escapeHtml(text.error)}</p>`;
  }
}

search.addEventListener("input", (event) => renderMenu(event.target.value));
loadMenu();
