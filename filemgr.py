from datetime import date
from vtrmgr import votermgr
from cdmgr import candidatemgr	
class filemanager:
    def addvoter(self,name,vid):
	votermgr.addvoter(self,name,vid)
    def deletevoter(self,vid):
	votermgr.deletevoter(self,vid)
    def displayvoters(self):
	votermgr.displayvoter(self)

    def addcandidate(self,name,cid):
	candidatemgr.addcandidate(self,name,cid)
    def deletecandidate(self,cid):
	candidatemgr.deletecandidate(self,cid)
    def displaycandidates(self):
	candidatemgr.displaycandidate(self)
