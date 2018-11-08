#-*- coding:utf-8 -*-
# pip install telesign
from __future__ import print_function
from telesign.messaging import MessagingClient
from telesign.util import random_with_n_digits
import sys

if sys.version[0] == "3": raw_input = input
customer_id = "B6C274DE-E718-42A2-AEAB-F285C94DF0BA"
api_key = "o/391HRcaUNkrrOCpRFm3WVbkbAtSQ5jADGDb6twObPnGrahiuP2VpPXUlk+xAcrx6FdEq7mhd1tR0Cv0zENEg=="

phone_number = "8616605815075"
verify_code = random_with_n_digits(5)

message = "Your code is {}".format(verify_code)
message_type = "OTP"

messaging = MessagingClient(customer_id, api_key)
response = messaging.message(phone_number, message, message_type)

user_entered_verify_code = raw_input("Please enter the verification code you were sent: ")

if verify_code == user_entered_verify_code.strip():
    print("Your code is correct.")
else:
    print("Your code is incorrect.")