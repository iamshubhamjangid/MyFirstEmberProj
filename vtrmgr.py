import psycopg2
from Voter import Voter
conn = psycopg2.connect(database="election", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
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
	query="INSERT INTO VOTERS VALUES (%s,%s,%s,%s)"
	data=(voter.v_id,voter.v_name,voter.v_age,voter.v_aadhar)
	cur.execute(query,data);
	conn.commit()
	print "Data successfully added"

    def addon(self,voter):
	votermgr.filecode(voter)

    def delete(self,voter_id):
	query="DELETE from VOTERS where ID= %s"
	data=(voter_id)
	cur.execute(query,data);

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
	cur.execute("SELECT id, name, age, aadhar  from VOTERS")
	rows = cur.fetchall()
	for row in rows:
	   print "Voter-ID = ", row[0]
   	   print "NAME = ", row[1]
   	   print "Age = ", row[2]
           print "Aadhar Number = ", row[3], "\n"

    
    @staticmethod 
    def filecode(voter):
        vfile = open("vtfile.txt", 'a')
        vfile.write(voter.v_id)
        vfile.write(":")
        vfile.write(voter.v_name)
        vfile.write("\n")
        print(vfile)
