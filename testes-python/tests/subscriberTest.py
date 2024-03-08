from pyTdd import subscriber
import json
import time

def test_alert():
    on_message = subscriber.on_message(client=None, userdata=None, msg=json.dumps({"id": f'lj01', "tipo": "freezer", "temperatura": 10, "timestamp": f"{time.strftime('%d/%m/%Y %H:%M:%S')}"}))
    print(on_message)