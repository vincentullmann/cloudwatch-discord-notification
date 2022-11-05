
# Lambda Function to send Discord Messages from CloudWatch Events

## Config:

Lambda / Environment variables
- add `WEBHOOK_URL` to your Lambda 

Lambda / Triggers 
- Add Trigger: CloudWatch Logs
- Log Group: the log group to watch
- Filter Name: anything
- Filter Pattern: eg.: "Traceback"

