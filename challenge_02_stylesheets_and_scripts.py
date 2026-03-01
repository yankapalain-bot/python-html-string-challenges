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

stylesheet = "main.min.css"
script_file = "bundle.js"

# Update link href value
old_styles = "styles.css"
start_index = html.find(old_styles)
end_index = start_index + len(old_styles)
html = html[:start_index] + stylesheet + html[end_index:]



# script src value
old_script = "app.js"
start_index = html.index(old_script)
end_index = start_index + len(old_script)

html = html[:start_index] + script_file + html[end_index:]

print(html)

# EXTENSION
#It is possible in a real html page to have more than one href or src attribute
#so you need to modify only the intended section
#for this purpose, you can use an argument with find to indicate where you want to make change

#old_script = "app.js"
#head_close_pos = html.find("</head>")
#head_close_pos = html.find("</head>")
#start_script = html.find(old_script, head_close_pos)
#end_script = start_script + len(old_script)

#html = html[:start_script] + script_file + html[end_script:]


#print(html)
