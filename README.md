# lambda_s3_cleaner
A lambda function to help keep your s3 bucket pristine and save $$$!

## Setup

Paste `s3_cleaner.py` into the code box. 

**Runtime**: python2.7

**Role**: Make a role with `S3FullAccess`.  Use that role.

**Triggers**  Pick S3.  Pick `Objet Created (All).  Select your bucket and (**optional!!**) key prefix and/or suffix.


### Optional - Slack Webhook

Do you want to be notified in slack every time someone is trying muck up your bucket?  Yeah, you probably do.

Make the slack boolean `True` and add your webhook and channel or user to post at.  *Easy peezy.*

## Todo

1. Ansible or Terraform deployment
2. Other webhooks (twitter? snapchat? etc??)
