import collections
import json 
import os
import requests

#store the webhook url with export='http:xxxxx'

webhook = os.environ.get("STORED_WEBHOOK")

#check ig the url has been exported and present in the variable path   
if webhook is None:
    raise Exception("No webhooks found")

data = {
        'text': 'Hey Jagruti is Connected to Slack'
    }

#post this to 
requests.post(
    webhook, json.dumps(data),
    headers={'Content-Type': 'application/json'}
)

print("output")