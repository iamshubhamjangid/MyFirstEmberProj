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

    def addon(self,candidate):
	candidatemgr.filecode(candidate)

	
    def delete(self,candidate):
	del cddict[candidate.c_id]

    def lists(self):
	print self.cddict

    def deleteon(self,cdid):
	f = open("cdfile.txt","r")
	lines = f.readlines()
	f.close()
	f = open("cdfile.txt","w")
	for line in lines:
           if cdid in line:
              line = line.replace('.' , '')
	   else:
	      print("Delete nahi ho sakti bhai\n")
	      f.write(line)
	f.close()


    @staticmethod 
    def filecode(candidate):
        cfile = open("cdfile.txt", 'a')
        cfile.write(candidate.c_id)
        cfile.write(":")
        cfile.write(candidate.c_name)
        cfile.write("\n")
        print(cfile)

    
