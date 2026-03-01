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

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"
body_content = (
    f"    <h1>{h1}</h1>\n"
    f"    <h2>{h2}</h2>\n"
    f"    <h3>{h3}</h3>\n"
)

#parts = html.split("<body>")
#html = parts[0] + "<body>\n" + body_content + parts[1]


#EXTENSION
#.split("<body>") can produce multiple parts if <body> appear many time (in comment for example)
#to be sure that we split only the first occurence, we add argument "1" to .split() function
parts = html.split("<body>", 1)

if len(parts) == 2:
    html = parts[0] + "<body>\n" + body_content + parts[1]
else:
    print("Error: <body> tag not found.")

print(html)
