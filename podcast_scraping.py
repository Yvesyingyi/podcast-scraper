# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

# initial url for french revolution
url = "https://www.revolutionspodcast.com/2014/07/index.html"

while True:
    print("Visiting", url)
    # Connect to the URL
    response = requests.get(url)
    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    # For identifying next page
    trigger_next = False
    # Check all <a> tags
    for tag in soup.findAll("a"):
        # get tag content string, tag href
        tag_content = str(tag.string)
        try:
            tag_href = tag['href']
        except:
            tag_href = ''
        # save next page url
        if trigger_next == True:
            url = tag_href
            trigger_next = False
        # identify next page url
        if tag_content == "Main":
            trigger_next = True
        # download mp3
        if re.match('^.*\.mp3$', tag_href):
            print("Downloading", tag_content, "from", tag_href, "...")
            urllib.request.urlretrieve(tag_href, './' + tag_content + ".mp3")
    time.sleep(1)  # pause the code for a sec
