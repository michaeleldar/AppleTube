from urllib.request import urlopen

def generate_page(link, user):
    temp = str(link).replace('https://', 'https://api.')
    page_text = urlopen(temp)
    html_bytes = page_text.read()
    html_text = html_bytes.decode("utf-8")

generate_page("https://scratch.mit.edu/projects/634444414/", 1)