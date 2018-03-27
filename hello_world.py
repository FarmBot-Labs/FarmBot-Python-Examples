import json
import paho.mqtt.publish as publish

# Generate this information by using `token_generation_example.py`.
my_device_id = 'device_1'
my_mqtt_host = 'brisk-bear.rmq.cloudamqp.com'
my_token = ''

# Prepare the Celery Script command.
message = {
    'kind': 'send_message',
    'args': {
        'message': 'Hello World!',
        'message_type': 'success'
    }
}

# Send the command to the device.
publish.single(
    'bot/{}/from_clients'.format(my_device_id),
    payload=json.dumps(message),
    hostname=my_mqtt_host,
    auth={
        'username': my_device_id,
        'password': my_token
        }
    )
