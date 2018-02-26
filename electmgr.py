import datetime
from datetime import date
from vtrmgr import votermgr
from cdmgr import candidatemgr
from filemgr import filemanager
class electionmgr:
	def registration(self):
		year = int(input('Enter a year\t'))
		month = int(input('Enter a month\t'))
		day = int(input('Enter a day\t'))
		regdate = datetime.date(year, month, day)
		return regdate
	def elecdate(self):
		year = int(input('Enter a year\t'))
		month = int(input('Enter a month\t'))
		day = int(input('Enter a day\t'))
		eldate = datetime.date(year, month, day)
		return eldate
	def rsdate(self):
		year = int(input('Enter a year\t'))
		month = int(input('Enter a month\t'))
		day = int(input('Enter a day\t'))
		rsltdate = datetime.date(year, month, day)
		return rsltdate
	
