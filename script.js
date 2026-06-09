const menu = [
  {
    category: "Pizza",
    note: "Alm. / Fam.",
    items: [
      ["1", "Margherita", "Tomat, ost, oregano", "75,- / 150,-"],
      ["2", "Vesuvio", "Tomat, ost, skinke, oregano", "79,- / 158,-"],
      ["3", "Pepperoni", "Tomat, ost, pepperoni, oregano", "79,- / 158,-"],
      ["4", "Capricciosa", "Tomat, ost, skinke, champignon, oregano", "81,- / 162,-"],
      ["5", "Hawaii", "Tomat, ost, skinke, ananas, oregano", "81,- / 162,-"],
      ["6", "Vegetarisk", "Tomat, ost, paprika, ananas, løg, champignon, oliven, oregano", "89,- / 178,-"],
      ["7", "Ciao", "Tomat, ost, skinke, pepperoni, cocktailpølser, bacon, kødsauce, oregano", "95,- / 190,-"],
      ["8", "Chaplin", "Tomat, ost, skinke, cocktailpølser, kødsauce, oregano", "92,- / 184,-"],
      ["9", "Bearnaise", "Tomat, ost, skinke, pepperoni, bearnaisesauce, oregano", "92,- / 184,-"],
      ["10", "Rimmi", "Tomat, ost, tun, rejer, krabbe, hvidløg, oregano", "92,- / 184,-"],
      ["11", "Alino", "Tomat, ost, skinke, pepperoni, kødsauce, oregano", "92,- / 184,-"],
      ["12", "Hopsan", "Tomat, ost, pepperoni, kødsauce, løg, hvidløg, oregano", "94,- / 188,-"],
      ["13", "Gorgonzola", "Tomat, ost, kebab, champignon, løg, gorgonzola, oregano", "94,- / 188,-"],
      ["14", "Volcane", "Tomat, ost, skinke, pepperoni, oksekød, løg, jalapeños, hvidløg, oregano", "95,- / 190,-"],
      ["15", "Pisa", "Tomat, ost, skinke, oksekød, cocktailpølser, champignon, hvidløg, oregano", "94,- / 188,-"],
      ["16", "Stærk", "Tomat, ost, skinke, kebab, bacon, chili, oregano", "92,- / 184,-"],
      ["17", "Amigo", "Tomat, ost, skinke, pepperoni, bacon, løg, oregano", "92,- / 184,-"],
      ["18", "Mexicano", "Tomat, ost, kebab, chili, jalapeños, løg, pepperoni, oregano", "94,- / 188,-"],
      ["19", "Pompei", "Tomat, ost, skinke, kødsauce, bearnaisesauce, oregano", "92,- / 184,-"],
      ["20", "Din egen pizza", "4 slags efter selvvalg", "120,- / 240,-"],
      ["21", "Amerikansk", "Tomat, ost, skinke, kebab, kødsauce, løg, paprika, chili, oregano", "95,- / 190,-"],
      ["22", "Tversted", "Tomat, ost, kebab, kylling, pommes frites, bearnaisesauce, oregano", "95,- / 190,-"],
      ["23", "Natalie", "Tomat, ost, kylling, champignon, løg, karry, oregano", "92,- / 184,-"],
      ["24", "Mt. Love", "Tomat, ost, skinke, kebab, pepperoni, cocktailpølser, oksekød, bacon, oregano", "100,- / 200,-"],
      ["117", "Kartoffel Amigo", "Tomat, ost, kartoffelskiver, pesto, mozzarella ost, olivenolie", "90,- / 180,-"],
      ["118", "Kartoffel pizza", "Tomat, ost, kartoffelskiver, mozzarella ost, olivenolie", "92,- / 184,-"]
    ]
  },
  {
    category: "Gourmet pizza",
    note: "Alm. / Fam.",
    items: [
      ["25", "Mozzarella", "Tomat, ost, gorgonzola, parmaskinke, mozzarella, rucolasalat, pesto, oregano", "105,- / 210,-"],
      ["26", "La Mamba", "Tomat, ost, mozzarella, parmaskinke, artiskok, rucolasalat, tomatskiver, pesto, oregano", "105,- / 210,-"],
      ["27", "Fabio", "Tomat, ost, tun, rejer, løg, hvidløg, chili, oregano", "115,- / 230,-"],
      ["28", "Italiano", "Tomat, ost, mozzarella, parmaskinke, parmesan, tomatskiver, rucolasalat", "105,- / 210,-"]
    ]
  },
  {
    category: "Salat pizza",
    note: "Alm. / Fam.",
    items: [
      ["31", "Kebab pizza", "Tomat, ost, kebab, oregano, frisk salat, tomat, agurk, dressing", "92,- / 184,-"],
      ["32", "Coralia", "Tomat, ost, kebab, pepperoni, løg, frisk salat, oregano, tomat, agurk, dressing", "95,- / 190,-"],
      ["33", "Greko", "Tomat, ost, skinke, oksekød, pepperoni, frisk salat, oregano, tomat, agurk, dressing", "95,- / 190,-"],
      ["34", "Copenhagen", "Tomat, ost, kylling, kebab, pepperoni, frisk salat, oregano, tomat, agurk, dressing", "95,- / 190,-"]
    ]
  },
  {
    category: "Indbagt pizza",
    note: "Alm.",
    items: [
      ["35", "Cao cao", "Tomat, ost, skinke, oregano", "80,-"],
      ["36", "Matador", "Tomat, ost, skinke, rejer, champignon", "85,-"],
      ["37", "Amigo", "Tomat, ost, kylling, kebab, paprika, chili", "92,-"],
      ["38", "Pasta", "Tomat, ost, spaghetti, kødsauce", "92,-"]
    ]
  },
  {
    category: "Pasta retter",
    note: "",
    items: [
      ["39", "Spaghetti seafood", "Med rejer, gorgonzola, chili, hvidløg, salat, flødesauce", "95,-"],
      ["40", "Spaghetti Carbonara", "Med bacon, løg, æg, flødesauce, salat", "90,-"],
      ["41", "Spaghetti Bolognese", "Med kødsauce, salat", "80,-"],
      ["42", "Spaghetti Napoli", "Med kebab, kylling, chili, flødesauce, pesto, salat", "95,-"]
    ]
  },
  {
    category: "Sandwich / Pita / Rulle",
    note: "",
    items: [
      ["43", "Kylling sandwich", "Med ost, salat, dressing", "80,-"],
      ["44", "Kebab sandwich", "Med ost, salat, dressing", "80,-"],
      ["45", "Pita Kebab", "Med hjemmelavet pitabrød, kebab, salat, agurk, tomat, dressing", "70,-"],
      ["46", "Pita Kylling", "Med hjemmelavet pitabrød, kylling, salat, agurk, tomat, dressing", "70,-"],
      ["47", "Pita Falafel", "Med hjemmelavet pitabrød, salat, agurk, tomat, dressing", "70,-"],
      ["48", "Kebab rulle", "Med kebab, salat, agurk, tomat, dressing", "85,-"],
      ["49", "Kylling rulle", "Med kylling, salat, tomat, agurk, dressing", "85,-"],
      ["50", "Hvidløg brød", "Med ost", "75,-"]
    ]
  },
  {
    category: "Amigos specialiteter",
    note: "",
    items: [
      ["51", "Stjerneskud", "Med 2 stk. frisk fiskefilet, rejer, brød, kaviar, asparges, agurk, dressing, citron", "115,-"],
      ["52", "Fiskefilet", "Med 2 stk. frisk fiskefilet, citron, ketchup, remoulade, pommes frites", "99,-"],
      ["53", "Skinke schnitzel", "Med bearnaisesauce, pommes sautes, salat, tomat, agurk, dressing", "100,-"],
      ["57", "Bøfsandwich", "", "115,-"],
      ["58", "Dansk bøf", "Med hvide kartofler, skysauce og paprika", "115,-"],
      ["60", "Herregårds bøf", "Med kartoffelbåde, ærter, tomatskiver, bearnaisesauce", "115,-"]
    ]
  },
  {
    category: "Børne menu",
    note: "",
    items: [
      ["63", "Chicken nuggets", "Med pommes frites", "65,-"],
      ["64", "Frisk fiskefilet", "Med pommes frites", "65,-"],
      ["65", "Mickey pizza", "Tomat, ost, skinke, oregano", "60,-"],
      ["66", "Rana pizza", "Tomat, ost, cocktailpølser, kødsauce, oregano", "65,-"],
      ["67", "Anders And pizza", "Tomat, ost, skinke, pepperoni, oregano", "65,-"]
    ]
  },
  {
    category: "Grill & Burger",
    note: "",
    items: [
      ["68", "1/2 grill kylling", "Med pommes frites, salat, ketchup, remoulade, creme fraiche", "109,-"],
      ["69", "Pommes frites Lille/Med/Stor", "", "30,- / 40,- / 50,-"],
      ["70", "Kebab tallerken", "Kebab, salat, tomat, agurk, rød dressing, pommes frites", "89,-"],
      ["71", "Kylling tallerken", "Kylling, salat, tomat, agurk, pommes frites", "89,-"],
      ["119", "Pølsemix", "Pølser, pommes frites, salat, tomat, agurk, ketchup", "89,-"],
      ["72", "Nachos 1", "Med cheddarost, guacamole, salsa", "75,-"],
      ["73", "Nachos 2", "Med kylling, cheddarost, guacamole, salsa", "80,-"],
      ["74", "Snack kurv", "2 mozzarellasticks, 2 chilicheese, 2 nuggets, 2 indbagte rejer, 2 løgringe, BBQ sauce, mayo", "80,-"],
      ["75", "Kylling burger", "", "65,-"],
      ["76", "Big burger", "", "75,-"],
      ["77", "Bacon burger", "", "80,-"],
      ["78", "Cheese burger", "", "80,-"],
      ["79", "Bacon cheese burger", "", "90,-"],
      ["80", "Dobbelt burger", "", "100,-"]
    ]
  },
  {
    category: "Salater",
    note: "",
    items: [
      ["81", "Tun salat", "Med tun, majs, løg, frisk salat, agurk, tomat, dressing", "75,-"],
      ["82", "Græsk salat", "Med frisk salat, tomat, agurk, oliven, fetaost, dressing", "70,-"],
      ["83", "Kebab salat", "", "75,-"],
      ["84", "Kylling salat", "", "75,-"],
      ["85", "Reje salat", "Med rejer, kaviar, citron, dressing", "89,-"]
    ]
  },
  {
    category: "Drikkevarer",
    note: "",
    items: [
      ["", "Stor sodavand glas 0,50 cl", "", "50,-"],
      ["", "Lille sodavand glas 0,33 cl", "", "40,-"],
      ["", "Cocio", "", "30,-"],
      ["", "Kaffe", "", "25,-"],
      ["", "Te", "", "20,-"],
      ["", "Øl Lille/Stor", "", "45,- / 60,-"],
      ["", "Classic Øl Lille/Stor", "", "50,- / 65,-"],
      ["", "Juice lille / stor", "", "40,- / 50,-"],
      ["", "Dansk vand", "", "30,-"],
      ["", "Vand", "", "25,-"],
      ["", "1 flaske vin hvid, rød, rose", "", "210,-"],
      ["", "1 glas vin", "", "65,-"],
      ["", "Sodavand 0,33 cl Dåse", "", "30,-"],
      ["", "Sodavand 0,50 cl Dåse", "", "40,-"]
    ]
  }
];

