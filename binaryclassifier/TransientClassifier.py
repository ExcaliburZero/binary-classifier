from binaryclassifier import EmulatorMain

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
		if random.rantint(0, 10) < 5:
			obsArray= em.generateSingleObject(True)
		else: 
			obsArray = em.generateSingleObject(False)


#Gather many slopes within the time series into an array of slopes.
		i = 0
		slopeList = []
		for x, y in enumerate(obsArray):
			i = i+1

			if i == len(obsArray):
				break

			(x2, y2) = obsArray[i]
			try:
				slopeList.append((float(y2)-y1)/(float(x2)-x1))
			except ZeroDivisionError:
				break
        	# line is vertical

		return slopeList


#This means to take an average slope of the transient
#by iterating through the list of slopes.
#It will then classify the data as a transient if the discernable slope exceeds a particular margin of error 
	def finalClassification(self):

		sum = 0
		slopeList = SlopeList()
		for i in slopeList:
			sum = sum + slopeList[i]


			averageSlope = sum / len(slopeList)


			error = createError()

			if averageSlope > error:
				isTransient = false
			else:
				isTransient = true















