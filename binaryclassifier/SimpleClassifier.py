import EmulatorMain


# At the moment this has dumb bugs (scope errors, etc) related to my newness at Python.
# Let's get together and debug them and everyone else's code too!

# Also, much of this is tip-toeing around the fact that I did not have the NumPy package at the time of writing
# I recommend that we all get it here: http://www.scipy.org/scipylib/download.html
# For the actual classifier I would like to use this to implement more precise (i.e. calculus-based) methods.

def slope_list(observations):
    """
    Returns a list of the slopes between the given observation points.
    :param observations: The observations to calculate the slopes between.
    :return: The list of slopes.
    """
    slopeList = []
    for obs in observations:
        (x2, y2) = obs
        slopeList.append(y2)
    return slopeList


# This means to take an average slope of the transient
# by iterating through the list of slopes.
# It will then classify the data as a transient if the discernable slope exceeds a particular margin of error
def classify_simple(observations):
    """
    Checks if the given list of observations indicates a simple transient or not.
    :param observations: The observations to check.
    :return: Whether the observations indicate a transient or not.
    """
    sum = 0
    high = 0
    low = 102  # 100 is max value the test data can generate
    slopeList = slope_list(observations)

    for i in slopeList:
        sum = sum + i

    averageSlope = sum / len(slopeList)
    errorAccountLow = averageSlope - .08
    errorAccountHigh = averageSlope + .08
    for i in slopeList:
        if i > high:
            high = i
        if i < low:
            low = i
        if (i < errorAccountLow) or (i > errorAccountHigh):
            return True
    if (high > errorAccountHigh) or (low < errorAccountLow):
        return True
    else:
        return False
