'''import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

url = "https://www.writingbeginner.com/hangman-words/"
#res = requests.get(url, verify=False)
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

words = set()  

for li in soup.select("li"):
    text = li.get_text().strip().lower()
    if text and " " not in text:  
        words.add(text)


word_bank = sorted(words)

print(f"Collected {len(word_bank)} words.") '''
#I've come back after a while and it is not working. They may have made a work-around for they don't appreciate web scraping
#visited, the website- it made me do a captcha so ig they don't appreciate bots


#v2 - after some html source code analysis, we understand that it now uses json as it is a WordPress site
import requests
from bs4 import BeautifulSoup

url = "https://www.writingbeginner.com/wp-json/wp/v2/posts/31205"
res = requests.get(url)
data = res.json()

html_content = data["content"]["rendered"]

soup = BeautifulSoup(html_content, "lxml")

words = set()
for li in soup.select("li"):
    text = li.get_text().strip().lower()
    if text and " " not in text:
        words.add(text)

word_bank = sorted(words)
print(f"Collected {len(word_bank)} words.")

#while CloudFare captcha protects the rendered site, WordPress often remains publically available
#instead of going to the rendered site, we got to the REST API database for wordpress to directly get the data, which is less protected
