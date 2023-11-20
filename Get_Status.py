import requests

#BaseURL
BaseURL='https://simple-books-api.glitch.me'
Response=requests.get(BaseURL)
# print(Response)

print(Response.status_code) #TO Featch HTTP Status Code
# print(Response.json()) #It will featch the message if avaliable like :{'message': 'Welcome to the Simple Books API.'}
print(Response.reason) #Will display like :Ok,Not Found
# print(Response.raw)
print(Response.text) #It will dispaly message same as per .json
# print(Response.content) #This will featch content like .text,.json()
