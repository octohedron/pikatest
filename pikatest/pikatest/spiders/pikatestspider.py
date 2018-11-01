#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pika
import logging
import scrapy


class PikaTestSpider(scrapy.Spider):
    """RabbitMQ Test"""
    # Spider name
    name = "pikatestspider"
    # Declare RabbitMQ queue name
    rbmqrk = 'data'
    # Connect with pika to RabbitMQ in localhost
    rmq = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    # Initialize a channel
    rmqc = rmq.channel()
    # Init class

    def __init__(self, *args, **kwargs):
        super(PikaTestSpider, self).__init__(*args, **kwargs)
        # Declare the queue when starting the class
        self.rmqc.queue_declare(queue=self.rbmqrk)

    def start_requests(self):
        # New list for storing the URLS
        for method_frame, properties, body in self.rmqc.consume(self.rbmqrk):
            new_url = body.decode()
            # This does get printed
            logging.info(new_url)
            # Acknowledge the message was received
            self.rmqc.basic_ack(method_frame.delivery_tag)
            # This could happen, but it never gets to the parse method
            yield scrapy.Request(url=new_url, callback=self.parse)

    # This method should get called
    def parse(self, response):
        # It never gets to here
        logging.info("Got response")
        logging.info(response.body)
