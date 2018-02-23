from Candidate import Candidate
class candidatemgr():
    cddict={}
    def isValid(self,candidate):
	if candidate.c_age>=28:
            if self.cddict.has_key(candidate.c_id):
	       print "User already exists!!!\n Not allowed to store multiple Same!!"
	    return True
	else:
	    print("You are not satisfying the minimum requirements to be a candidtae!!!\n You are under 28!!")
   
    def add(self,candidate):
	self.cddict[candidate.c_id]=candidate.c_name
	
    def delete(self,candidate):
	del cddict[candidate.c_id]

    def lists(self):
	print self.cddict

    
