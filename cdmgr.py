import psycopg2
from Candidate import Candidate
conn = psycopg2.connect(database="election", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
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
	query="INSERT INTO CANDIDATE VALUES (%s,%s,%s,%s)"
	data=(candidate.c_id,candidate.c_name,candidate.c_age,candidate.c_aadhar)
	cur.execute(query,data);
	conn.commit()
	print "Data successfully added"

    def addon(self,candidate):
	candidatemgr.filecode(candidate)

	
    def delete(self,cd_id):
	query="DELETE from CANDIDATE where ID= %s"
	cur.execute(query,cd_id,);
	conn.commit()

    def lists(self):
	cur.execute("SELECT id, name, age, aadhar  from CANDIDATE")
	rows = cur.fetchall()
	for row in rows:
	   print "CANDIDATE-ID = ", row[0]
   	   print "NAME = ", row[1]
   	   print "Age = ", row[2]
           print "Aadhar Number = ", row[3], "\n"

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

    
