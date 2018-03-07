from telegram.ext import CommandHandler
from telegram.ext import Updater
import datetime
import calendar
from math import *
import sys

updater = Updater(token=sys.argv[1])
dispatcher = updater.dispatcher

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Hey! Ich bin Janine's cooler Bot und du? Antworte nicht, ich kann noch nicht reagieren :) Aber du kannst mich fragen, wann der nächste Spieleabend ist (/spieleabend) :)")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

def spieleabend(bot, update):
	print(update.message.chat_id)
	bot.send_message(chat_id=update.message.chat_id, text="Jeden zweiten Freitag ist Spieleabend! Der nächste ist am {0}! Los geht's, wie immer, um 20 Uhr!".format(nextspieleabend().strftime('%d %b %Y')))

spieleabend_handler = CommandHandler('spieleabend', spieleabend)
dispatcher.add_handler(spieleabend_handler)
updater.start_polling()


def nextfriday(today):
	weekday = today.weekday()
	nextfriday = datetime.date.today()
	if weekday == 1:
	    nextfriday = today + datetime.timedelta(days=3)
	elif weekday == 2:
	    nextfriday = today + datetime.timedelta(days=2)
	elif weekday == 3:
	    nextfriday = today + datetime.timedelta(days=1)
	elif weekday == 4:
	    nextfriday = today
	elif weekday == 5:
	    nextfriday = today + datetime.timedelta(days=6)
	elif weekday == 6:
	    nextfriday = today + datetime.timedelta(days=5)
	else:
	    nextfriday = today + datetime.timedelta(days=4)

	return nextfriday

def nextspieleabend():
	today = datetime.date.today()
	date = today.isocalendar()

	if date[1] % 2 == 1:
		#Woche ungerade
		#Wochentag Mo bis Fr -> dieser Freitag Spieleabend
		if date[2] == 1 or date[2] == 2 or date[2] == 3 or date[2] == 4 or date[2] == 5:
			nextspieleabend = nextfriday(today)
		else: 
			nextspieleabend = nextfriday(today) + datetime.timedelta(days=7)
			

	else: 
		#Woche gerade
		if date[2] == 6 or date[2] == 7:
			nextspieleabend = nextfriday(today)
		else: 
			nextspieleabend = nextfriday(today) + datetime.timedelta(days=7)
	
	return nextspieleabend

def erinnerung(bot, _):
	#today = datetime.date.today()
	#today = datetime.fromtimestamp(1521120934)
	#if today == nextspieleabend - datetime.timedelta(days=1):
	bot.send_message(chat_id=15849814, text="Morgen ist Spieleabend! 20 Uhr gehts los!".format(nextspieleabend().strftime('%d %b %Y')))
	

updater.job_queue.run_repeating(erinnerung, interval=1800, first=0)	

