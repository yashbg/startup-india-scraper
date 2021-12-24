import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.startupindia.gov.in/content/sih/en/search.html'

num_pages = 2
params = {'roles': 'Startup', 'page': num_pages}

r = requests.get(url, params)

soup = BeautifulSoup(r.text, 'html5lib')

results = soup.find(id='persona-results')
startups = results.find_all('div', class_='col-md-4 col-sm-6 col-space20')

for startup in startups:
    print(startup)
