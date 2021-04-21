#librarie
import cv2
import numpy 
import imutils # A library I discovered the other day that has helpful methods for working with opencv and numpy.
import argparse # To be used for testing through command line

"""
• A way to detect a person in singular frame.
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

def output_option(args):
      path_to_video = args['video']
      path_to_image = args['image']

      if str(args["camera"]) == 'true':
            use_camera = True
      else:
            use_camera = False
      dis = None 
      if args['output'] is not None and path_to_image is None:
            dis = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600,600))

      if use_camera:
            detectByCamera()

def detectByCamera(dis):
      output = cv2.VideoCapture(0)
      print("Detecting Humans...")
      while True:
            inp,frame = output.read()
            frame = render_human(frame)
            if dis is not None:
                  dis.write(frame)
            trigger = cv2.waitKey(1)
            if trigger == ord('q'):
                  break
      output.release()
      cv2.destroyAllWindows()

if __name__ == "__main__":
    # A pre-trained model available to us for detectcting humans; built into OpenCV!
    model = cv2.HOGDescriptor()
    # Will feed support vector machine with this call to the model.
    model.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    args = argsParser()
    output_option(args)
