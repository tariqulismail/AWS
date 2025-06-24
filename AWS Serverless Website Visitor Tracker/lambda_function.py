import json
import boto3
from datetime import datetime
import urllib.request

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WebsiteVisitors')

def get_location(ip):
    try:
        with urllib.request.urlopen(f"http://ip-api.com/json/{ip}") as url:
            data = json.loads(url.read().decode())
            return {
                'country': data.get('country'),
                'region': data.get('regionName'),
                'city': data.get('city'),
                'lat': data.get('lat'),
                'lon': data.get('lon'),
            }
    except:
        return {}


def lambda_handler(event, context):
    headers = event.get('headers', {})
    request_context = event.get('requestContext', {})

    ip = request_context.get('identity', {}).get('sourceIp', 'unknown')
    user_agent = headers.get('User-Agent', headers.get('user-agent', 'unknown'))
    visit_time = str(datetime.utcnow())
    location = get_location(ip)
    key = f"{ip}_{user_agent}" if ip != 'unknown' else 'unknown'

    try:
        response = table.get_item(Key={'user_key': key})
        item = response.get('Item', {})

        if item:
            item['count'] = int(item.get('count', 0)) + 1
            item['last_visit'] = visit_time
        else:
            item = {
                'user_key': key,
                'ip': ip,
                'user_agent': user_agent,
                'count': 1,
                'first_visit': visit_time,
                'last_visit': visit_time,
                'country': location.get('country'),
                'city': location.get('city'),
                'lat': str(location.get('lat')),
                'lon': str(location.get('lon'))
            }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Visitor tracked successfully",
                "user_key": key,
                "count": item['count']
            })
        }


        cloudwatch = boto3.client('cloudwatch')

        cloudwatch.put_metric_data(
            Namespace='VisitorAnalytics',
            MetricData=[
                {
                    'MetricName': 'TotalVisits',
                    'Dimensions': [{'Name': 'Country', 'Value': location.get('country', 'Unknown')}],
                    'Value': 1,
                    'Unit': 'Count'
                }
            ]
        )


    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Error processing request",
                "error": str(e)
            })
        }