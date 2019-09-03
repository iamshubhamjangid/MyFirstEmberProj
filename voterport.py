class Voter:
   def __init__(self, v_name, v_id, v_aadhar):
      self.v_name = v_name
      self.v_id = v_id
      self.v_aadhar = v_aadhar
      self.vfile=open("vtfile.txt",'r')
      self.vdict={}
      for line in self.vfile:
        x=line.split(":")
        self.vt_id=x[0]
	self.vt_name=x[1]
	self.vdict[self.vt_id]=self.vt_name
        self.vt_id=self.v_id
      
   def voteradd(self):
         v_age=int(input("Enter voter Age here\t"))
         if v_age>=18:
	    
	    if self.vdict.has_key(self.vt_id):
		print("User already exist!!!! \nNot allowed to vote!!")
	    else:
	       vfile=open("vtfile.txt",'a')
               vfile.write(self.v_id)
	       vfile.write(":")
	       vfile.write(self.v_name)
	       vfile.write("\n")
	       print(vfile)
	 else:
	     print("Not even eligible for vote")
   @staticmethod
   def findvoter():
	  vtr_id=raw_input("enter your Voter id:\t")
	  if vdict.has_key(vtr_id):
		print("great!!")
	  else:
		print("\n..........\n")
       
