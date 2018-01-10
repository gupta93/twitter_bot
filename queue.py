import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1',backpressure_detection=True))
channel = connection.channel()
channel.queue_declare(queue='twitter')