import math

#request for inputs
ballManufactored = int(input("How many bowling balls will be manufactored? "))
ballDiameter = float(input("What is the diameter of each ball in inches? "))
coreVolume = float(input("What is the core volume in inches cubed? "))

# calculate the ball volume
ballRadius = ballDiameter/2
ballVolume = (4/3)*(math.pi)*(ballRadius**3)

#calculate the outside shell volume
ballFillerNeeded = ballVolume-coreVolume
#multiplying the outside shell volume by the balls manufactored
totalFillerNeeded = ballFillerNeeded*ballManufactored

#print statement to user
print("You will need " + str(round(totalFillerNeeded, 4)) + " cubed inches of filler")
