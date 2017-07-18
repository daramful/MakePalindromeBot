import os
import logging
import urllib

# Grab the Bot OAuth token from the environment.
BOT_TOKEN = os.environ["Bot_Token"]

SLACK_URL = "https://slack.com/api/chat.postMessage"

def lambda_handler(data, context):
    if "challenge" in data:
        return data["challenge"]
        
    # Grab the Slack event data.
    slack_event = data['event']

    if "bot_id" in slack_event:
        logging.warn("Ignore bot event")
    else:
        text = slack_event["text"]
        palindromeText = text + text[::-1]
        
        channel_id = slack_event["channel"]
        
        data = urllib.parse.urlencode(
            (
                ("token", BOT_TOKEN),
                ("channel", channel_id),
                ("text", palindromeText)
            )
        )
        data = data.encode("ascii")
        
        request = urllib.request.Request(
            SLACK_URL, 
            data=data, 
            method="POST"
        )

        request.add_header(
            "Content-Type", 
            "application/x-www-form-urlencoded"
        )
        
        urllib.request.urlopen(request).read()

#Complete
    return "200 OK"
