import json
import urllib2
import paho.mqtt.client as mqtt  # pip install paho-mqtt

# ================================================
# RELEVANT INFORMATION:
# Password, email, server, etc..
# Please change this.
# ================================================
email = "___ PUT YOUR EMAIL HERE ___"
# Use ENV vars in the real world for added security.
password = "__PUT YOUR PASSWORD HERE ___"
server_host = "my.farmbot.io"

# ================================================
# This hash will be sent to the REST API as JSON.
# We need this to create an API token.
# ================================================
data = {
    'user': {
        'email': email,
        'password': password
    }
}


req = urllib2.Request("https://" + server_host + "/api/tokens")
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))

# The response will contain everything we need to
# connect to the MQTT server
response_json = json.loads(response.read())

# ================================================
# Now that we have an API token, let's connect to
# the MQTT server.
# ================================================

my_device_id = response_json['token']['unencoded']['bot']
my_token = response_json['token']['encoded']
# Never hardcode server names.
# Always use the server name provided in your API
# token.
mqtt_host = response_json['token']['unencoded']['mqtt']

# ================================================
# Let's create a CeleryScript RPC object.
# In this case, we are moving the device to
# Position (10, 10, 10) with an offset of
# (-3, -2, -1)
# ================================================

celery_script_rpc = {
    "kind": "rpc_request",
    "args": {
        "label": "MY_EXAMPLE_RPC_0x03ABC"  # Use UUIDs in realworld apps
    },
    "body": [{
        "kind": "move_absolute",
        "args": {
            "speed": 100,
            "offset": {
                "kind": "coordinate",
                "args": {
                    "z": -3,
                    "y": -2,
                    "x": 1
                }
            },
            "location": {
                "kind": "coordinate",
                "args": {
                    "z": 10,
                    "y": 10,
                    "x": 10
                }
            }
        }
    }]
}

# Callbacks used by Paho MQTT


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("bot/" + my_device_id + "/status")
    # client.subscribe("bot/" + my_device_id + "/logs")
    client.subscribe("bot/" + my_device_id + "/from_device")
    client.publish("bot/" + my_device_id + "/from_clients",
                   json.dumps(celery_script_rpc))


def on_message(client, userdata, msg):
    print("Incoming MQTT messages: ")
    print(msg.topic + " " + str(msg.payload))


# ================================================
# We have all the information we need.
# We can login to the MQTT server and send our
# RPC as soon as we connect.
# ================================================

client = mqtt.Client()
client.username_pw_set(my_device_id, my_token)

# Attach event handlers:
client.on_connect = on_connect
client.on_message = on_message

# Finally, connect to the server:
client.connect(mqtt_host, 1883, 60)

client.loop_forever()  # You should see an `rpc_ok` from the device on STDOUT
