import time
import sys
from voterport import Voter
from candidateport import Candidate
from datetime import date
el_date=date(2018,1,22)
today = date.today()
newvar=0
print("\n")
def main():
  print("\n---------Welcome To Online Voting Portal---------\n")
  user=raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\n")
  while user=='c' or user=='C' or user=='v' or user=='V' or user=='e' or user=='E': 
    if user=='V' or user=='v':
      vtch=raw_input("Add Voter?? [Y/N] \t")
      while vtch=='y' or vtch=='Y':
         v_name=raw_input("Enter Voter Name here:\t")
         v_id=raw_input("Enter Voter Unique Id here:\t")
         v_aadhar=raw_input("Enter Voter Unique Aadhar Id here:\t")
         vt=Voter(v_name,v_id,v_aadhar)
         vt.voteradd(	)
         vtch=raw_input("Add Voter?? [Y/N] \t")
      else:
	 user=  raw_input("Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit---->[E]")
    elif user=='C' or user=='c':
      cdch=raw_input("Add Candidate?? [Y/N] \t")
      while cdch=='y' or cdch=='Y':
         c_name=raw_input("Enter Candidate Name here:\t")
         c_id=raw_input("Enter Candidate Unique Id here:\t")
         c_aadhar=raw_input("Enter Candidate Unique Aadhar Id here:\t")
         cd=Candidate(c_name,c_id,c_aadhar)
         cd.addcndt()
         cdch=raw_input("Add Candidate?? [Y/N] \t")
      else:
	 user=  raw_input("Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit---->[E]")
    elif (user=='E' or 'e'):
	break
  else:
       print "wrong choice"
if __name__== "__main__":
  main()
if today==el_date:
   print("Now you are here to Vote........\n")
   Voter.findvoter()
