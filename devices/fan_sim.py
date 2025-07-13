import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic_toggle = "home/fan/toggle"
topic_status = "home/fan/status"

status = False

def on_message(client, userdata, msg):
    global status
    if msg.payload.decode() == "TOGGLE":
        status = not status
        print("Fan:", "ON" if status else "OFF")
        client.publish(topic_status, "ON" if status else "OFF")

client = mqtt.Client()
client.connect(broker, port)
client.subscribe(topic_toggle)
client.on_message = on_message
client.loop_forever()
