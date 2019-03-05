import json
# Let's blink an LED.

# We need the same credentials as before:
import paho.mqtt.client as mqtt
# This information was created using `token_generation_example.py`.
my_device_id = "device_18"
# This information was created using `token_generation_example.py`.
my_token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBhZG1pbi5jb20iLCJpYXQiOjE1MDYzNzM2ODcsImp0aSI6ImUwMGNiOTFiLWYyMmYtNDI3Mi1hZmY4LWVkZDYxZTcyMjhlOCIsImlzcyI6Ii8vMTkyLjE2OC4xLjEyMTozMDAwIiwiZXhwIjoxNTA5ODI5Njg3LCJtcXR0IjoiMTkyLjE2OC4xLjEyMSIsIm9zX3VwZGF0ZV9zZXJ2ZXIiOiJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2Zhcm1ib3QvZmFybWJvdF9vcy9yZWxlYXNlcy9sYXRlc3QiLCJmd191cGRhdGVfc2VydmVyIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9GYXJtQm90L2Zhcm1ib3QtYXJkdWluby1maXJtd2FyZS9yZWxlYXNlcy9sYXRlc3QiLCJib3QiOiJkZXZpY2VfMTgifQ.cshGOBHbkO5PlAKC7PIBzVMNiqOayVSpkuxnlhT_RwMcjaG59XRQW2n0Q_qlgApzvjAyr_Z6-AJDHN07SACOEr0lZQgfwj_WCzp5Y4jY6R953t0MW4uEnu1DGQ3uP9pNp_3iN-gKZ2dYeC6NLUKB0GDnMUV3J8UpYbUoaWdirfVjTF2gPY5_S_7dStVGSN18BVNOUVV-V_Hxqe5znK8FRgrUOccVaNm-vppMIUu3n6Uy5WiIiPWWoTya5hpvM34lMhKczk76CIIECUbx8hyQmNVmchuSNorHAmjOEH5DTRXtDAzBA9XlOY3Jw5d26V3BzlwmFy1y51C3FxYj7TwYEw"

# Now let's build an RPC command.
celery_script_rpc = {
    "kind": "rpc_request",
    "args": {
        "label": "cb78760b-d2f7-4dd1-b8ad-ce0626b3ba53"
    },
    "body": [{
        "kind": "toggle_pin",
        "args": {
            "pin_number": 13
        }
    }]
}

# Encode it as JSON...
json_payload = json.dumps(celery_script_rpc)

# Connect to the broker...
client = mqtt.Client()
# ...using credentials from `token_generation_example.py`
client.username_pw_set(my_device_id, my_token)


# An event handler for sending off data:
def on_connect(client, userdata, flags, rc):
    print("CONNECTED! Sending data now...")
    # "bot/device_18/from_device" contains all of FarmBot's responses to
    # commands. It's JSON, like everything else. If FarmBot is running, we will
    # see a response from this channel.
    client.subscribe("bot/" + my_device_id + "/from_device")

    # Publish that payload as soon as we connect:
    client.publish("bot/" + my_device_id + "/from_clients", json_payload)


def on_message(client, userdata, msg):
    print("Got a message: ")
    print(msg.topic + " " + str(msg.payload))


# Attach event handler:
client.on_connect = on_connect
client.on_message = on_message

# Finally, connect to the server:
client.connect("clever-octopus.rmq.cloudamqp.com", 1883, 60)
print("Here we go...")
client.loop_forever()
