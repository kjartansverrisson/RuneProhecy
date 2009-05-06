#!/usr/bin/env python
# encoding: utf-8
import logging
import wsgiref.handlers
import os

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import images

from models.prophecies import Prophecy

class appstart(webapp.RequestHandler):
	def get(self):
		locale = self.request.get('lang_id')
		if locale == '':
			locale = 'is'
		strings = getstrings(locale)
		template_values = {
			'strings' : getstrings(locale),
			'locale': locale
		}
		
		path = os.path.join(os.path.dirname(__file__), 'views/start.html')
		self.response.out.write(template.render(path, template_values))

class enternames(webapp.RequestHandler):
	def get(self):
		locale = self.request.get('lang_id')
		if locale == '':
			locale = 'is'
		lines = self.request.get('lines')
		if lines == '2':
			lines = '12'

		if lines == '3':
			lines = '123'

		template_values = {
			'lines': lines,
			'strings' : getstrings(locale),
			'locale': locale
		}
		path = os.path.join(os.path.dirname(__file__), 'views/step1.html')
		self.response.out.write(template.render(path, template_values))	

class prophecy(webapp.RequestHandler):
	def get(self):
		locale = self.request.get('lang_id')
		if locale == '':
			locale = 'is'
		
		lines = self.request.get('lines')
		logging.debug('Number of lines: ' + str(lines))
	
		datearray = list()
		namearray = list()
		#Format is lang-monthday
		for j in range(int(lines)):
			logging.debug('Iteration number: ' + str(j))
			datearray.append(self.request.get('lang_' + str(j))+'-'+self.request.get('mon_' + str(j))+self.request.get('day_' + str(j)))
			namearray.append(self.request.get('name_' + str(j)))

		logging.debug('Checking date array: ')
		logging.debug(datearray)
		logging.info('Fetching ' + str(len(namearray)) + ' documents')

		days = Prophecy.get_by_key_name(datearray)
		dl = list()
		for i in range(len(days)):
			logging.debug('Iteration: ' + str(i))
			logging.debug('Days range: ' + str(len(days)))
			d = {
			'day': days[i].day,
			'rune_title': days[i].rune_title,
			'rune_subtitle': days[i].rune_subtitle,
			'god': days[i].god,
			'day_of_month': days[i].day_of_month,
			'description': days[i].description.replace('\\r\\n','<br/>'),
			'languageid': days[i].languageid,
			'name':namearray[i],
			'calendar_day': int(days[i].day[2:4]),
			'calendar_month': getmonthname(days[i].day[0:2],datearray[i][0:2]),
			'locale': locale
			}
			dl.append(d)
			
		if lines == '2':
			lines = '12'

		if lines == '3':
			lines = '123'
		
		template_values = {
			'lines': lines,
			'days': dl,
			'strings' : getstrings(locale)
		}
		
		path = os.path.join(os.path.dirname(__file__), 'views/step2.html')
		self.response.out.write(template.render(path, template_values))

