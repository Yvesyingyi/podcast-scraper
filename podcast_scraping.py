import requests
import wget
import time
from bs4 import BeautifulSoup
import re

def request_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def get_tag_contents(tag):
    tag_content = str(tag.string)
    try:
        tag_href = tag['href']
    except:
        tag_href = ''
    return tag_content, tag_href

def get_next_url(soup):
    trigger_next = False
    for tag in soup.findAll("a"):
        tag_content, tag_href = get_tag_contents(tag)
        if trigger_next == True:
            return tag_href
        if tag_content == "Main":
            trigger_next = True

def download_files(soup):
    for tag in reversed(soup.findAll("a")):
        tag_content, tag_href = get_tag_contents(tag)
        if re.match(r'^.*\.mp3$', tag_href):
            print("Downloading", tag_content, "from", tag_href)
            # wget.download(tag_href, './' + tag_content + ".mp3")

url = "https://www.revolutionspodcast.com/2014/07/index.html"
while True:
    if url == "https://www.revolutionspodcast.com/2015/12/index.html":
        print("Complete.")
        break
    print("*****Visiting", url, "*****")
    soup = request_page(url)
    url = get_next_url(soup)
    download_files(soup)
    time.sleep(1)
