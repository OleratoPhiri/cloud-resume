import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-counter')

def lambda_handler(event, context):
    """
    This function runs every time the visitor counter API is called.
    It adds 1 to the count in DynamoDB and returns the new total.
    """

    # Update the count — add 1 to whatever the current value is
    response = table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='SET #count = if_not_exists(#count, :start) + :increment',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={
            ':increment': 1,
            ':start': 0
        },
        ReturnValues='UPDATED_NEW'
    )

    # Get the new count value
    count = int(response['Attributes']['count'])

    # Return the count with CORS headers
    # CORS lets your browser (on a different domain) call this API
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': count})
    }