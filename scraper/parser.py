from bs4 import BeautifulSoup

def parse_quote(html):
    """
    This function takes a html url, with quotes inside, parse it and return a dictionnary with the quote and the author.
    """
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for item in soup.find_all("div", class_="quote"):
        quote = item.find(class_="text").text.strip()
        author = item.find(class_="author").text.strip()

        quotes.append({
            "quote": quote,
            "author": author
        })
    
    return quotes