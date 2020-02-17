#!/usr/bin/env python3

import re

questions = re.compile(r"\S.+pet\=(?P<pet>\S.+)\&school\=(?P<school>\S.+)\&name\=(?P<mother>\S.+)\&honeymoon\=(?P<honeymoon>\S.+)\sHTTP\S.+")
log = open("/var/log/apache2/access.log", "r")
array = []

for l in log:
    u = questions.findall(l)
    if u:
        print(u)
    else:
        exit
