#!/usr/bin/env python
#-*-coding:utf-8-*-
""" base handler for all other handlers """
import tornado.web
import time
import random
import string
from concurrent.futures import  ThreadPoolExecutor

# printtable == '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# printable[:-32] == '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'
STRINGS = string.printable[0:-32]


class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(20)
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def generate_passwd(self, length=12):
        passwd = ''.join(random.sample(STRINGS, length))
        return passwd

    def save_passwds_to_cookies(self, passwds):
        passwds = '|'.join(passwds[:9])
        self.set_secure_cookie('passwds', passwds)

    def get_passwds_from_cookies(self):
        passwds = self.get_secure_cookie('passwds')
        if passwds:
            return passwds.split('|')
        return []

