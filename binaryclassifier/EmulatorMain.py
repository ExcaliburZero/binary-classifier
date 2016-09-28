# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 19:26:17 2016
@author: critter
From https://www.noao.edu/meetings/eventful-universe/Thursday0318/morning/CRTS_TucsonMar10.pdf :
Discovery rate ~ 1 transient per 10^6 sources detected per epoch So, transient discovery seems very rare. 

Each object contains a semi-random number of observations (2-10). Observations come in tuples of (time (seconds), light (no idea)). 
Objects are arrays of these tuples where the first index is the first observation taken.
"""

from collections import namedtuple
import random

class EmulatorMain(object):
    
    def generateSingleObject(self, isTransient): #pass True to generate a transient
        """
        Method to be called by the event broker or emulator when it wants
        a single object's observational data. Returns an array of namedtuple.
        if you wanted to emulate a real time event stream, it should return a
        single namedtuple every x seconds instead of a whole array at once
        """
        totalObservations = random.randint(2, 10) #2 to 10 observations per object
        x = 0
        initialBrightness = random.randint(1, 100) #arbitrary value for the brightness observed
        isSlopePositive = random.choice([True, False])
        hasSlopeChanged = False
        if isTransient == True:
            variance = random.randint(1, (initialBrightness/4) + 1)
        timeTaken = 0 # pretend in seconds
        timeInterval = random.randint(3600, 28800)
        #observations may take place between 1 and 8 hours but remain constant for the object
        finalObject = []
        for x in range(0, totalObservations + 1):
            point = namedtuple('Observation' + str(x), ['time', 'light'])
            if isTransient == False:
                timeTaken = timeTaken + timeInterval
                p = point(timeTaken, (initialBrightness + createError()))
                finalObject.append(p)
                continue
            if hasSlopeChanged == False:
                j = random.randint(1, 20) # 1 in 20 chance of slope changing
                if j == 1:
                    hasSlopeChanged = True
                    isSlopePositive = not isSlopePositive
            if isSlopePositive == True:
                initialBrightness = initialBrightness + variance
            else:
                initialBrightness = initialBrightness - variance
            timeTaken = timeTaken + timeInterval;
            p = point(timeTaken, (initialBrightness + createError()))            
            finalObject.append(p)
            
        return finalObject

    def generateManyObjects(obsCount): 
        """
        Method to be called by the event broker when it wants to parse through many objects. obsCount determines 
        how many objects are created. Pass None in if you want a random amount of objects between 2 and 10
        Returns ? Do we even need this?
        """
      
def createError():
    # Error between -5%-5% of value passsed in (random)
    observationalError = random.randint(-5, 5)
    observationalError = observationalError * .01
    return observationalError

"""#CODE TO PRINT OUT OBSERVATIONS OF A SINGLE OBJECT
a = EmulatorMain()
h = a.generateSingleObject(True)
for a in h:
    print a
"""
