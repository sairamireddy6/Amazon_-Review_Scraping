import requests
from bs4 import BeautifulSoup
import pandas as pd


link = "https://www.amazon.in/LG-24-inch-Monitor-Freesync-Borderless/dp/B08J5Y9ZSV/ref=sr_1_2?dchild=1&pf_rd_i=976392031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=fdf29120-98d8-40f7-810a-585fb8aa67c1&pf_rd_r=9NSA2WH49QR1TJ0815CK&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1634737622&smid=A14CZOWI0VEHLG&sr=8-2&th=1"

page = requests.get(link).content

soup = BeautifulSoup(page,'html.parser')



""" To get reviewer  """
reviewer = []
names = soup.find_all('span',class_='a-profile-name')
for i in range(0,len(names)):
    reviewer.append(names[i].get_text())
print(reviewer)



""" To get posted_date """
posted_date = []
date = soup.find_all('span',class_='review-date')
for y in range(0,len(date)):
    posted_date.append(date[y].get_text())

""" To remove 'Reviewed in India on' from posted_date"""
posted_date[:] = [reviews.lstrip('Reviewed in India on ') for reviews in posted_date]
print(posted_date)



""" To get review_text """
review_text = []
rewiew = soup.find_all('div',{"data-hook":"review-collapsed"})
for s in range(0,len(rewiew)):
    review_text.append(rewiew[s].get_text())

""" To remove '\n' from review_text"""
review_text[:] = [reviews.lstrip('\n') for reviews in review_text]
review_text[:] = [reviews.rstrip('\n') for reviews in review_text]
print(review_text)

excel = pd.DataFrame()
excel['reviewer']=reviewer
excel['posted_date']=posted_date
excel['review_text']=review_text

print(excel)
excel.to_excel(r'C:\Users\sairam\OneDrive\Desktop\Customaise Analytics Private Limited\reviews.xlsx',index=False)