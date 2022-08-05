import requests
import html5lib
from bs4 import BeautifulSoup

# url = "https://codewithharry.com"

#


#

# ============================================================================================================
url =input("[+]Enter complete url of website:> ")
print("""
1 ->website all anchors tag.
2 ->whole website html format.
3 ->Get all paragraph on website.
""")
info=input("[+]Enter what you want to geather:> ")
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
if info == 1:
    url = "https://codewithharry.com"
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    anchors = soup.find_all('a')
    all_links = set()
    # Get all the links on the page:
    for link in anchors:
        if (link.get('href') != '#'):
            linkText = "https://codewithharry.com" + link.get('href')
            all_links.add(link)
            print(linkText)

    navbarSupportedContent = soup.find(id='navbarSupportedContent')

elif info == 2:
    pass