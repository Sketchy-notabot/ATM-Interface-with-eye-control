import cv2
import numpy as np
import dlib
from math import hypot

numpad = np.zeros((600, 300, 3), np.uint8)


def numberpad(num):
    if num == 1:
        x = 0
        y = 0
    elif num == 2:
        x = 100
        y = 0
    elif num == 3:
        x = 200
        y = 0
    elif num == 4:
        x = 0
        y = 150
    elif num == 5:
        x = 100
        y = 150
    elif num == 6:
        x = 200
        y = 150
    elif num == 7:
        x = 0
        y = 300
    elif num == 8:
        x = 100
        y = 300
    elif num == 9:
        x = 200
        y = 300
    elif num == 0:
        x = 100
        y = 450
    cv2.rectangle(numpad, (x + 2, y + 2), (x + 100 - 2, y + 150 - 2), (20, 255, 57), 2)
    num_size = cv2.getTextSize(str(num), cv2.FONT_HERSHEY_SIMPLEX, 4, 2)
    num_width, num_height = num_size[0], num_size[1]
    num_x = int((100 - num_width[0]) / 2) + x
    num_y = int((170 + num_height) / 2) + y
    cv2.putText(numpad, str(num), (num_x, num_y), cv2.FONT_HERSHEY_SIMPLEX, 4, (140, 215, 157), 2)


for i in range(10):
    numberpad(i)


def rightmove(curr_x, curr_y):
    cv2.rectangle(numpad, (curr_x + 2, curr_y + 2), (curr_x + 100 - 2, curr_y + 150 - 2), (20, 255, 57), 2)
    if curr_x == 100 and curr_y == 450:
        curr_x = 0
        curr_y = 0
    elif curr_x == 200:
        if curr_y == 300:
            curr_x = 100
        else:
            curr_x = 0
        curr_y = curr_y + 150
    else:
        curr_x = curr_x + 100

    cv2.rectangle(numpad, (curr_x + 2, curr_y + 2), (curr_x + 98, curr_y + 148), (0, 0, 255), 2)
    return (curr_x, curr_y)



def leftmove(curr_x, curr_y):
    cv2.rectangle(numpad, (curr_x + 2, curr_y + 2), (curr_x + 100 - 2, curr_y + 150 - 2), (20, 255, 57), 2)
    if curr_x == 100 and curr_y == 450:
        curr_x = 200
        curr_y = 300
    elif curr_x == 0:
        if curr_y == 0:
            curr_x = 100
            curr_y = 450
        else:
            curr_x = 200
            curr_y = curr_y - 150
    else:
        curr_x = curr_x - 100

    cv2.rectangle(numpad, (curr_x + 2, curr_y + 2), (curr_x + 98, curr_y + 148), (0, 0, 255), 2)
    return (curr_x, curr_y)


def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


def blinking_ratio(eye, landmarks):
    left_point = (landmarks.part(eye[0]).x, landmarks.part(eye[0]).y)
    right_point = (landmarks.part(eye[3]).x, landmarks.part(eye[3]).y)
    top_point = midpoint(landmarks.part(eye[1]), landmarks.part(eye[2]))
    bottom_point = midpoint(landmarks.part(eye[5]), landmarks.part(eye[4]))

    # gray = cv2.circle(gray, top_point, 3, (0, 0, 255), 1)

    hor_length = hypot(left_point[0] - right_point[0], left_point[1] - right_point[1])
    ver_length = hypot(top_point[0] - bottom_point[0], top_point[1] - bottom_point[1])

    blink_ratio = hor_length / ver_length
    return blink_ratio


def gaze_ratio(eye, landmarks):

    roi_left_eye = np.array([(landmarks.part(eye[0]).x, landmarks.part(eye[0]).y),
                             (landmarks.part(eye[1]).x, landmarks.part(eye[1]).y),
                             (landmarks.part(eye[2]).x, landmarks.part(eye[2]).y),
                             (landmarks.part(eye[3]).x, landmarks.part(eye[3]).y),
                             (landmarks.part(eye[4]).x, landmarks.part(eye[4]).y),
                             (landmarks.part(eye[5]).x, landmarks.part(eye[5]).y)], np.int32)
    # cv2.polylines(gray, [roi_left_eye], True, (0, 0, 255), 2)

    min_x = np.min(roi_left_eye[:, 0])
    max_x = np.max(roi_left_eye[:, 0])
    min_y = np.min(roi_left_eye[:, 1])
    max_y = np.max(roi_left_eye[:, 1])

    eye = gray[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(eye, 30, 255, cv2.THRESH_BINARY)
    eye = cv2.resize(eye, None, fx=5, fy=5)
    threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)

    h, w = threshold_eye.shape
    left_threshold = threshold_eye[0: h, 0: int(w / 2)]
    left_white = cv2.countNonZero(left_threshold)
    right_threshold = threshold_eye[0: h, int(w / 2): w]
    right_white = cv2.countNonZero(right_threshold)

    ratio = left_white - right_white
    return ratio


text = ""


def select(curr_x, curr_y):
    if curr_y == 0:
        if curr_x == 0:
            nom = 1
        elif curr_x == 100:
            nom = 2
        else:
            nom = 3
    elif curr_y == 150:
        if curr_x == 0:
            nom = 4
        elif curr_x == 100:
            nom = 5
        else:
            nom = 6
    elif curr_y == 300:
        if curr_x == 0:
            nom = 7
        elif curr_x == 100:
            nom = 8
        else:
            nom = 9
    else:
        nom = 0
    return nom


font = cv2.FONT_HERSHEY_DUPLEX
frames = 0
curr_x = 0
curr_y = 0
i = 0
j = 0
k = 0
cv2.rectangle(numpad, (curr_x + 2, curr_y + 2), (curr_x + 98, curr_y + 148), (0, 0, 255), 2)


cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        cv2.rectangle(gray, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 255), 2)
        left_ratio = blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        right_ratio = blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)

        if i > 0 and left_ratio < 4.12:
            n = select(curr_x, curr_y)
            text += str(n)
            print(text)
            i = 0
        if left_ratio > 4.12:
            i += 1
            gray = cv2.putText(gray, "Blink m8", (50, 250), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        gaze = gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)


        if gaze > 300:
            j += 1
            if j > 5:
                (curr_x, curr_y) = leftmove(curr_x, curr_y)
                j = 0
            # left side of screen
            cv2.putText(gray, "Left ", (50, 50), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(gray, str(gaze), (50, 70), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)

        elif gaze < -900:
            k += 1
            if k > 5:
                (curr_x, curr_y) = rightmove(curr_x, curr_y)
                k = 0
            # right side of screen
            cv2.putText(gray, "Right", (450, 50), font, 0.5, (255, 255, 0), 1, cv2.LINE_AA)
            cv2.putText(gray, str(gaze), (50, 70), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)

        else:
            # center
            cv2.putText(gray, "Center", (250, 50), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.putText(gray, str(gaze), (50, 70), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow('FACE', gray)
    cv2.imshow('Numpad', numpad)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
