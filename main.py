from bs4 import BeautifulSoup
import requests

page_to_scrape_houston = requests.get("https://www.sports-reference.com/cfb/schools/houston/2022.html#all_team")
soup = BeautifulSoup(page_to_scrape_houston.text, "html.parser")
#https://www.sports-reference.com/cfb/schools/houston/2022.html#all_team
# https://www.espn.com/college-football/team/stats/_/id/248/season/2022
QBs = soup.find_all                                     

