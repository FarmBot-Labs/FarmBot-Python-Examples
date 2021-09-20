# You Might Not Need This

These examples are old.

FarmBot now offers a [Python library](https://github.com/FarmBot/farmbot-py) to handle low level MQTT management.

Consider using the Python library instead.

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

# How Does It Work?

 * FarmBot uses [JSON Web Tokens (JWTs)](https://jwt.io) for authorization.
 * JWTs can contain "claims". A claim is just data encoded inside a token.
 * The `"mqtt"` claim in a FarmBot JWT is important because it tells you which MQTT server your account must use.
 * Currently, all users are routed to `clever-octopus.rmq.cloudamqp.com` as their MQTT server, but this may change in the future without notice.
 * It is a best practice to not hardcode the MQTT server URL and instead extract the URL from the Token.
 * This will prevent your application from losing connectivity if the MQTT server changes in the future.

An example of extracting the MQTT server hostname from a token can be found [here](https://github.com/FarmBot-Labs/FarmBot-Python-Examples/blob/master/token_generation_example.py#L22).

Read more about FarmBot API tokens [here](https://github.com/FarmBot/Farmbot-Web-App#q-how-can-i-generate-an-api-token).
