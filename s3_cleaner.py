from __future__ import print_function

import json
import urllib, urllib2
import boto3
from datetime import date, timedelta

s3 = boto3.resource('s3')
# If you want slack notifications (and you do, duh, slack notifications are awesome)
# Make this True and fill out the slack portion of the code with your stuff
slack = False

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')

    s3_bucket = s3.Bucket(bucket)

    print('Cleaning up this awful mess : ' + bucket + '/' + key)
    response = s3_bucket.delete_objects(Delete = {'Objects': [{'Key':key}]})
    print(response)
    if slack:
        message = 'Cleaned up this trash: ' + bucket + '/' + key
        color = "good"
        icon_emoji = ":beers:"

        headers = {"Content-Type":"application/json","charset":"utf-8"}
        slack_url = "YOUR SLACK WEBHOOOK URL GOES HERE"
        slack_data = {
            "channel": "YOUR CHANNEL OR USERNAME GOES HERE",
            "username": "S3 CLEANBOT XL2000",
            "icon_emoji": icon_emoji,
            "attachments":[{
                "text":  message,
                "color": color,
            }]
        }

        slack_req = urllib2.Request(slack_url, data=json.dumps(slack_data).encode('utf-8'))
        response = urllib2.urlopen(slack_req).read()
        print('Slack response: ' + response)
    return 1
