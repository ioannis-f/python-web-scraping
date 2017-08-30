from lxml.html import fromstring
from advanced_link_crawler import download

url = 'http://example.webscraping.com/places/default/view/Singapore-203'
html = download(url)

tree = fromstring(html)
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print(area)
