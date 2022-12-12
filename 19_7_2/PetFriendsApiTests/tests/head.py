import requests
import requests

url = 'https://petfriends.skillfactory.ru'

#use the 'headers' parameter to set the HTTP headers:
x = requests.head(url)

print(x.status_code)
print(x.headers)


# # Making a HEAD request
# r = requests.head('https://petfriends.skillfactory.ru/', headers ={'Host':''})
#
# # check status code for response received
# # success code - 200
# print(r)
#
# # print headers of request
# print(r.headers)
#
# # checking if request contains any content
# print(r.content)
