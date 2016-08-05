#!/usr/bin/env python
from collections import *
d = {100:'string1', 102:'string2', 101:'string3'}
od = OrderedDict(sorted(d.items()))
print(od)
