import mechanicalsoup
import argparse

browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
browser.open("http://www.se.rit.edu/~swen-331")

for link in browser.page.select('a'):
    print(link.text)