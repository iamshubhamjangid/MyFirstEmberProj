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

    def addon(self,voter):
	votermgr.filecode(voter)

    def delete(self,voter):
	del self.voterdict[voter.v_id]

    def deleteon(self,voterid):
	f = open("vtfile.txt","r")
	lines = f.readlines()
	f.close()
	f = open("vtfile.txt","w")
	for line in lines:
           if voterid in line:
              line = line.replace('.' , '')
	   else:
	      print("Delete nahi ho sakti bhai\n")
	      f.write(line)
	f.close()

    def vtlist(self):
	print self.voterdict
    
    @staticmethod 
    def filecode(voter):
        vfile = open("vtfile.txt", 'a')
        vfile.write(voter.v_id)
        vfile.write(":")
        vfile.write(voter.v_name)
        vfile.write("\n")
        print(vfile)
