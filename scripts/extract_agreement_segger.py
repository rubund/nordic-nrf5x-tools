#!/usr/bin/env python3

import re
import sys



if len(sys.argv) != 2:
    print("Missing argument")
    sys.exit(-1)

m1 = re.compile(r"<textarea[^>]+>(.*?)</textarea>", re.DOTALL)

fp = open(sys.argv[1], "r")

t = fp.read()
fp.close()
matches1 = m1.findall(t)

if len(matches1) > 0:
    agreement_text = matches1[0]
    agreement_text = agreement_text.replace("&copy;", "©")
    agreement_text = agreement_text.replace("&amp;", "&")
    print(agreement_text)



