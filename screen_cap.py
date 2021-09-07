import pyautogui
import cv2
import numpy as np


res = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

file_name = "My_Rec.avi"

fps = 60

out = cv2.VideoWriter(file_name, codec, fps, res)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 1280, 720)

while True:
    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'):
        break


out.release()
cv2.destroyAllWindows()