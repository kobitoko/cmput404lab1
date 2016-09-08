import requests

# does the request lib actually work
print requests.__version__

# doing https gives you SNIMissingWarning because installed python is old.
response = requests.get("http://google.com")

# gave 200 because it automatically follows redirects, unlike curl.
# need to disable that manually if you dont want it to follow redirects.
print response.status_code

response2 = requests.post("http://ccid-eddieantonio.rhcloud.com/billy_the-kid")
print response2.status_code
print response2.content

gitResponse = requests.get("https://raw.githubusercontent.com/kobitoko/cmput404lab1/master/lab1.py")
print gitResponse.text
