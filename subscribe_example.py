import paho.mqtt.client as mqtt
# This information was created using `token_generation_example.py`.
my_device_id = "device_18"
# This information was created using `token_generation_example.py`.
my_token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBhZG1pbi5jb20iLCJpYXQiOjE1MDYzNzM2ODcsImp0aSI6ImUwMGNiOTFiLWYyMmYtNDI3Mi1hZmY4LWVkZDYxZTcyMjhlOCIsImlzcyI6Ii8vMTkyLjE2OC4xLjEyMTozMDAwIiwiZXhwIjoxNTA5ODI5Njg3LCJtcXR0IjoiMTkyLjE2OC4xLjEyMSIsIm9zX3VwZGF0ZV9zZXJ2ZXIiOiJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL2Zhcm1ib3QvZmFybWJvdF9vcy9yZWxlYXNlcy9sYXRlc3QiLCJmd191cGRhdGVfc2VydmVyIjoiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy9GYXJtQm90L2Zhcm1ib3QtYXJkdWluby1maXJtd2FyZS9yZWxlYXNlcy9sYXRlc3QiLCJib3QiOiJkZXZpY2VfMTgifQ.cshGOBHbkO5PlAKC7PIBzVMNiqOayVSpkuxnlhT_RwMcjaG59XRQW2n0Q_qlgApzvjAyr_Z6-AJDHN07SACOEr0lZQgfwj_WCzp5Y4jY6R953t0MW4uEnu1DGQ3uP9pNp_3iN-gKZ2dYeC6NLUKB0GDnMUV3J8UpYbUoaWdirfVjTF2gPY5_S_7dStVGSN18BVNOUVV-V_Hxqe5znK8FRgrUOccVaNm-vppMIUu3n6Uy5WiIiPWWoTya5hpvM34lMhKczk76CIIECUbx8hyQmNVmchuSNorHAmjOEH5DTRXtDAzBA9XlOY3Jw5d26V3BzlwmFy1y51C3FxYj7TwYEw"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # "bot/device_18/status" will broadcast the FarmBot "state tree"- it is a
    # data structure representing _all_ bot state, such as pin status, lock
    # lock status, installed farmware, etc.
    client.subscribe("bot/" + my_device_id + "/status")

    # "bot/device_18/logs" shows the messages typically seen in the status bar
    # of the web app. Like everything else on MQTT, it is encoded as JSON.
    client.subscribe("bot/" + my_device_id + "/logs")

    # "bot/device_18/from_clients" allows you to listen to your echo.
    # All incoming commands to the device will show up here.
    # We use a special form of JSON called "CeleryScript". Read more here:
    # https://github.com/FarmBot/farmbot-js/wiki/Celery-Script
    # https://github.com/FarmBot/farmbot-js/wiki/Using-Raw-MQTT
    client.subscribe("bot/" + my_device_id + "/from_clients")

    # "bot/device_18/from_device" contains all of FarmBot's responses to
    # commands. It's JSON, like everything else.
    client.subscribe("bot/" + my_device_id + "/from_device")


def on_message(client, userdata, msg):
    # Print stuff to the screen.
    # EXERCISE: Try running this script and pushing buttons on the Web App.
    #           You shoud see activity print to the screen.
    print("Incoming MQTT messages: ")
    print(msg.topic + " " + str(msg.payload))


# Connect to the broker...
client = mqtt.Client()
# ...using credentials from `token_generation_example.py`
client.username_pw_set(my_device_id, my_token)

# Attach event handlers:
client.on_connect = on_connect
client.on_message = on_message

# Finally, connect to the server:
client.connect("clever-octopus.rmq.cloudamqp.com", 1883, 60)

client.loop_forever()
