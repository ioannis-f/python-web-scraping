import re
from advanced_link_crawler import download

url = 'http://example.webscraping.com/places/default/view/Singapore-203'
html = download(url)

print(re.findall(r'<td class="w2p_fw">(.*?)</td>', html))

print(re.findall('<td class="w2p_fw">(.*?)</td>', html)[1])

print(re.findall('''<tr id="places_area__row">.*?<td\s*class=["']w2p_fw["']>(.*?)</td>''', html))
