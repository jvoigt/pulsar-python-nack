import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

for i in range(10):
    msg = f'hello-pulsar-{i}'
    result = producer.send((msg).encode('utf-8'))
    # result is always None as there is no return in the C Implementation
    print(f'MSG: {msg} --> Result: {result}')

client.close()