def main():
	logging.getLogger().setLevel(logging.DEBUG)
	application = webapp.WSGIApplication([
		(r'/', appstart),
		(r'/step/1', enternames),
		(r'/step/2', prophecy),
		], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

def getmonthname(number, locale):
	string = {
		'en': {
			'01': 'January',
			'02': 'February',
			'03': 'March',
			'04': 'April',
			'05': 'May',
			'06': 'June',
			'07': 'July',
			'08': 'August',
			'09': 'September',
			'10': 'October',
			'11': 'November',
			'12': 'December'
		},
		'is': {
			'01': 'janúar',
			'02': 'febrúar',
			'03': 'mars',
			'04': 'apríl',
			'05': 'maí',
			'06': 'júní',
			'07': 'júlí',
			'08': 'ágúst',
			'09': 'september',
			'10': 'október',
			'11': 'nóvember',
			'12': 'desember'
		}
	}
	return string[locale][number]
	
def getstrings(locale):
	strings = {
		'is': {
			'page_one_text': 'Byrjaðu á því að velja fjölda nafna og ýttu svo á <strong>"Áfram"</strong>.',
			'page_one_form_text': '<strong>Fjöldi nafna:</strong>',
			'page_one_button_next': 'Áfram',
			'step1_text': 'Þegar þú hefur slegið inn nafn og afmælisdag, settu þá hak í boxið við endann á línunni til að staðfesta að innslegnar upplýsingar séu réttar.',
			'step1_name': 'Nafn',
			'step1_birthday': 'Afmælisdagur',
			'step1_language': 'Tungumál',
			'step1_confirm': 'Staðf.',
			'step1_button_start_over': 'Byrja aftur',
			'step1_button_next': 'Áfram',
			'step1_month1': 'Janúar',
			'step1_month2': 'Febrúar',
			'step1_month3': 'Mars',
			'step1_month4': 'Apríl',
			'step1_month5': 'Maí',
			'step1_month6': 'Júní',
			'step1_month7': 'Júlí',
			'step1_month8': 'Águst',
			'step1_month9': 'September',
			'step1_month10': 'Október',
			'step1_month11': 'Nóvember',
			'step1_month12': 'Desember',
			'language_en': 'Enska',
			'language_is': 'Íslenska',
			'language_dk': 'Danska',
			'language_de': 'Þýska',    
			'step2_button_print': 'Prenta skjölin mín',
			'step2_button_start_over': 'Byrja aftur',
			'step2_button_page_one': 'Síða eitt',
			'step2_button_page_two': 'Síða tvö',
			'step2_button_page_three': 'Síða þrjú',
			'step2_thank_you_text': 'Verið er að prenta Víkingadagatalið þitt, þú getur skoðað fleiri daga á meðan þú bíður.  Þegar því er lokið getur þú greitt fyrir þau hjá gjaldgera.<br/><br/>Megi guðirnir gefa þér gott veður á meðan dvöld þinni stendur á Íslandi.',  	  	  	
			'step2_thank_you_button_start_over': 'Smelltu hér til að byrja aftur',
		},
		'en':{
			'page_one_text': 'Start by choosing the number of names to want to enter and then click <strong>"Move to next step"</strong>.',
			'page_one_form_text': '<strong>Number of names:</strong>',
			'page_one_button_next': 'Next step',
			'step1_text': 'When you have entered the names and birthdays, please check the box at the end of each line to confirm that you have entered the information correctly.',
			'step1_name': 'Name',
			'step1_birthday': 'Birthday',
			'step1_language': 'Language',
			'step1_confirm': 'Confirm.',
			'step1_button_start_over': 'Start over',
			'step1_button_next': 'Next step',
			'step1_month1': 'January',
			'step1_month2': 'February',
			'step1_month3': 'March',
			'step1_month4': 'April',
			'step1_month5': 'May',
			'step1_month6': 'June',
			'step1_month7': 'July',
			'step1_month8': 'August',
			'step1_month9': 'September',
			'step1_month10': 'October',
			'step1_month11': 'November',
			'step1_month12': 'December',
			'language_en': 'English',
			'language_is': 'Icelandic',
			'language_dk': 'Danish',
			'language_de': 'German',    
			'step2_button_print': 'Order prints',
			'step2_button_start_over': 'Start over',
			'step2_button_page_one': 'Page one',
			'step2_button_page_two': 'Page two',
			'step2_button_page_three': 'Page three',
			'step2_thank_you_text': 'Your Viking Prophecy is being printed but while you wait, feel free to take a look at a few more.  When the printer has finished you can pay at the cashiers.<br/><br/>May the gods give you wonderful weather during your stay in Iceland.',  	  	  	
			'step2_thank_you_button_start_over': 'Click here to start over',
		}
	}
	return strings[locale]
		
if __name__ == "__main__":
    main()