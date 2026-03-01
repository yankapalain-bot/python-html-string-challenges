html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
    <h1>Welcome to My Page</h1>
    <h2>About This Project</h2>
    <h3>Technical Details</h3>

</body>
</html>"""

paragraph_text = "This project was built entirely using Python string methods."
img_src = "hero.jpg"
img_alt = "A hero for the page"

p_tag = (
    f"   <p>"
    f" {paragraph_text}"
    f" </p>"
)

img_tag = (f"   <img")
img_tag = img_tag + (f' src="{img_src}"')
img_tag = img_tag + (f' alt="{img_alt}"')
img_tag = img_tag + (f">")

# pos_h1 = html.rfind("</h1")
# pos_h2 = html.rfind("</h2")
# pos_h3 = html.rfind("</h3")

# last_pos = max(pos_h1, pos_h2, pos_h3)

# if last_pos == pos_h1:
#     closing_tag = "</h1>"
# elif last_pos == pos_h2:
#     closing_tag = "</h2>"
# elif last_pos == pos_h3:
#     closing_tag = "</h3>"

# ADVANCED
#Generalize 
# Add a helper snippet to find the right insert position

closing_tags = ["</h1>", "</h2>", "</h3>"]

positions = []

# Find positions using .rfind()
for tag in closing_tags:
    pos = html.rfind(tag)
    if pos != -1:          # Filter out tags not found
        positions.append((pos, tag))

# Ensure at least one heading exists
if positions:
    # Pick the maximum position (latest in document)
    last_pos, last_tag = max(positions, key=lambda item: item[0])
    
    insert_pos = last_pos + len(last_tag)

    insertion = (
        "\n"
        + p_tag + "\n"
        + img_tag + "\n"
    )

    html = html[:insert_pos] + insertion + html[insert_pos:]

    print(html)


