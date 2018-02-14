class votermgr:
    voterdict={}
    def __init__(self,name,aadhar,vid,age):
	self.v_name=name
	self.v_age=age
	self.v_id=vid
	self.v_aadhar=aadhar

    def isValid(self):
	if self.v_age>=18:
	   if votermgr.voterdict.has_key(self.v_id):
	       print "User already exists!!!\n Not allowed to store multiple Same!!"
	   	
	   return True
	
	else:
	    print("You are not satisfying the minimum requirements to vote!!!\n You are under 18!!")
    @staticmethod
    def addvoter(self,name,vid):
	votermgr.voterdict[vid]=name
	return votermgr.voterdict
    @staticmethod
    def deletevoter(self,vid):
	del votermgr.voterdict[vid]
	return votermgr.voterdict
    @staticmethod
    def displayvoter(self):
	print votermgr.voterdict

	    
	
	
