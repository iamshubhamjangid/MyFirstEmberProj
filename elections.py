import datetime
from filemgr import filemanager
from datetime import date
from vtrmgr import votermgr
from electionmgr import elmgr
from cdmgr import candidatemgr
today = date.today()
def main():
  fm=filemanager()
  time=datetime.datetime.now()
  print("\n---------Welcome To Online Voting Portal---------\n")
  if time.hour<=18 and time.hour>=10:
    print("You are in the registration Portal\n Registration will be opoen till 18:00\n")
    user = raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\n")
    while user == 'c' or user == 'C' or user == 'v' or user == 'V' or user == 'e' or user == 'E':
          if user == 'V' or user == 'v':
              vtch = raw_input("Add Voter?? [Y/N] \t")
	      while vtch=='y' or vtch=='Y':
    	          name=raw_input("Enter your name here\t")
                  age=int(input("Enter your age here\t"))
                  vid=raw_input("Enter your unique voter id here\t")
                  aadhar=raw_input("Enter your aadhar number here\t")          
                  vtr=votermgr(name,aadhar,vid,age)
                  if vtr.isValid()==True :
	             fm.addvoter(name,vid)
		     fm.displayvoters()
		  vtch = raw_input("Add Voter?? [Y/N] \t")
	      else:
		  user = raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit--->[E]")
    	  elif user=='c' or user=='C':
	      cdch = raw_input("Add Candidate?? [Y/N] \t")
	      while cdch=='y' or cdch=='Y':
    	          name=raw_input("Enter your name here\t")
                  age=int(input("Enter your age here\t"))
                  cid=raw_input("Enter your unique voter id here\t")
                  aadhar=raw_input("Enter your aadhar number here\t")          
                  cdt=candidatemgr(name,aadhar,cid,age)
                  if cdt.isValid()==True :
	              fm.addcandidate(name,cid)
		      fm.displaycandidates()
		  cdch = raw_input("Add Candidate?? [Y/N] \t")
	      else:
		  user = raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\Exit--->[E]n")
	  else:
		elm=elmgr()
		elecdate=elm.electiondate()
		if today==elecdate:
		    print("Now its voting time")
		else:
		    print today
		    print("Ye kya nautanki h!!")
  else:
	print "Voting Registrain has closed"
if __name__ == "__main__":
    main()
