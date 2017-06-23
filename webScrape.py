from lxml import html
import requests
import urllib
import os

page = requests.get('http://www.tenth.org/about/staff')
tree = html.fromstring(page.content)

staffList = tree.xpath("//div[@id='all-staff']//a[@class='person']")

for person in staffList:
    name = person.xpath("header/h1/text()")[0]
    image = person.xpath('@style')

    if len(image) == 0:  # if there's no image, there's nothing else for us here.
        continue

    image = image[0][22:-1]

    names = name.split(' ')

    # some folks have titles in their names, so let's pull those.
    if names[0] == 'Dr.' or names[0] == 'Rev.':
        user = names[1][0] + names[2]
    else:
        user = names[0][0] + names[1]

    user = str.lower(user)

    # delete existing, then download new image
    if os.path.exists("rawImages/" + user + ".jpg"):
        os.unlink("rawImages/" + user + ".jpg")
    urllib.urlretrieve(image, "rawImages/" + user + ".jpg")  # somehow, this seems to also convert PNGs to JPGs?

    print "Downloaded image for " + user

