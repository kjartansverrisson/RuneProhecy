#!/usr/bin/env python
# encoding: utf-8
import wsgiref.handlers
import os

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from google.appengine.api import images

from models.prophecies import Prophecy
from models.prophecies import TempProphecy
from models.prophecies import God
from models.prophecies import GodDescription

class get_god_keys(webapp.RequestHandler):
	def get(self):
		logos = GodDescription.all().filter('languageid=', 'is')
		logos.fetch(365)
		for logo in logos:
			self.response.out.write(logo.description + ": " + str(logo.key()) + "<br/>")

class appstart(webapp.RequestHandler):
	def get(self):
		#Gods
		g = God(encoding='utf8', key_name='gfreyr')
		g.filename = 'ed_freyr.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gnjordur')
		g.filename = 'ed_njordur.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gthor')
		g.filename = 'ed_thor.jpg'
		g.put()
		g = God(encoding='utf8', key_name='godinn')
		g.filename = 'ed_odinn.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gtyr')
		g.filename = 'ed_tyr.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gbaldur')
		g.filename = 'ed_baldur.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gheimdallur')
		g.filename = 'ed_heimdallur.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gfreyja')
		g.filename = 'ed_freyja.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gfrigg')
		g.filename = 'ed_frigg.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gloki')
		g.filename = 'ed_loki.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gvidar')
		g.filename = 'ed_vidar.jpg'
		g.put()
		g = God(encoding='utf8', key_name='gullur')
		g.filename = 'ed_ullur.jpg'
		g.put()

		
		g = GodDescription(encoding='utf8', key_name='enfreyr')
		g.description = u'Rune of Freyr'
		g.image = God.get_by_key_name('gfreyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isfreyr')
		g.description = u'Merki Freys'	
		g.image = God.get_by_key_name('gfreyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='defreyr')
		g.description = u'Das Wappen Freyrs'
		g.image = God.get_by_key_name('gfreyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkfreyr')
		g.description = u'Freyrs tegn'
		g.image = God.get_by_key_name('gfreyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='ennjordur')
		g.description = u'Rune of Njordur'
		g.image = God.get_by_key_name('gnjordur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isnjordur')
		g.description = u'Merki Njarðar'	
		g.image = God.get_by_key_name('gnjordur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='denjordur')
		g.description = u'Das Wappen Njörds'	
		g.image = God.get_by_key_name('gnjordur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dknjordur')
		g.description = u'Njords tegn'
		g.image = God.get_by_key_name('gnjordur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enthor')
		g.description = u'Rune of Thor'	
		g.image = God.get_by_key_name('gthor').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isthor')
		g.description = u'Merki Þórs'	
		g.image = God.get_by_key_name('gthor').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dethor')
		g.description = u'Das Wappen Thors'	
		g.image = God.get_by_key_name('gthor').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkthor')
		g.description = u'Thors tegn'
		g.image = God.get_by_key_name('gthor').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enodinn')
		g.description = u'Rune of Odinn'	
		g.image = God.get_by_key_name('godinn').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isodinn')
		g.description = u'Merki Óðins'	
		g.image = God.get_by_key_name('godinn').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkodinn')
		g.description = u'Das Wappen Odins'	
		g.image = God.get_by_key_name('godinn').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='deodinn')
		g.description = u'Odins tegn'
		g.image = God.get_by_key_name('godinn').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='entyr')
		g.description = u'Rune of Tyr'	
		g.image = God.get_by_key_name('gtyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='istyr')
		g.description = u'Merki Týs'	
		g.image = God.get_by_key_name('gtyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='detyr')
		g.description = u'Das Wappen Tyrs'	
		g.image = God.get_by_key_name('gtyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dktyr')
		g.description = u'Tyrs tegn'
		g.image = God.get_by_key_name('gtyr').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enbaldur')
		g.description = u'Rune of Baldur'	
		g.image = God.get_by_key_name('gbaldur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isbaldur')
		g.description = u'Merki Baldurs'	
		g.image = God.get_by_key_name('gbaldur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='debaldur')
		g.description = u'Das Wappen Baldurs'	
		g.image = God.get_by_key_name('gbaldur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkbaldur')
		g.description = u'Balders tegn'
		g.image = God.get_by_key_name('gbaldur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enheimdallur')
		g.description = u'Rune of Heimdallur'	
		g.image = God.get_by_key_name('gheimdallur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isheimdallur')
		g.description = u'Merki Heimdalls'	
		g.image = God.get_by_key_name('gheimdallur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='deheimdallur')
		g.description = u'Das Wappen Heimdalls'
		g.image = God.get_by_key_name('gheimdallur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkheimdallur')
		g.description = u'Heimdals tegn'
		g.image = God.get_by_key_name('gheimdallur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enfreyja')
		g.description = u'Rune of Freyja'	
		g.image = God.get_by_key_name('gfreyja').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isfreyja')
		g.description = u'Merki Freyju'	
		g.image = God.get_by_key_name('gfreyja').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='defreyja')
		g.description = u'Das Wappen Freyjas'	
		g.image = God.get_by_key_name('gfreyja').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkfreyja')
		g.description = u'Freyjas tegn'
		g.image = God.get_by_key_name('gfreyja').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enfrigg')
		g.description = u'Rune of Frigg'	
		g.image = God.get_by_key_name('gfrigg').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isfrigg')
		g.description = u'Merki Friggjar'	
		g.image = God.get_by_key_name('gfrigg').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='defrigg')
		g.description = u'Das Wappen Friggs'	
		g.image = God.get_by_key_name('gfrigg').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkfrigg')
		g.description = u'Friggs tegn'
		g.image = God.get_by_key_name('gfrigg').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enloki')
		g.description = u'Rune of Loki'	
		g.image = God.get_by_key_name('gloki').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isloki')
		g.description = u'Merki Loka'	
		g.image = God.get_by_key_name('gloki').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='deloki')
		g.description = u'Das Wappen Lokis'	
		g.image = God.get_by_key_name('gloki').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkloki')
		g.description = u'Lokes tegn'
		g.image = God.get_by_key_name('gloki').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='envidar')
		g.description = u'Rune of Vidar'	
		g.image = God.get_by_key_name('gvidar').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isvidar')
		g.description = u'Merki Viðars'	
		g.image = God.get_by_key_name('gvidar').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='devidar')
		g.description = u'Das Wappen Vidars'	
		g.image = God.get_by_key_name('gvidar').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkvidar')
		g.description = u'Vidars tegn'
		g.image = God.get_by_key_name('gvidar').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='enullur')
		g.description = u'Rune of Ullur'	
		g.image = God.get_by_key_name('gullur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='isullur')
		g.description = u'Merki Ulls'	
		g.image = God.get_by_key_name('gullur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='deullur')
		g.description = u'Das Wappen Ullurs'	
		g.image = God.get_by_key_name('gullur').key()
		g.put()
		g = GodDescription(encoding='utf8', key_name='dkullur')
		g.description = u'Ulls tegn'
		g.image = God.get_by_key_name('gullur').key()
		g.put()

		#Keyname format is lang-monthday

		self.response.out.write('Skjal vistað')


		

class update_data(webapp.RequestHandler):
	def get(self):
		r = TempProphecy.all().fetch(1000)
		for p in r:
			np = Prophecy(key_name=str(p.languageid) + '-' + str(p.day))
			np.day = p.day 
			np.rune_title = p.rune_title
			np.rune_subtitle = p.rune_subtitle
			np.day_of_month = p.day_of_month
			np.description = p.description
			np.languageid = p.languageid
			np.put()

def main():
    application = webapp.WSGIApplication([
		(r'/get_god_keys', get_god_keys),
		(r'/update_data', update_data),
		(r'.*', appstart)], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()