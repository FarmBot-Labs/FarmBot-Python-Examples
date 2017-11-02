import json
import urllib2

# Get an API token using email / password.
data = {'user': {'email': 'user@user.com', 'password': 'password123'}}

# To generate the token, we POST JSON to `api/tokens`.
req = urllib2.Request('https://my.farmbot.io/api/tokens')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))

# It will return a JSON object...
raw_json = response.read()
token_data = json.loads(raw_json)

# ... response_body.token.encoded is the important part- you will use this as
# an MQTT password.
the_token = token_data['token']['encoded']
token_info = token_data['token']['unencoded']

print("\n\nYou will need to know your device_id to use MQTT.\n")
print("Your device id is: \n" + token_info['bot'] + "\n")
print("The MQTT Host is: \n" + token_info['mqtt'] + "\n")
# You can copy/paste this data and move on to `subscribe_example.py`.
print("The token is: \n" + the_token)
