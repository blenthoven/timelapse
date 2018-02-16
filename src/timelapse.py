import cv2
import sys
import os
import time

def render_video(path, _rate):

    rate = int(_rate)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path + '/output.avi', fourcc, 24.0, (1920, 1080))

    files = sorted(os.listdir(sys.argv[1]))

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 600,600)

    for f in files:
        ret = True
        stop = False
        i = 0

        path_to_file = path + "/" + f
        cap = cv2.VideoCapture(path_to_file)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        while(i < length):
            ret, frame = cap.read()
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            i += 15
            cv2.imshow('frame', frame)
            out.write(frame)
            print(str(i) + " " + str(length))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                stop = True
                print("break")
                break

        cap.release()
        if stop:
            break

    out.release()

if len(sys.argv) != 3:
    print("Invalid arguments")

if os.path.exists(sys.argv[1]):
    render_video(sys.argv[1], sys.argv[2])
