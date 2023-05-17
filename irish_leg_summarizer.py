# coding: utf-8
from transformers import pipeline
summarizer = pipeline("summarization", model="./summary_model")
text = "summarize: The Inflation Reduction Act lowers prescription drug costs, health care costs, and energy costs. It's the most aggressive action on tackling the climate crisis in American history, which will lift up American workers and create good-paying, union jobs across the country. It'll lower the deficit and ask the ultra-wealthy and corporations to pay their fair share. And no one making under $400,000 per year will pay a penny more in taxes."
summarizer(text)
import requests
from bs4 import BeautifulSoup
link = "https://www.irishstatutebook.ie/eli/2023/si/21/made/en/print"
html = requests.get(link).text
soup = BeautifulSoup(html, "html.parser")
article = soup.find(class_='act-content')
summarizer(article.text)
get_ipython().run_line_magic('save', '')
