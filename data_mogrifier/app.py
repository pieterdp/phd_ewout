#!/usr/bin/env python3
from lib.mergeOriginal import MergeOriginal

db = MergeOriginal()
db.merge()
db.mk_big_match()
db.match_check()
