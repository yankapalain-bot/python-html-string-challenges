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
</body>
</html>"""

page_title = "My Awesome Portfolio"
page_lang = "fr"


#html = html.replace('lang="en"', f'lang="{page_lang}"')
#html = html.replace("My Page", page_title)


# Adanced EXTENSION:
# The .replace() method accepts a third argument called "count".
# This limits how many occurrences of the target substring are replaced.
# In larger HTML documents, a string like "My Page" might appear multiple times
# To change the <title> tag and not other occurrences,
# we should limit the replacement count to 1.

html = html.replace('lang="en"', f'lang="{page_lang}"', 1)
html = html.replace("My Page", page_title, 1)
print(html)