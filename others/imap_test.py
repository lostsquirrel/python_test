# -*- coding: utf-8 -*-
import email
import logging
import unittest

from imapclient import IMAPClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # ssl_context = ssl.create_default_context()

        # don't check if certificate hostname doesn't match target hostname
        # ssl_context.check_hostname = False

        # don't check if the certificate is trusted by a certificate authority
        # ssl_context.verify_mode = ssl.CERT_NONE
        logging.debug("start server opened")
        with IMAPClient(HOST, port=143, ssl=False) as server:
            logging.debug("server opened")
            server.login(USERNAME, PASSWORD)
            server.select_folder("INBOX", readonly=True)
            messages = server.search("")

            for uid, message_data in server.fetch(messages, "RFC822").items():
                email_message = email.message_from_bytes(message_data[b"RFC822"])
                print(uid, email_message.get("From"), email_message.get("Subject"))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