const menuRoot = document.querySelector("#menu-root");
const categoryNav = document.querySelector("#category-nav");
const searchInput = document.querySelector("#menu-search");

function slugify(value) {
  return value
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)/g, "");
}

function itemMatches(item, category, query) {
  if (!query) return true;
  const searchable = [category, item[0], item[1], item[2], item[3]].join(" ").toLowerCase();
  return searchable.includes(query);
}

function renderNav() {
  categoryNav.innerHTML = menu
    .map((section) => `<a href="#${slugify(section.category)}">${section.category}</a>`)
    .join("");
}

function renderMenu(query = "") {
  const normalizedQuery = query.trim().toLowerCase();
  const sections = menu
    .map((section) => ({
      ...section,
      items: section.items.filter((item) => itemMatches(item, section.category, normalizedQuery))
    }))
    .filter((section) => section.items.length);

  if (!sections.length) {
    menuRoot.innerHTML = '<p class="empty">Ingen retter matcher din søgning.</p>';
    return;
  }

  menuRoot.innerHTML = sections
    .map((section) => {
      const id = slugify(section.category);
      const items = section.items
        .map(([number, name, desc, price]) => {
          const numberMarkup = number ? `<span class="item-number">${number}.</span>` : "";
          const descMarkup = desc ? `<p class="item-desc">${desc}</p>` : "";
          return `
            <article class="menu-item">
              <div class="item-main">
                <h3 class="item-title">${numberMarkup}<span class="item-name">${name}</span></h3>
                ${descMarkup}
              </div>
              <div class="item-price">${price}</div>
            </article>
          `;
        })
        .join("");

      return `
        <section id="${id}" class="menu-section">
          <div class="section-heading">
            <h2>${section.category}</h2>
            ${section.note ? `<span>${section.note}</span>` : ""}
          </div>
          <div class="items">${items}</div>
        </section>
      `;
    })
    .join("");
}

renderNav();
renderMenu();

searchInput.addEventListener("input", (event) => {
  renderMenu(event.target.value);
});
