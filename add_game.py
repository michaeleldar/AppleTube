from urllib.request import urlopen

from flask import g

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
    html_page.write("<link rel=\"stylesheet\" href=\"../../static/style.css\">\n")
    html_page.write("<script src=\"../../static/script.js\"></script>\n")
    html_page.write("</head>\n")
    html_page.write("<body>\n")
    html_page.write("<h1>" +  title_text + "</h1>\n")
    html_page.write("<h3>made by " + user + "</h3>\n")
    html_page.write("<p>\n")
    html_page.write("<iframe src=\"" + link + "embed\" allowtransparency=\"true\" width=\"485\" height=\"402\" frameborder=\"0\" scrolling=\"no\" allowfullscreen></iframe>\n")
    html_page.write("</p>\n")
    html_page.write("</body>\n")
    html_page.write("</html>\n")
    games_page = open("games.html", "r")
    games_page_lines = games_page.read().split("\n")
    games_page.close()
    games_page = open("games.html", "w")
    app_py = open("app.py", "a")
    for x in games_page_lines:
        if x.find("</p>") != -1:
            games_page.write("</p><br>")
            games_page.write("<p><a href=\"games/" + title_text_code + "\">" + title_text + "</a><br></p>\n")
        else:
            games_page.write(x + "\n")
    app_py.write("@app.route('/games/" + title_text_code + "')\n")
    app_py.write("def games_" + title_text_code + "(): ")
    app_py.write("    url_for('static', filename='style.css')")
    app_py.write("    url_for('static', filename='style.css')")
    


generate_page("https://scratch.mit.edu/projects/634444414/", "test")