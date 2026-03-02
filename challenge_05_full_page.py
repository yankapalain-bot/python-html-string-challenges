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


html = html.replace('lang="en"', 'lang="es"', 1)
html = html.replace("My Page", "Full Page Challenge", 1)

stylesheet = "main.min.css"
script_file = "main.bundle.js"

# Update link href value
head_close_pos = html.find("<title>")
old_styles = "styles.css"
start_index = html.find(old_styles, head_close_pos)
end_index = start_index + len(old_styles)
html = html[:start_index] + stylesheet + html[end_index:]


# script src value
old_script = "app.js"
start_index = html.index(old_script, head_close_pos)
end_index = start_index + len(old_script)

html = html[:start_index] + script_file + html[end_index:]

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"
body_content = (
    f"    <h1>{h1}</h1>\n"
    f"    <h2>{h2}</h2>\n"
    f"    <h3>{h3}</h3>\n"
)

parts = html.split("<body>", 1)

if len(parts) == 2:
    html = parts[0] + "<body>\n" + body_content + parts[1]
else:
    print("Error: <body> tag not found.")

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

#function to extract content tag
def extract_tag_content(html_string, tag):
    opening_tag = "<" + tag + ">"
    closing_tag = "</" + tag + ">"
    
    start_pos = html_string.find(opening_tag)
    if start_pos == -1:
        return None
    
    start_pos += len(opening_tag)
    
    end_pos = html_string.find(closing_tag, start_pos)
    if end_pos == -1:
        return None
    
    return html_string[start_pos:end_pos]

#title_start = html.find("<title>") + len("<title>")
#title_end = html.find("</title>")

page_title_content = extract_tag_content(html,"title")
newparagraph_text = "    The second paragraph in Step 6 requires you to extract the title text dynamically from the string. Extend this idea: write a generalised extraction snippet that, given any tag name as a string variable "
newp_tag = (
    f"   <p>"
    f"    <h1>{page_title_content}</h1>\n"
    f" {newparagraph_text}"
    f" </p>"
)

body_close_pos = html.find("</body>")

html = html[:body_close_pos] + newp_tag + html[body_close_pos:]

print(html)


### THIS PART WAS COMMENTED BEFORE REDIRECT into the html output file
styles_count = html.count("styles.css")
script_count = html.count("app.js")

if styles_count == 0 and script_count == 0:
    print("\n✅ SUCCESS: Both 'styles.css' and 'app.js' were fully replaced.")
else:
    if styles_count > 0:
        print(f"\n❌ ERROR: 'styles.css' still appears {styles_count} time(s).")
    if script_count > 0:
        print(f"❌ ERROR: 'app.js' still appears {script_count} time(s).")
    

print("\n--- VALIDATION REPORT ---")

test_title = html.count("<title>Full Page Challenge</title>")
if test_title == 1:
    print("\n ✅ <title> is correct")

test_h1 = html.count("<h1>")
test_h2 = html.count("<h2>")
test_h3 = html.count("<h3>")

if test_h1 == 2:
    print("\n ✅ <h1> found")
if test_h2 == 1:
    print("\n ✅ <h2> found")
if test_h3 == 1:
    print("\n ✅ <h3> found")

test_img = html.count("<img")
if test_img == 1:
    print("\n ✅ <img> appears exactly once")

test_p = html.count("<p>")
if test_p == 2:
    print("\n ✅ <p> appears exactly twice")

if html.startswith("<!DOCTYPE html>"):
   print("\n ✅ Starts with <!DOCTYPE html>")

if html.endswith("</html>"):
   print("\n ✅ Ends with </html>")
 
print("------------------------")