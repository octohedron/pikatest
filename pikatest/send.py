#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='data')

urls = ["http://example.com",

        "http://reddit.com",

        "http://wikipedia.com",

        "http://google.com",

        "http://facebook.com",

        "http://youtube.com",

        "http://instagram.com",

        "http://computer.com",

        "https://hello.com/en/index.html"]

for u in urls:
    channel.basic_publish(exchange='',
                          routing_key='data',
                          body=u)
    print(" [x] Sent " + u)
connection.close()
