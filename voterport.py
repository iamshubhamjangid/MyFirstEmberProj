class Voter: 
   def __init__(self, v_name, v_id, v_aadhar):
      self.v_name = v_name
      self.v_id = v_id
      self.v_aadhar = v_aadhar
      Voter.vCount += 1
      global vt_id,vt_name
      vt_id=v_id
      vt_name=v_name
      vdict={v_name:v_id}
   def displayVoter(self):
      print(vdict)
   def voteradd(self):
         v_age=int(input("Enter voter Age here\t"))
         if v_age>=18:	
   	    vdict={vt_name:vt_id} 
	    if vdict.has_key(vt_id):
		print("user already exist!!""\n" "Not allowed to vote!!")
	    else :
		vfile=open("vtfile",'a')
                vfile.write(str(vdict))
	        print(vfile)
	 else:
	     print("Not even eligible for vote")

