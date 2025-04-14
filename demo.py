from urllib.parse import quote_plus

username = "pranav_shepal"
password = "Pranav@07"
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)
print(encoded_username)
print(encoded_password)