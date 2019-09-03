## Summary

Based on the Pass the SALT 2019 conference logo.

I'm sharing it mostly for its design process in case other people want to create their own conference badges.

The badges were made by the Polytech'Lille [Fabricarium](http://fabricarium.polytech-lille.fr/).

Compared to [previous year badges](https://www.thingiverse.com/thing:2968762), the following changes were made:

* New logo
* Poplar plywood instead of MDF
* Two more fields: affiliation/twitter/nickname and serial (to sort easily badges based on entrance ticket serials)
* Replace raster etching by vector etching (faster)
* Two holes for two-end lanyards (to avoid badges to turn over)
* Tokens directly attached to the badge (previous year people tend to lose the 3D-printed [tokena](https://www.thingiverse.com/thing:2988836)
* Outer cut in green so badges are detached last (avoid spurious moves during inner holes cutting)
* Optional language flag (most attendees are French-speaking and we'd like them to have the courtesy to switch to English in presence of non-French-speaking people)
* Common template text, much easier to work with, no more manual step after tile cloning

## Print settings

Printer: Trotec Speedy 400

Notes: The badges were engraved and cut with a Trotec Speedy 400 with a 60W Iradion 156F CO2 laser on 1000x600 3mm poplar plywood panels.

## How I designed this

### List of attendees

We'll consider a list in a simple text file.
One single line per attendee, four fields separated by a "#" => three lines on the final badges plus one line with the serial on one of the side tokens, fields can be empty, e.g.:
```
FPDXT#Thib0t##⠠⠵ ⠈⠞ ⠢⠇ ⠨⠖
Z8ZWF#Philippe#Teuwen#@doegox
```
Yeah some people are challenging the system ;)

Of course, if # is used in some badge names, choose another separator.

The file is alphabetically sorted, i.e. sorted by ticket order serial numbers.

From this list, a few information items are important:
* What are the longest fields? (take the font into account, MMM is larger than III, XXX is larger than Xxx)
* What are the symbols in use? (this is important to see if the font looks ok for all symbols)

```
cat attendees.txt |\
    tr -d "a-zA-Z# 0-9"|\
    sed 's/\(.\)/\1\n/g'|\
    sort|uniq|tr -d '\n'
!'-./;=@_⠇⠈⠖⠞⠠⠢⠨⠵ćçéëîïôúü
```

Some manual corrections:
* Uniform capitalisation: Name, not name or NAME
* Swap First name/Last name for those who mixed them up
* Shorten some affiliations to fit the badges. When only two field were used the affiliation can also be broken in two lines


### Design

Prepare a SVG with Inkscape.

Typical setup with vector engraving is:
- draw blue paths to be vector engraved (width of 0.05mm)
- draw red paths to be cut (width of 0.05mm)
- draw green paths to be cut lastly, i.e. the outside cut (width of 0.05mm)

### Image block

badge2marqFR_example.png

Use the longest attendee fields and preview all the symbols in use. Here is an example, with some paths much larger than 0.05mm just to ease the initial preview.

### Paths, paths, paths

Remove the test attendee name for now. In the template I'm using the following dummy values:

* xxxxxxxx01
* xxxxxxxx02
* xxxxxxxx03
* xxx04

Initial logo was made of a stroke with a width, but the engraving laser takes only paths, so strokes must be converted.
* Select all strokes
* Path > Stroke to path
* Path > Union

Text must be also converted to path, but at this point only the text common to all badges gets converted.
* Select text
* Path > Object to path

As we're using vector engraving, all objects must get a visible stroke and no fill.

If symmetry was used to design the logo, it must be converted before tiling.
* Select all objects except the template text
* Path > Object to path

Then group all, including text and cuts, and make tiles out of it.
* Edit > Clone > Create tiled clones
  * Shift X 5% per column  (the % is for some uniform spreading, to be adjusted depending on design size & placement)
  * Shift Y 5% per row
  * rows * columns: 6*11 (see how to fill at best the wood panel size you'll use)
* Delete first "clone" duplicated on top of original element
* Select all; Edit / Clone / Unlink clones
* File / Document properties / resize page to drawing / resize to 1000x600 and center objects

### Image block

badge2marqUK_template_example.png 

Our template, "UK flag" version. At this point, attendee text is not yet turned into a path.

### Mailing

Time to use our attendees list with our template.

```python
#!/usr/bin/env python3

ERASE_LAST=True

import subprocess
with open("attendees.txt") as f:
    l=[[lll.rstrip() for lll in ll.split('#')] for ll in f.readlines()]

for p in range((len(l)+65)//66):
    pl=l[p*66:(p+1)*66]
    with open("template.svg") as f:
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
    with open("badges_%02i.svg" % p,  "w") as f:
        f.write(t)
    subprocess.run(["inkscape", "badges_%02i.svg" % p,
        "--export-plain-svg=badges_%02i_flatten.svg" %p,
        "--export-text-to-path"])
```

The last line automates the final conversion of the attendee text to path.
The produced SVG files can now be "printed" directly on the laser cutter.

### Resources

* http://www.cutlasercut.com/resources/drawing-guidelines/styles-examples
* https://edutechwiki.unige.ch/fr/Trotec_Speedy_100R
* http://carrefour-numerique.cite-sciences.fr/fablab/wiki/doku.php?id=trucs_astuces:tests_de_marquage
* http://fabricarium.polytech-lille.fr/#!/machines/1
* https://www.thingiverse.com/thing:3671472
