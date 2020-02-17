#!/usr/bin/env python3

import re

user_pass = re.compile(r"\S.+username\=(?P<user_name>\S.+)\&(?P<password>\S.+)\sHTTP\S.+")
log = open("/var/log/apache2/access.log", "r")
array = []

for l in log:
    u = user_pass.findall(l)
    if u:
        print(u)
    else:
        exit
