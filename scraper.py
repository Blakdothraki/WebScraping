import csv

from bs4 import BeautifulSoup
import requests

page = requests.get("https://quotes.toscrape.com/")
BS = BeautifulSoup(page.text, "html.parser")
quotes = BS.findAll("span", {"class": "text"})
authors = BS.findAll("small", {"class": "author"})

with open("quotes.csv", "w") as file:
    write = csv.writer(file)
    write.writerow(["QUOTES", "AUTHORS"])
    for quote, author in zip(quotes, authors):
        write.writerow([quote.text, author.text])
print("Quotes have been written to 'quotes.txt'")
