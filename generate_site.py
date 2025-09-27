import os
import random

# Кольорові палітри та шрифти
COLOR_PALETTES = [
    {"primary": "#3498db", "secondary": "#2ecc71", "accent": "#e74c3c", "background": "#ecf0f1", "text": "#2c3e50"},
    {"primary": "#9b59b6", "secondary": "#f1c40f", "accent": "#e67e22", "background": "#ffffff", "text": "#34495e"},
]

FONTS = [
    "Arial, sans-serif",
    "'Courier New', monospace",
    "'Lucida Console', monospace"
]

# Секції сайту
SECTIONS = ["hero", "features", "contacts"]

# Генерація index.html
def generate_html(colors, font, layout_order):
    html_content = f"""<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="styles.css">
<title>Простий сайт</title>
</head>
<body>
"""

    for section in layout_order:
        if section == "hero":
            html_content += f"""
<section class="hero">
    <h1>Ласкаво просимо на наш сайт!</h1>
    <a href="#contacts" class="btn">Зв'язатися</a>
</section>
"""
        elif section == "features":
            html_content += """
<section class="features">
    <h2>Наші особливості</h2>
    <div class="cards">
        <div class="card">Особливість 1</div>
        <div class="card">Особливість 2</div>
        <div class="card">Особливість 3</div>
    </div>
</section>
"""
        elif section == "contacts":
            html_content += """
<section class="contacts" id="contacts">
    <h2>Контакти</h2>
    <form>
        <input type="text" placeholder="Ваше ім'я">
        <input type="email" placeholder="Ваш email">
        <textarea placeholder="Повідомлення"></textarea>
        <button type="submit">Відправити</button>
    </form>
</section>
"""
    html_content += "\n</body>\n</html>"
    return html_content

# Генерація styles.css
def generate_css(colors, font):
    return f"""
body {{
    margin: 0;
    font-family: {font};
    background-color: {colors['background']};
    color: {colors['text']};
}}

.hero {{
    text-align: center;
    padding: 100px 20px;
    background-color: {colors['primary']};
    color: white;
}}

.btn {{
    display: inline-block;
    padding: 10px 20px;
    background-color: {colors['accent']};
    color: white;
    text-decoration: none;
    border-radius: 5px;
}}

.features {{
    padding: 50px 20px;
    text-align: center;
}}

.cards {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}}

.card {{
    background-color: {colors['secondary']};
    padding: 20px;
    border-radius: 10px;
    flex: 1 1 200px;
}}

.contacts {{
    padding: 50px 20px;
    text-align: center;
}}

.contacts input, .contacts textarea {{
    display: block;
    width: 100%;
    max-width: 400px;
    margin: 10px auto;
    padding: 10px;
}}

.contacts button {{
    padding: 10px 20px;
    background-color: {colors['primary']};
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}}

@media (max-width: 768px) {{
    .cards {{
        flex-direction: column;
    }}
}}
"""

def main():
    # Створення папки dist
    if not os.path.exists("dist"):
        os.makedirs("dist")

    # Випадкова палітра, шрифт та порядок секцій
    colors = random.choice(COLOR_PALETTES)
    font = random.choice(FONTS)
    layout_order = SECTIONS.copy()
    random.shuffle(layout_order)

    # Генерація файлів
    with open("dist/index.html", "w", encoding="utf-8") as f:
        f.write(generate_html(colors, font, layout_order))

    with open("dist/styles.css", "w", encoding="utf-8") as f:
        f.write(generate_css(colors, font))

    print("Сайт згенеровано у папці dist/")

if __name__ == "__main__":
    main()
