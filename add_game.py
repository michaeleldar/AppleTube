from urllib.request import urlopen

def generate_page(link, user):
    temp = str(link).replace('https://', 'https://api.')
    page_text = urlopen(temp)
    html_bytes = page_text.read()
    html_text = html_bytes.decode("utf-8")
    letters = ""
    qoutes_happened = False
    title_text = ""
    colon_happened = False
    done = False
    for x in html_text:
        if done == False:
            if letters == "title":
                if x == ":":
                    colon_happened = True
                if colon_happened == True:
                    if x == "\"":
                        if qoutes_happened == True:
                            qoutes_happened = False
                            done = True
                        else:
                            qoutes_happened = True
                    if qoutes_happened == True:
                        title_text += x
            else:
                if x == "t":
                    letters += "t"
                elif x == "i":
                    letters += "i"
                elif x == "l":
                    letters = "title"
    title_text = title_text.replace("\"", "")
    title_text_code = title_text.replace(" ", "_")
    title_text_code = title_text_code.replace("/", "_")
    html_page = open("games/" + title_text_code + ".html", 'w')
    html_page.write("<!DOCTYPE html>\n")
    html_page.write("<html>\n")
    html_page.write("<head>\n")
    html_page.write("<title>AppleTube</title>\n")
    html_page.write("<link rel=\"stylesheet\" href=\"../style.css\">\n")
    html_page.write("<script src=\"../script.js\"></script>\n")
    html_page.write("</head>\n")
    html_page.write("<body>\n")
    html_page.write("<h1>" +  title_text +"</h1>\n")
    html_page.write("<h2>made by </h2>\n")

generate_page("https://scratch.mit.edu/projects/564962221/", 1)