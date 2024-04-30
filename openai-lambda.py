import json
from urllib import request, parse

print('Loading function')


def lambda_handler(event, context):
    
    body = event.get('body', None)  # Using .get() is safer in case 'body' key does not exist
    
    if body is None:
        return {
            "statusCode": 400,
            "body": json.dumps("No body found in the request")
        }
  
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_OPENAI_API_KEY"  # Replace YOUR_OPENAI_API_KEY with your actual OpenAI API key
    }
    
    data = {
        "model": "gpt-4-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistent, helping users around AWS Lambda "}, {"role": "user", "content": body}],
        "temperature": 0.7
    }
    
    
    # Convert data dictionary to JSON string
    json_data = json.dumps(data)
    json_data_bytes = json_data.encode('utf-8')  # Convert string to bytes
    
    # Set up the request
    req = request.Request(url, data=json_data_bytes, headers=headers, method='POST')
    
    # Send the request and capture the response
    with request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        
    return {"response": response_body}
    #raise Exception('Something went wrong')
