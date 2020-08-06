
# comments:
# css selector learning source: https://www.w3schools.com/cssref/css_selectors.asp
# soup objects use css selector sintax with method select - therefore if you would have read the documentation carefully you would have known that already

# problem 1 - resolved partialy. PLease finish it.
import requests
from bs4 import BeautifulSoup
import pprint

site = 'https://hub.packtpub.com/tag/python/' # the general link to the site

def main(n:int, c:int): # n - number of news to be iterated, c - min number of comments
	"This is the function that will get the n and c arguments and will call the needed code writen bellow"
	  #find the max number of pages to iterate
	page_list_main = iterate_pages(get_page_limit())

	#selected_news = list()
	num = 0

	for page in page_list_main:
		news_attr_main = extract_news(page)
		#print(news_attr_main)
		for item in news_attr_main:    # item is a new
			num += 1
	
			if int(item[2]) >= c and num <= n:
				#selected_news = selected_news.append(item)
				print("new's number", num)
				print("The new's title is:    {}   , and the link to it is \n   {}\n" .format(item[0], item[1]))
	
	pass


def iterate_pages(max_page):
	"Iterate the entire range of news pages and return a list of soup objects. Each object representing the respective page content"

	page_list = list()

	for p in range(1, int(max_page) + 1):
		page_link = site + "page/{}/".format(p)
		# print(page_link)
		res = requests.get(page_link)
		soup = BeautifulSoup(res.text, 'html.parser')
		page_list.append(soup)

	return page_list # return list of tuples


def extract_news(soup_object):
	"Function gets a soup object representing the entire page, then extracts only the news data out of it and packs them in a tuple "

	links = soup_object.select('div[class=td-block-span6] h3 a[rel=bookmark]')
	comments = soup_object.select('div[class=td-module-comments] a')
	
	news_attr = list()

	for n, comment in zip(links, comments):
		title = n.get('title')
		href = n.get('href')
		c = comment.getText()
		news_attr.append((title, href, c))

	return news_attr # return list of tuples



def get_page_limit():
	"Get the maximum range of pages that must be iterated. Returns int value"

	res = requests.get(site)
	soup = BeautifulSoup(res.text, 'html.parser')

	pages = soup.select('div span[class=pages]') # get the element with the max page numbers
	text = pages[0].getText()

	last_character = text.split(' ')[-1] # isolate the max page number
	return last_character

main(70, 2)
# news_pages = iterate_pages(2)


# problem 2 - you must resolve it. Apply the same logic as in problem 1, but this time for site: https://feeder.co/discover/programming. Here you have a list of blog posts. Each blog post has a specific number of followers. You need to return a list of tuples. Each tuple has 3 mebers - title of the blog, link to the blog post, and number of followers. You must arange the tuples in the list in descending order according to the number of followers. 

