#pip install requests-html
from requests_html import HTMLSession

#create the session
session = HTMLSession()

#define our URL
url = input("Enter Video Page URL:")

#use the session to get the data
r = session.get(url)

#Render the page, up the number on scrolldown to page down multiple times on a page
r.html.render(sleep=1, keep_page=True, scrolldown=1)

#take the rendered html and find the element that we are interested in
videos = r.html.find('#video-title-link')

#loop through those elements extracting the text and link
for item in videos:
    video = {
        'title': item.text,
        'link': item.absolute_links
    }
    print(video)
