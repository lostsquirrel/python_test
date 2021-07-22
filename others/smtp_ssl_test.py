# -*- coding: utf-8 -*-
import smtplib
import ssl

port = 465  # For SSL
smtp_server = ""
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address
password = ""
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server) as server:
    server.login(sender_email, password)
    print("xxx")
    server.sendmail(sender_email, receiver_email, message)
