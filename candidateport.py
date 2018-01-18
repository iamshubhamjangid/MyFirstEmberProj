class Candidate:
   cCount = 0
   def __init__(self, c_name, c_id, c_aadhar):
      self.c_name = c_name
      self.c_id = c_id
      self.c_aadhar = c_aadhar
      Candidate.cCount += 1
      global cd_id,cd_name
      cd_id=c_id
      cd_name=c_name
      cdict={c_name:c_id}
   def displayCount(self):
     print "Total Candidates are: %d" % Candidate.cCount

   def displayCandidate(self):
      print "Name : ", self.c_name,  ", Voter Id ", self.c_id,  ", Aadhar Id: ", self.c_aadhar
   def cdadd(self):
         c_age=int(input("Enter candidate Age here\t"))
         if c_age>=28:	
   	    cdict={cd_name:cd_id} 
	    if cdict.has_key(cd_id):
		print("user already exist!!""\n" "Not allowed to vote!!")
	    else :
		vfile=open("cdfile",'a')
                vfile.write(str(cdict))
	        print(vfile)
	 else:
	     print("Not even eligible for vote")
