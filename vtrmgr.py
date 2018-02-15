from Voter import Voter
class votermgr(Voter):
    voterdict={}
    def isValid(self,object):
	if self.v_age>=18:
	   if votermgr.voterdict.has_key(self.v_id):
	       print "User already exists!!!\n Not allowed to store multiple Same!!"
	   	
	   return True
	
	else:
	    print("You are not satisfying the minimum requirements to vote!!!\n You are under 18!!")
   
    def add(self,object):
	votermgr.voterdict[self.v_id]=self.v_name
	return votermgr.voterdict
    @staticmethod
    def delete(self,object):
	del votermgr.voterdict[vid]
	return votermgr.voterdict
    @staticmethod
    def listvoter():
	print votermgr.voterdict

	    
	
	
