import requests
from bs4 import BeautifulSoup
from tkinter import *

window = Tk()
window.title("Hacker News")
window.minsize(width=1200, height=800)
window.geometry("1200x800")
window.resizable(width=True, height=True)

my_title = Label(text="Hacker News", font=('Verdana', 12, 'bold'))
my_title.pack()

my_label = Label()
my_label.config(fg="white")
my_label.pack()

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.content, 'html.parser')

headlines = soup.find_all('td', class_="title")

for headline in headlines:
    headline_label = Label(text=headline.text, font=('Verdana', 10, 'normal'))
    headline_label.pack()

window.mainloop()
