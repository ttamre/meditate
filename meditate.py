#!/usr/bin/env python3

import logging
import json

from twilio.rest import Client

"""
Send text message to a list of numbers

client  - twilio client that will send the message
client_number - number to send text from
message - body of the text message
"""
def send_mass_texts(client:Client, client_number:str, message:str, number_file:str = "numbers.txt"):
    with open(number_file) as f:
        numbers = f.readlines()

    logging.info("--------------------")
    logging.info(f"{client} sending mass texts to {len(numbers)} phone numbers")
    logging.info("--------------------")

    for number in numbers:
        send_message(client, client_number, number, message)

"""
Send text message to a phone number

client  - twilio client that will send the message
number  - phone number to send the message to
client_number - number to send text from
message - body of the text message
"""
def send_message(client:Client, client_number:str, number:str, message:str):
    message = client.messages.create(
        body=message,
        from_=client_number,
        to=number
    )

    logging.info(f"{client} sent SMS {message} to {number}")

if __name__ == "__main__":
    with open("secrets.json") as f:
        data = json.load(f)
        account_sid = data["account_sid"]
        auth_token = data["auth_token"]
        client_number = data["client_number"]

    client = Client(account_sid, auth_token)
    message = "Don't forget to meditate today!"
    send_mass_texts(client, client_number, message)
