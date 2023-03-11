#pip install requests-html
#First Run will install Chromium
from requests_html import HTMLSession

#create the session
session = HTMLSession()

#define our URL and scrolls on Page
url = input("Enter Video Page URL: ")
#scroll_down = int(input("Enter number of Scrolls on Page URL: "))

#use the session to get the data
r = session.get(url)

#Render the page, up the number on scrolldown to page down multiple times on a page
r.html.render(sleep=1, keep_page=True, scrolldown=1)

#take the rendered html and find the element that we are interested in
if "videos" in url:
    videos = r.html.find('#video-title-link')
else:
    videos = r.html.find('#video-title')

#loop through those elements extracting the text and link
for item in videos:
    video = {
        'title': item.text,
        'link': item.absolute_links
    }
    print(video)
