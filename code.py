import pandas as pd
from selenium.webdriver import Chrome
import time

num_pages = 20
url = f'https://www.startupindia.gov.in/content/sih/en/search.html?roles=Startup&page={num_pages}'

names = []
links = []

driver = Chrome()
# driver.implicitly_wait(30)
driver.get(url)
# time.sleep(2)

startups = driver.find_elements_by_class_name('img-wrap')
print(len(startups))

for startup in startups:
    links.append(startup.get_attribute('href'))
    details = startup.find_elements_by_class_name('events-details')
    name, stage, location = details[0].text.split('\n')
    names.append(name)

driver.close()

dict = {'Name': names, 'Link': links}
df = pd.DataFrame(dict)
df.drop_duplicates(inplace=True)
print(df.shape[0])
df.to_csv('startups.csv', index=False)
