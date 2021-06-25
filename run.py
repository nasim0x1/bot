from mybot import LinkedInBot
import time
import slack
import os

class Bot:
    def __init__(self):

        # SLACK_TOKEN = "xoxp-714528761526-712373871424-2185449950881-308bfc1da28c9444cbecf4dababad899"
        # SECRET = "79bd653f024c1d5065ce9dd6634ac9"
        # self.CHANNEL_NAME = "#linkedin_notifications"

        SLACK_TOKEN = "xoxb-2203603573413-2219300700961-HnMOx0Vao5uY1e5eayRahiO9"
        self.CHANNEL_NAME = "#fiverr"

        self.message_client = slack.WebClient(token=SLACK_TOKEN)
        self.delay = 6*60*60
        self.bot = LinkedInBot(self.CHANNEL_NAME)
        

    def start(self):
        while True:
            body = self.bot.get_message_payload()
            respone = self.message_client.chat_postMessage(**body)
            print(respone)
            time.sleep(self.delay)



if __name__ == "__main__":
    Bot().start()