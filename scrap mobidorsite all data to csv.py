import requests
from bs4 import BeautifulSoup as bs
from csv import writer
import csv
# from requests import get
# from urlextract import URLExtract
# def listToString(s):
#     str1 = " "
#     return (str1.join(s))

def list_to_row(filename, list_elements):
    with open(filename, 'a+', newline='', encoding='utf-8') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_elements)

a_file = open('mobidorsite all urls.txt', 'r')
urllist = []
for line in a_file:
    stripped_line = line.strip()
    urllist.append(stripped_line)
a_file.close()

for url in urllist:
    response = requests.get(url)
    html = bs(response.text, 'html.parser')
    h2s = html.find('div', {'class': 'entry-content clear'})

    title = html.find('h1').text
    print(title)

    infodata1 = h2s.findAll('ul')[0]
    pricedata1 = h2s.findAll('table')[0]
    specificationdata1 = h2s.findAll('table')[2]
    prosconsdata = h2s.findAll('table')[3]

    ext_imlinks = [link.get("src") for link in h2s("img") if "i0.wp" in link.get("src")]
    img1 = ext_imlinks[0]
    img2 = ext_imlinks[-1]
    img4 = ext_imlinks[3]
    img1final = img1.split('?')[0]
    img2final = img2.split('?')[0]
    img4final = img4.split('?')[0]

    final_list = [url, title, infodata1, pricedata1, specificationdata1, prosconsdata,
                  img1final, img2final, img4final ]
    list_to_row('000mobidor_final01.csv', final_list)