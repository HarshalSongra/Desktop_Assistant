from googlesearch.googlesearch import GoogleSearch
import urllib2

response = GoogleSearch().search("Python")
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())
