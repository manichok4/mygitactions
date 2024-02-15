//connect to dynamodb

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

  
  response = table.put_item(
    Item={
            
