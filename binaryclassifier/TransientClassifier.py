from binaryclassifier import EmulatorMain
import random #ADDED TO USE RANDINT()~~~~~~~~~~

class Classifier (object): 

#At the moment this has dumb bugs (scope errors, etc) related to my newness at Python. 
#Let's get together and debug them and everyone else's code too!

#Also, much of this is tip-toeing around the fact that I did not have the NumPy package at the time of writing
#I recommend that we all get it here: http://www.scipy.org/scipylib/download.html
#For the actual classifier I would like to use this to implement more precise (i.e. calculus-based) methods.
    def SlopeList(self):

#Generate data using CVC's data generator. For this prototype, randomly pass in a value of true or false
        em = EmulatorMain.EmulatorMain()

#generate an array of observations
        obsArray = [] #ADDED FOR CLARIY~~~~~~
        if random.randint(0, 10) < 5: #SPELLING ERROR~~~~
	       obsArray= em.generateSingleObject(True)
        else: 
	       obsArray = em.generateSingleObject(False)

#Gather many slopes within the time series into an array of slopes.
        slopeList = []
        
        #for x, y in enumerate(obsArray):
        (x2, y2) = obsArray[0]
        for obs in obsArray[1:]:
            x1 = x2
            y1 = y2
            (x2, y2) = obs
            try: #!!!!!!!!!!!!!LINE BELOW IS THE ONLY LINE THAT WILL STILL GENERATE AN ERROR, DONT KNOW WHAT ITS SUPPOSED TO DO~~~~
                slopeList.append((float(y2)-y1)/(float(x2)-x1)) #X1 AND Y1 AREN'T DEFINED? DON'T KNOW WHAT THEY ARE THERE FOR~~~~
            except ZeroDivisionError:
                break
        	# line is vertical
        return slopeList

#This means to take an average slope of the transient
#by iterating through the list of slopes.
#It will then classify the data as a transient if the discernable slope exceeds a particular margin of error 
    def finalClassification(self):
        sum = 0
        slopeList = self.SlopeList() #FIXED UNDEFINED NAME~~~~~
        
        for i in slopeList:
            sum = sum + i
            averageSlope = sum / len(slopeList)
            error = EmulatorMain.createError() #FIEXED UNDEFINED NAME~~~~~~~
            if abs(averageSlope) > error:
                isTransient = False #FIXED false TO False~~~~~
            else:
                isTransient = True #SAME PROBLEM AS ABOVE~~~~~~
        return isTransient #ADDED RETURN STATEMENT~~~~~~~
        
                         
cC = Classifier()
cC.SlopeList()
