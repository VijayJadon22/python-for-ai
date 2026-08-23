import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

#print("hello world) this will give an error which we can see by shift + Enter