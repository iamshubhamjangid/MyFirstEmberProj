from Voter import Voter
class votermgr():
    voterdict={}
    def isValid(self,voter):
	if voter.v_age>=18:
	   if self.voterdict.has_key(voter.v_id):
	       print "User already exists!!!\n Not allowed to store multiple Same!!"
	   return True
	else:
	    print("You are not satisfying the minimum requirements to vote!!!\n You are under 18!!")

    def add(self,voter):
	self.voterdict[voter.v_id]=voter.v_name

    def delete(self,voter):
	del self.voterdict[voter.v_id]

    def vtlist(self):
	print self.voterdict

	    
	
	
