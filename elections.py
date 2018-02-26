import datetime
from Voter import Voter
from datetime import date
from vtrmgr import votermgr
from electmgr import electionmgr
from cdmgr import candidatemgr
from Candidate import Candidate
from filemgr import filemanager
today = date.today()
def main():
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
		  voter=Voter(vid,aadhar,name,age)          
                  fm=filemanager()
                  vtr=votermgr()
                  if vtr.isValid(voter)==True :
	             opt=raw_input("\n--------------\nChoose one the options\nAdd Voter---->(A)\nDelete Voter---->(D)\n")
		     filemanager.Voteroptions[opt](voter) 
		     vtr.addon(voter)
		  choice=raw_input("Want to delete the voter??\t")
		  if (choice=='y' or 'Y'):
			vtr_id=raw_input("Enter the voter id which you want to delete \t")
			vtr.deleteon(vtr_id)	
		  else:
			pass 
		  vtch = raw_input("Add Voter?? [Y/N] \t")
	      else:
		  opt=raw_input("\n-------------\nChoose one the options\nDisplay Voter---->(V)\n")
		  filemanager.listing[opt]()
		  user = raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit--->[E]")
    	  elif user=='c' or user=='C':
	      cdch = raw_input("Add Candidate?? [Y/N] \t")
	      while cdch=='y' or cdch=='Y':
    	          name=raw_input("Enter your name here\t")
                  age=int(input("Enter your age here\t"))
                  cid=raw_input("Enter your unique voter id here\t")
                  aadhar=raw_input("Enter your aadhar number here\t")
		  candidate=Candidate(cid,aadhar,name,age)          
                  fm=filemanager()   
                  CdMgr=candidatemgr()
                  if CdMgr.isValid(candidate)==True :
		     opt=raw_input("Choose one the options\nAdd Candidate---->(A)\n Delete Candidate---->(D)\n")
		     filemanager.Candidateoptions[opt](candidate)
		     CdMgr.addon(candidate)
		  cdch = raw_input("Add Candidate?? [Y/N] \t")
	      else:
		  opt=raw_input("Choose one the options\nDisplay Candidate---->(C)\n")
		  filemanager.listing[opt]()
		  user = raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\Exit--->[E]n")
	  else:
		print("\n------------------------------\nNow Election Manger will Commence the Election Date here\n-----------------------\n")
		elm=electionmgr()
		electiondate=elm.elecdate()
		if today==electiondate:
		    print("Now its voting time")
		    while (time.hour<=17 and time.hour>=10):
			vtr_id=raw_input("Enter your unique voter Id\t")
			if votermgr.voterdict.has_key(vtr_id):
				print("Now you have the following list of candidates for Voting\n Be careful while Voting as once you done with voting cannot be redone!!")
				cdm=candidatemgr()
				cdict=candidatemgr.cddict
				for cndt in cdict:	
					print cndt
					print ""

			else:
				print("you are not registerd for voting!!!")			

		else:
		    print today
  else:
	print "Voting Registrain has closed"
if __name__ == "__main__":
    main()
