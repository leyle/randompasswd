#!/usr/bin/env python
#-*-coding:utf-8-*-
import re
from base import BaseHandler
from tornado.concurrent import run_on_executor

class IndexHandler(BaseHandler):
    @run_on_executor()
    def get(self):
        passwd_len = self.get_argument('l', '12')
        if not re.match('^\d+$', passwd_len):
            passwd_len = 12
        passwd_len = int(passwd_len)
        if passwd_len > 20:
            passwd_len = 20

        random_passwd = self.generate_passwd(passwd_len)
        passwds = self.get_passwds_from_cookies()
        passwds.insert(0, random_passwd)
        print passwds
        self.save_passwds_to_cookies(passwds)

        self.render('index.html', cur_passwd=random_passwd, history=passwds)

