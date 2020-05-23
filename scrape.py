from bs4 import BeautifulSoup
import requests


# instagram username
username = input("Hello, Enter your username: ")

# instagram user profile url
url = f"https://www.instagram.com/{username}/"

# response
source_code_response = requests.get(url)
response_code = source_code_response.status_code
response_html = source_code_response.text

# soup
soup = BeautifulSoup(response_html, 'html.parser')


if(int(response_code) == 404):
    print("User not found")
else:
    profile_info = soup.select_one("meta[property='og:description']")
    print(profile_info.get("content").split("-")[0])
