# ATM-Interface-with-eye-control
Uses eye gaze and blinking detecion to control an ATM machine to carry out tasks like account transfer, withdrawal, pin generation, checking account balance, etc.

The Finall.py is a python script that uses opencv to detect the eye gaze direction i.e. left, center or right and eye blink detection to control the 
cursor on the screen. Looking right would shift the cursor to the right, looking left to the left and blinking would select the current option.

The required libraries are:
cv2
dlib
pynput
numpy
cmake
