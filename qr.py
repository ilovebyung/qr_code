import time
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os
import sys


def read_qr():
    while True:

        success, frame = cap.read()
        # resize frame
        #frame = imutils.resize(frame, width=480)
        # grayscale
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for barcode in decode(frame):

            data = barcode.data.decode('utf-8')
            # print(data)  # if data = 'data'
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(
                frame, data, (pts2[0], pts2[1]), font, 0.9, (255, 0, 255), 2)

            if data == 'WELCOME':
                print(data)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break


try:
    # opencv etup
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)

    # full screen window
    #cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    read_qr()

except Exception as e:
    print(e)  # print error exception
# Run a new iteration of the current script.
# os.execv(sys.executable, ['python'] + [sys.argv[0]])
