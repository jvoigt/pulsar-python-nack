import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic',
                            subscription_name='my-sub')

while True:
    msg = consumer.receive()
    data = msg.data().decode(encoding="utf-8")
    msg_id = msg.message_id()

    print(f"Received message: {msg}")
    counter = int(data.split("-")[2])
    
    if (counter % 2):
        print(f"{counter} is even")
        consumer.acknowledge(msg)
    else:
        print(f"{counter} is odd")
        consumer.negative_acknowledge(msg)

client.close()