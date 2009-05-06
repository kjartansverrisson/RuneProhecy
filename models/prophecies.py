#!/usr/bin/env python
# encoding: utf-8
"""
prophecies.py

Created by Kjartan Sverrisson on 2009-01-12.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

from google.appengine.ext import db

class God(db.Model):
	filename = db.StringProperty(verbose_name='Filename')

class GodDescription(db.Model):
	description = db.StringProperty(verbose_name='God text')
	image = db.ReferenceProperty(God, verbose_name='God image')

class Prophecy(db.Model):
	day = db.StringProperty(verbose_name='Day')
	rune_title = db.StringProperty(verbose_name='Rune title')
	rune_subtitle = db.StringProperty(verbose_name='Rune sub-title')
	day_of_month = db.StringProperty(verbose_name='Day of the month')
	description = db.TextProperty(verbose_name='Description')
	languageid = db.StringProperty(verbose_name='Language ID')
	god = db.ReferenceProperty(GodDescription, verbose_name='God image')
	
class TempProphecy(db.Model):
	day = db.StringProperty(verbose_name='Day')
	rune_title = db.StringProperty(verbose_name='Rune title')
	rune_subtitle = db.StringProperty(verbose_name='Rune sub-title')
	day_of_month = db.StringProperty(verbose_name='Day of the month')
	description = db.TextProperty(verbose_name='Description')
	languageid = db.StringProperty(verbose_name='Language ID')
	god = db.ReferenceProperty(GodDescription, verbose_name='God image')	

