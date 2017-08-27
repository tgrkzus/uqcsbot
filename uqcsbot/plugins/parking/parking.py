from errbot import BotPlugin, botcmd
from bs4 import BeautifulSoup
import requests

class Parking(BotPlugin):
    @botcmd  # flags a command
    def parking(self, msg, args):  # a command callable with !tryme
        page = requests.get("https://pg.pf.uq.edu.au/")
        if page.status_code == 200:
            soup = BeautifulSoup(page.content)
            body = soup.body.select("table#parkingAvailability")
            
            return body # This string format is markdown.
        else:
            return "There was an error getting information from the website"
