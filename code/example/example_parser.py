#!/usr/bin/env python3

import re

example = re.compile(r"\S.+openid_identifier\=(?P<openid>\S.+)\&name\=(?P<name>\S.+)\&pass\=(?P<pass>\S.+)\sHTTP\S.+")
log = open("/var/log/apache2/access.log", "r")
array = []

for l in log:
    u = example.findall(l)
    if u:
        print(u)
    else:
        exit
