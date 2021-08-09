import csv
import requests
import time
from bs4 import BeautifulSoup

with open('samples.csv','w', newline='') as fd:
    writer = csv.writer(fd, delimiter=',')
    writer.writerow(["movie","sentence","score"])
    
    for i in range(1, 150):
        URL = "https://movie.naver.com/movie/point/af/list.naver?&page=%d" %(i)
        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')

        movies = soup.select("tbody > tr")

        for m in movies:
            m_name = m.select_one("a").text
            m_score = m.select_one("em").text
            
            m_review = m.text.split('\n')[7]
            if m_review == "":
                continue

            writer.writerow([m_name,m_review,m_score])

        time.sleep(0.5)