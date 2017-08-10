import PIL.ImageGrab
import numpy as np
from cv2 import *
import cv2
import msvcrt
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Frames per second (fps).', default=8, type=int)
parser.add_argument('-n', help='Video name.', default='capture', type=str)
args = parser.parse_args()

def keyStroke():
    ks = False
    if msvcrt.kbhit:
        ks = msvcrt.getch()
    
    return ks

def getCurrentFrame():
    im = PIL.ImageGrab.grab()
    return im

def main():
    try:
        recording = False
        fps = 8
        video_name = "capture"        
        video_name = args.n
        fps = args.f
        im = getCurrentFrame()
        img_arr = np.array(im)
        frame_size = cv.GetSize(cv.fromarray(img_arr))
        fourcc = cv.CV_FOURCC('i','Y', 'U', 'V')
        vid = cv.CreateVideoWriter(video_name + ".avi", fourcc, fps, frame_size, True)


        print("Press 'r' to start recording, Ctrl+C to stop recording or exit. \n")
        kbd = keyStroke()

        while kbd.decode() == 'r':
            recording = True
            im = getCurrentFrame()
            print(str(im.getdata()))
            img_arr = np.array(im)
            img_arr = cv2.cvtColor(img_arr, cv.CV_BGR2RGB)
            bitmap = cv.CreateImageHeader((img_arr.shape[1], img_arr.shape[0]), cv.IPL_DEPTH_8U, 3)
            cv.SetData(bitmap, img_arr.tostring(), img_arr.dtype.itemsize * 3 * img_arr.shape[1])
            cv.WriteFrame(vid, bitmap)
    except KeyboardInterrupt:
        print('\n')
        print('Recording finished. \n')
        sys.exit()
    

if __name__ == '__main__':
    main()
