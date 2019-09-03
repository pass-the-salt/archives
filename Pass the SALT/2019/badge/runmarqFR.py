#!/usr/bin/env python3

ERASE_LAST=True

import subprocess
with open("20190602_list1FR.txt") as f:
    l=[[lll.rstrip() for lll in ll.split('#')] for ll in f.readlines()]

for p in range((len(l)+65)//66):
    pl=l[p*66:(p+1)*66]
    with open("badge2marqFR_template.svg") as f:
        t=f.read()
    for on,fn,ln,tn in pl:
        t=t.replace("xxxxxxxx01", fn.strip(), 1)
        t=t.replace("xxxxxxxx02", ln.strip(), 1)
        t=t.replace("xxxxxxxx03", tn.strip(), 1)
        t=t.replace("xxx04", on.strip(), 1)
    if ERASE_LAST:
        t=t.replace("xxxxxxxx01", "")
        t=t.replace("xxxxxxxx02", "")
        t=t.replace("xxxxxxxx03", "")
        t=t.replace("xxx04", "")
    with open("badges2marqFR_%02i.svg" % p,  "w") as f:
        f.write(t)
    subprocess.run(["inkscape", "badges2marqFR_%02i.svg" % p, "--export-plain-svg=badges2marqFR_%02i_flatten.svg" %p, "--export-text-to-path"])
