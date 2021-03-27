#libraries

imporrt cv2
import numpy 
import imutils # A library I discovered the other day that has helpful methods for working with opencv and numpy.
import argparse # To be used for testing through command line

# A pre-trained model available to us for detectcting humans; built into OpenCV!
model = cv2.HOGDescriptor()
# Will feed support vector machine with this call to the model.
model.setSVMDetector(cv2.HOGDescriptorr_getDefaultPeopleDetector())

# I'm still up in arms on how to implement this correctly, but I DO know we need these three things.

"""
• A way to detect a person in singular frame.
• I want to add personal webcam capability so I'll need a function to process that logic.
• This entire thing will be tested through the command line so the argparse lib will come in handy for checking the values in the dict it returns.
• Some sort of way to track the amount of 'humans' that've been processed. Probably will just be a plain old counter but yeah.
"""
