#librarie
import cv2
import numpy 
import imutils # A library I discovered the other day that has helpful methods for working with opencv and numpy.
import argparse # To be used for testing through command line

# A pre-trained model available to us for detectcting humans; built into OpenCV!
model = cv2.HOGDescriptor()
# Will feed support vector machine with this call to the model.
model.setSVMDetector(cv2.HOGDescriptorr_getDefaultPeopleDetector())

# I'm still up in arms on how to implement this correctly, but I DO know we need a few things.

"""
• A way to detect a person in singular frame.
• I want to add personal webcam capability so I'll need a function to process that logic.
• This entire thing will be tested through the command line so the argparse lib will come in handy for checking the values in the dict it returns.
• Some sort of way to track the amount of 'humans' that've been processed. Probably will just be a plain old counter but yeah.
"""
# This methods goal is to return the frame with a box around the rendered human.
def render_human(frame):
      box,weights = model.detectMultiScale(frame,winStride=(4,4), padding=(8,8),scale=1.03)
      human_count = 1
      # detectMultiScale() returns 2-tuple so we'll have to iterate through the data containing the coordinates of the box
      for x,y,w,h in box:
            # draw the green box and the number of people above it
            cv2.rectangle(frame, (x,y),  (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame, f"Human #{human_count}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            human_count += 1
      cv2.putText(frame, "Running...", (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0),2)
      cv2.putText(frame, f"Humans Seen : {human_count-1}", (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
      cv2.imshow('Results',frame)
      return frame
