import requests

# Set time to get a response in fixed time incase website is not responding it will wait only for fixed time not hang forever
r = requests.get("http://httpbin.org/delay/2", timeout=3)

print(r.text)

# # Logging and get data
# r = requests.get(
#     "http://httpbin.org/basic-auth/rapid/testing", auth=("rapid", "testing")
# )

# print(
#     r
# )  # code: 200 (Sucessful authentication), code: 401 (Unsuccessful authentication.)
# print(r.text)  # Print the text of the page after authentication


# # To Post data using requests.post and passing data as parameter
# payload = {"username": "rapid292", "password": "testing"}  # Form Data
# r = requests.post("http://httpbin.org/post", data=payload)

# r_dict = r.json() # Provide dictionary with all info related request

# print(r_dict)


# # To specific url passing disctionary as parameter
# payload = {"page": 2, "count": 25}  # Dict
# r = requests.get("http://httpbin.org/get", params=payload)

# print(r.url)  # Output: http://httpbin.org/get/?page=2&count=25


# Printing image from  the page
# with open("img.png", "wb") as f:
#     f.write(r.content) # Writes the content i.e. image in file img.png


# Checking Status of the website

# Http status codes : 200 - success, 300 - redirects, 400 - clients Error, 500 - server errors(like site crashes etc.)
# print(r.status_code)

# print(r.ok)  # provides only Client Error or Server Error response in boolean

# print(r.headers) # provide indepth of website
