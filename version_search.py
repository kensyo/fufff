# -*- coding: UTF-8 -*-
import re
from html.parser import HTMLParser

class fpVersionHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.os_version = {}
        self.is_td = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.is_td = True
        else:
            self.is_td = False

    def handle_endtag(self, tag):
        self.is_td = False

    def handle_data(self, data):
        if self.is_td:
            if data == "Linux" and self.os_version == {}:
                self.os_version["Linux"] = None
            elif re.match('(^11(\d|\.)*$)', data) and self.os_version == {"Linux" : None}:
                self.os_version["Linux"] = data

    def latest_version(self):
        return self.os_version
