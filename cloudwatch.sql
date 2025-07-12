fields @timestamp, @message
| filter @message like /ERROR/
| stats count(*) as error_count by @message
| sort error_count desc
| limit 5
