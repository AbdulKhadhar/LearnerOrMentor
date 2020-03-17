class Tech:

   menCount = 0
   lerCount = 0
   entCount = 0

   def __init__(self, name, Exp):
      self.name = name
      self.Exp = Exp
      self.status = status
      self.avl = avl
      Tech.entCount += 1
   
   def addStacks(self):
       print ("Enter your name")
       ent1=input(self.name)
       print ("Enter your experience")
       ent2=input(self.Exp)
       
   def SetMentorOrLearner(self):
       print ("Enter One Option \n 1. Mentor \n 2. Learner")
       status = input(self.status)
       if status == "Mentor" :
           self.status= "Mentor"
           Tech.menCount += 1
       elif status == "Learner" :
           self.status= "Learner"
           Tech.lerCount += 1
       else :
            print ("Enter correct choice as 1 or 2")
   def SetAvailableTime(self) :
        if status == "Mentor" :
            print ("Enter Available Time :")
            avl =input(self.avl)
            self.avl=avl
    
   def totalCount(self):
     print ("Total Mentors %d" % Tech.menCount)
     print ("Total Lerners %d" % Tech.lerCount)
     print ("Total  %d" % Tech.entCount)

   def getMentor(self):
      
        print ("Enter experience of your mentor")
        a=input()
        if a >= self.Exp :
          print ("Name : ", self.name,  ", Experience: ", self.Exp,"Time Available", self.avl)
        else :
          print ("No Mentor with your requirements")
          
