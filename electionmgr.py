from datetime import date
import datetime 
class elmgr:
     def vtregdate(self):
	 date_entry = input('Enter Voter Registration Day Date in YYYY-MM-DD format')
	 year, month, day = map(int, date_entry.split('-'))
	 vtreg = datetime.date(year, month, day)
	 return vtreg
     def cndregdate(self):
	 date_entry = input('Enter Candidate Registation Day Date in YYYY-MM-DD format')
	 year, month, day = map(int, date_entry.split('-'))
	 cdreg = datetime.date(year, month, day)
	 return cdreg
     def electiondate(self):
	 date_entry = input('Enter Election Commencement Date in YYYY-MM-DD format')
	 year, month, day = map(date_entry.split('-'))
	 eldate = datetime.date(year, month, day)
	 return eldate
     def resultdate(self):
	 date_entry = input('Enter Result Declaration Date in YYYY-MM-DD format')
	 year, month, day = map(int, date_entry.split('-'))
	 rdate = datetime.date(year, month, day)
	 return rdate
