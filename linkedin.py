import requests
from bs4 import BeautifulSoup
from os import environ

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'rdonovan2004@gmail.com',
    'session_password': environ.get('LINKEDIN_PW'),
    'loginCsrfParam': csrf,
    }

client.post(LOGIN_URL, data=login_information)

result = client.get('https://www.linkedin.com/in/marek-balla-50381170')
soup = BeautifulSoup(result.text,  "html.parser")
result = soup.select("#top-card > div > div.profile-card.vcard > div.profile-overview > div.profile-overview-content > table")
print (result)
#top-card > div > div.profile-card.vcard > div.profile-overview > div.profile-overview-content > table
