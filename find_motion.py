import cv2
from spot_diff import spot_diff
import time
import numpy as np


def find_motion():

	motion_detected = False
	is_start_done = False

	cap = cv2.VideoCapture(0)

	check = []
	
	print("waiting for 2 seconds")
	time.sleep(2)
	frame1 = cap.read()

	_, frm1 = cap.read()
	frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

	
	while True:
		_, frm2c = cap.read()
		frm2 = cv2.cvtColor(frm2c, cv2.COLOR_BGR2GRAY)

		diff = cv2.absdiff(frm1, frm2)

		_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

		contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

		#look at it
		contors = [c for c in contors if cv2.contourArea(c) > 25]


		if len(contors) > 5:
			cv2.putText(frm2c, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,0),2)
			motion_detected = True
			is_start_done = False

		elif motion_detected and len(contors) < 3:
			if (is_start_done) == False:
				start = time.time()
				is_start_done = True
				end = time.time()

			end = time.time()

			print(end-start)
			if (end - start) > 4:
				frame2 = cap.read()
				cap.release()
				cv2.destroyAllWindows()
				x = spot_diff(frame1, frame2)
				if x == 0:
					print("runnig again")
					return

				else:
					print("found motion sending mail")
					return

		else:
			cv2.putText(frm2c, "no motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

		cv2.imshow("winname", frm2c)

		_, frm1 = cap.read()
		frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

		if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			break

	return
