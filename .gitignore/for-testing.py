"""
import tkinter
window=tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# used to show obj in windows
lable=tkinter.Label(window,text="Abhay basani").pack()
window.mainloop()
# ===========================================================================

import os
os.environ['PYTHONPATH'].split(os.pathsep)       #running path where file is
os.system('cmd /k "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"')         #install pip.py
os.system('cmd /k "cmd pip --version"')          #know running python version
os.system('cmd /k "ipconfig"')
os.environ['PYTHON'].split(os.pathsep)      #path where python module store
os.system('cmd /k "python get-pip.py"')
k=os.system('cmd /k ""')
py -m pip install --upgrade pip            #for update pip so package should install properly
print(k)
"""
# =======================================================================================================================
# If you want to scrape a website:
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal
#
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# print(anchors)

# Get first element in the HTML page
# print(soup.find('p') )

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if (link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents:
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0]
print(elem)


