# Control FarmBot with Python

# Up and Running

 0. Read about [CeleryScript](https://github.com/FarmBot/farmbot-js/wiki/Celery-Script) and [our use of MQTT](https://github.com/FarmBot/farmbot-js/wiki/Using-Raw-MQTT) first. This is important stuff!
 1. [Install Paho-MQTT](https://pypi.python.org/pypi/paho-mqtt/1.1#installation)
 2. Try the examples below, preferably in order.

# Examples

**IMPORTANT NOTE:** If you do not generate a token via `token_generation_example.py`, _none of these examples will work_.

 * `token_generation_example.py` - Learn how to create an API token. You need
    this to login to the MQTT server.
 * `subscribe_example.py` - Learn how to _listen_ to incoming data. Running this script is a great way to observe real world commands used by the Web App.
 * `publish_example.py` - Learn how to _send_ CeleryScript RPC nodes to the device.
