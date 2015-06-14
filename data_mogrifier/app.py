#!/usr/bin/env python3
from lib.dbFetch import dbFetch

d = dbFetch()

d.mergePrisoners()
d.comparePrisoners()