from datetime import date
from vtrmgr import votermgr
from cdmgr import candidatemgr	
vtrs = votermgr()
cdts = candidatemgr()
class filemanager:

   def AddVoters(voter):
	vtrs.add(voter)

   def AddCandidate(candidate):
      	cdts.add(candidate)
  
   def DeleteVoter(voter):
	vtrs.delete(voter)

   def DeleteCandidate(candidate):
	cdts.delete(candidate)
   
   def ListVoters():
	vtrs.vtlist()

   def ListCandidates():
	cdts.lists()

   Voteroptions={
	'A':AddVoters,
	'D':DeleteVoter,
	'a':AddVoters,
	'd':DeleteVoter		
	  }
   Candidateoptions={
	'A':AddCandidate,
	'D':DeleteCandidate,
	'a':AddCandidate,
	'd':DeleteCandidate
	  }
   listing={
	'V':ListVoters,
	'C':ListCandidates,
	'v':ListVoters,
	'c':ListCandidates	
	   }
