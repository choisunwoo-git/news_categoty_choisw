# print("Hi")


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['[plitics', 'Eoconomic', 'Social', 'Culture', 'IT']

df_fitles = pd.DataFrame()
for i in range(6):
    url = "https://news.naver.com/section/10{}".format(i)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tags = soup.select('.sa_text_strong')
    titles = []
    for title_tag in title_tags:
        titles.append(title_tag.text)
    print(titles)
    df_section_titles = pd.DataFrame(titles, columns = ['titles'])
    df_section_titles['category'] = category[i]
    df_fitles = pd.concat([df_fitles, pd.DataFrame(titles)], ignore_index=True)
print(df_fitles.head())
print(df_fitles.info())
print(df_fitles.head['category'].value_counts())
df_fitles.to_csv('./crawling_data/naver_headline_news_{}.csv'.format(datetime.datetime.now().strftime("%Y%m%d")))


