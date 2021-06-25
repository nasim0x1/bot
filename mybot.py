from selenium import webdriver
import os
import time
from urllib.parse import unquote
# Create the CoinBot Class
class LinkedInBot:

    # Create a constant that contains the default text for the message
    BOT_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Diversity Linkedln Notifications\n\n"
            ),
        },
    }

    # The constructor for the class. It takes the channel name as the
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel
        self.browser = webdriver.Chrome(os.getcwd()+"/chromedriver")


    # scrape the data from linkedin    
    def _scrape_data(self):
        #Open login page
        self.browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

        #Enter login info:
        elementID = self.browser.find_element_by_id('username')
        elementID.send_keys("vekkajifyo@biyac.com")

        elementID = self.browser.find_element_by_id('password')
        elementID.send_keys("Gh)tq,EiH4(?c2U")
        #Note: replace the keys "username" and "password" with your LinkedIn login info
        elementID.submit()

        hashtags = ["Diversity","Inclusion","Diverseandinclusive","D&L","metric","nationalaward",
                    "globalaward","Diversitylab","Vault","mansfieldrule","D&FAlliances",
                    "Minoritycounsel","Chicagocommittee","Diversion","AmericanBarAssociation","DisabilityInclusion",
                    "LegalProfessionAward","Europelegal",
                    "nationaldiversitycouncil","minoritycorporate",
                    "counselassociation","leadershipcouncil","legaldiversity","LGBTBar","americalegal","uklegal"]

        # hashtags = ["programname"]
        news_feeds = {}
        for index,tag in enumerate(hashtags):
            #Go to webpage
            self.browser.get(f'https://www.linkedin.com/search/results/content/?keywords=%23{tag}&origin=FACETED_SEARCH&sortBy=%22date_posted%22')
            # u = f'https://www.linkedin.com/search/results/content/?keywords=%23programname&origin=FACETED_SEARCH&sortBy=%22date_posted%22'

            try:
                elements_link = []
                try:
                    search_result_section = self.browser.find_element_by_xpath("""//*[@id="search-marvel-srp-scroll-container"]""")
                    ul_section = search_result_section.find_element_by_tag_name("ul")
                    item = ul_section.find_elements_by_tag_name("li")
                    for post in item:
                        post.click()
                        time.sleep(1)

                        url = unquote(self.browser.current_url)
                        url = (url.split("(")[-1]).split(",")[0]
                        post_url = f"https://www.linkedin.com/feed/update/{url}/"
                        elements_link.append(post_url)
                    print(f"Tag no {index+1} out of {len(hashtags)}:{tag}")
                except:
                    elements_link.append("No Post Found")


                links = ", ".join([str(item) for item in elements_link])
                news_feeds[tag] = links
            except Exception as E: 
                pass

        blocks = []
        for key in news_feeds.keys():
            blocks.append({"type":"section",
                            "text":{
                                "type":"mrkdwn",
                                "text":f"*POST UNDER #{key.upper()}* \n\n{news_feeds[key]}. \n\n\n\n"
                            }  
                        },
                        )
        return blocks


    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.BOT_BLOCK,
            ]+self._scrape_data(),
        }
                