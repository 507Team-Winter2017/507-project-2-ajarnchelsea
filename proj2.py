import urllib.request
from bs4 import BeautifulSoup
import ssl

#proj2.py
### Your Problem 1 solution goes here


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_url = 'http://www.nytimes.com'
html = urllib.request.urlopen(base_url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')
 

a = soup.find_all(class_="story-heading")
a = a[:10]
for story_heading in a: 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url2 = 'http://www.michigandaily.com'
html2 = urllib.request.urlopen(base_url2, context = ctx).read()
soup2 = BeautifulSoup(html2, 'html.parser')

most = soup2.ol.find_all("li")
for item in most:
	x = item.a
	print(x.text)


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url3 = "http://newmantaylor.com/gallery.html"
html3 = urllib.request.urlopen(base_url3, context = ctx).read()
soup3 = BeautifulSoup(html3, 'html.parser')

imgs = soup3.find_all("img")
for img in imgs:
	x = img.get("alt", "")
	if len(x) > 0:
		print(x)
	else:
		print ("No alternate text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
counter = 1
for i in range(6):
	if i == 0:
		base_url4 = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
		req = urllib.request.Request(base_url4, None, {'User-Agent': 'SI_CLASS'})
		html4 = urllib.request.urlopen(req, context = ctx).read()
		soup4 = BeautifulSoup(html4, 'html.parser')
	else:
		page_num = "&page=" + str(i)
		base_url4 = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4" + page_num
		req = urllib.request.Request(base_url4, None, {'User-Agent': 'SI_CLASS'})
		html4 = urllib.request.urlopen(req, context = ctx).read()
		soup4 = BeautifulSoup(html4, 'html.parser')


	emails = soup4.find_all("div", class_="field field-name-contact-details field-type-ds field-label-hidden")
	for email in emails:
		for item in email.find_all("a"):
			x = item["href"]
			base_url5 = "https://www.si.umich.edu" + str(x)
			req2 = urllib.request.Request(base_url5, None, {'User-Agent': 'SI_CLASS'})
			html5 = urllib.request.urlopen(req2, context = ctx).read()
			soup5 = BeautifulSoup(html5, 'html.parser')
			y = (soup5.find_all("div", class_="field field-name-field-person-email field-type-email field-label-inline clearfix"))
			for item in y:
				for email in item.find_all("a"):
					z = email["href"]
					print (str(counter) + " " + z[7:])
					counter += 1


