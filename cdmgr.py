class candidatemgr:
    cddict={}
    def __init__(self,name,aadhar,cid,age):
	self.c_name=name
	self.c_age=age
	self.c_id=cid
	self.c_aadhar=aadhar

    def isValid(self):
	if self.c_age>=28:
            if candidatemgr.cddict.has_key(self.c_id):
	       print "User already exists!!!\n Not allowed to store multiple Same!!"
	    return True
	else:
	    print("You are not satisfying the minimum requirements to be a candidtae!!!\n You are under 28!!")
    @staticmethod
    def addcandidate(self,name,cid):
	candidatemgr.cddict[cid]=name
	return candidatemgr.cddict
    @staticmethod
    def deletecandidate(self,cid):
	del candidatemgr.cddict[cid]
	return candidatemgr.cddict
    @staticmethod
    def displaycandidate(self):
	print candidatemgr.cddict

    
