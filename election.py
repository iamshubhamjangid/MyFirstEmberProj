import time
from datetime import date
el_date=date(2018,1,17)
today = date.today()
print("\n---------Welcome To Online Voting Portal---------\n")
elcom="Shubham Jangid"
print("Election Commisioner is: Mr. "+elcom)
print("\n")
voter={}
candidate={}
namo=0
raga=0
print("You have to foolow the order as \n you have to select first voter and then candidate because if you choose first candidate then you wont be able to get to the voters portal")
user=  raw_input("Who are you?? Choose one of these:\nCandidate[C]\nVoter[V]\n")
while(user=='c' or 'C' or 'v' or 'V'): 
  if user=='V' or user=='v':
    print("\n------------------You are in voter portal-----------------\n")
    choice = raw_input("Enter the choice as Do you want to vote? Y/N")
    while choice == 'y' or choice == 'Y': 
	print("Enter the voter details \n")
	v_age=int(input("Enter Your age:\t"))
	if v_age>=18:
  	   v_id=raw_input("Enter the Unique voter id\t")
  	   voter_id=v_id  
  	   v_aadhar=raw_input("Enter the Unique Aadhar id\t")
  	   if voter.has_key(voter_id):
     	      print("User Already Exist!!!!\n NOT ALLOWED TO VOTE!!")
  	   else:
     	      voter[voter_id]=v_aadhar
     	      with open('voters.txt', 'w') as file:
                 file.write(str(voter))
     	         print(file)
	   choice = raw_input("Enter the choice as Do you want to vote? Y/N")
	else:
     	   print("You are not Eligible to vote!!!")
           choice = raw_input("Enter the choice as Do you want to vote? Y/N") 
    else:
     print("Voting Portal is closed now.....\n")	  
     print("\n")
     user=  raw_input("Who are you?? Choose one of these:\nCandidate[C]\nVoter[V]\n") 
  elif user=='C' or user=='c':
     print("\n------------------You are in candidate portal-----------------\n")
     choice = raw_input("Enter the choice as Do you want to be a candidate? Y/N")
     while choice == 'y' or choice == 'Y':    
	print("Enter the candidate details \n")
	c_age=int(input("Enter Your age:\t"))
	if c_age>=25:
  	   c_id=raw_input("Enter the Unique Candidate voter id\t")
  	   cd_id=c_id  
  	   c_aadhar=raw_input("Enter the Unique Candidate Aadhar id\t")
	   c_name=raw_input("Enter your name\t")
  	   if candidate.has_key(cd_id):
     	      print("Candidate Already Exist!!!!\n NOT ALLOWED TO Add same Candidate again!!!")
  	   else:
     	      candidate[cd_id]=c_name
     	      with open('candidates.txt', 'w') as file:
                 file.write(str(candidate))
	   choice = raw_input("Enter the choice as Do you want to be a candidate? Y/N")
	else:
     	   print("You are not Eligible to be a candidate!!!")
           choice = raw_input("Enter the choice as Do you want to be a candidate? Y/N") 
     else:
        print("exit of the candidate portal\n")	  
        print("\n")
        user=  raw_input("Who are you?? Choose one of these:\n1)Candidate[C]\n2)Voter[V]\n")
  else:
     break
else:
     print("Exit.....!!!\n invalid choice")
if(today==el_date):
   print("Its time for voting")
   print("Now you have the following candidates for voting:-\n")
   for cd in candidate:
	  print(candidate[cd])
	  print("")
   voterid=raw_input("Enter voter's unique id\t")
   if voter.has_key[voterid]:
      print("choose the options to vote:-\n 1)%s \n 2) %s\n",candidate[0],candiadte[1])
   else:
      print("you are not authorised to vote!!")
else:
     print("this is not the voting day!!!\n please do check the date!!!")
	
