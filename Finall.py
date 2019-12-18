import tkinter as tk
from tkinter import *
from pynput.mouse import Controller as Ctrl, Button as Btn
import cv2
import dlib
from math import hypot
import numpy as np

font = cv2.FONT_HERSHEY_DUPLEX
mouse = Ctrl()


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.frame_no = 0

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self.frame_no = frame_class.frame_no
        print(self.frame_no)
        mouse.position = new_frame.pos
        self._frame.pack()


class StartPage(tk.Frame):
    frame_no = 1
    pos = [400, 350]

    def __init__(self, master):
        tk.Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        self.label1 = Label(self, text="Select the account you wish to use", bg="#add8e6", width=100)
        self.label1.pack()
        self.label1.place(x=250, y=200)
        self.account1 = Button(self, text="Account 1", bg="#42f590", bd="4", activebackground="#4287f5",
                               command=lambda: master.switch_frame(PagePin).pack())
        self.account1.pack()
        self.account1.place(x=350, y=300, height=100, width=100)
        self.account2 = Button(self, text="Account 2", bg="#42f590", bd="4", activebackground="#4287f5",
                               command=lambda: master.switch_frame(PagePin).pack())
        self.account2.pack()
        self.account2.place(x=550, y=300, height=100, width=100)
        self.account3 = Button(self, text="Account 3", bg="#42f590", bd="4", activebackground="#4287f5",
                               command=lambda: master.switch_frame(PagePin).pack())
        self.account3.pack()
        self.account3.place(x=750, y=300, height=100, width=100)


class PagePin(Frame):
    frame_no = 2
    pos = [530, 160]

    def __init__(self, master):
        Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        label1 = Label(self, text="Please enter your PIN", bg="#add8e6", width=100)
        label1.pack()
        label1.place(x=250, y=20)
        self.entry1 = Entry(self, width=40)
        self.entry1.pack()
        self.entry1.place(x=480, y=50)
        btn_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        r = 0
        c = 0
        for b in btn_list:
            b = Button(self, text=b, width=7, height=5, bg="#42adf5", command=lambda btn=b: self.digit_action(btn))
            b.pack()
            b.place(x=500 + c*60, y=120 + r*80)
            c += 1
            if c > 2:
                c = 0
                r += 1

        b1 = Button(self, text='C', width=7, height=4, bg='#42adf5', command=lambda: self.clear())
        b1.pack()
        b1.place(x=500, y=365)
        b1 = Button(self, text='0', width=7, height=4, bg='#42adf5', command=lambda btn=b: self.digit_action(btn))
        b1.pack()
        b1.place(x=560, y=365)
        b1 = Button(self, text='Enter', width=7, height=4, bg='#42adf5',
                    command=lambda: master.switch_frame(PageOptions).pack())
        b1.pack()
        b1.place(x=620, y=365)

    def digit_action(self, btn):
        self.entry1.insert(END, btn)

    def clear(self):
        self.entry1.delete(0, END)


class PageOptions(tk.Frame):
    frame_no = 3
    pos = [100, 300]

    def __init__(self, master):
        Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        label1 = Label(self, text="Select what you wish to do", bg="#add8e6", width=100)
        label1.pack()
        label1.place(x=250, y=200)
        b1 = Button(self, text='Deposit', width=22, height=5, bg='#42adf5', command=lambda: master.switch_frame(PageDeposit).pack())
        b1.pack()
        b1.place(x=1000, y=250)
        b2 = Button(self, text='Withdraw', width=22, height=5, bg='#42adf5', command=lambda: master.switch_frame(PageWithdraw).pack())
        b2.pack()
        b2.place(x=1000, y=400)
        b3 = Button(self, text='Check Balance', width=22, height=5, bg='#42adf5', command=lambda: master.switch_frame(PageBalance).pack())
        b3.pack()
        b3.place(x=50, y=250)
        b4 = Button(self, text='Account Transfer', width=22, height=5, bg='#42adf5', command=lambda: master.switch_frame(PageTrans).pack())
        b4.pack()
        b4.place(x=50, y=400)
        b5 = Button(self, text='Mini Statement', width=22, height=5, bg='#42adf5', command=lambda: master.switch_frame(PageEnd).pack())
        b5.pack()
        b5.place(x=1000, y=550)
        b6 = Button(self, text='PIN Generation', width=22, height=5, bg='#42adf5', command=lambda: master.switch_frame(PageEnd).pack())
        b6.pack()
        b6.place(x=50, y=550)


class PageDeposit(tk.Frame):
    frame_no = 4
    pos = [620, 350]

    def __init__(self, master):
        Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        label1 = Label(self, text="Insert the amount you wish to deposit and enter", bg="#add8e6", width=100)
        label1.pack()
        label1.place(x=250, y=200)
        b1 = Button(self, text="Done", width=10, height=3, bg='#42adf5',
                    command=lambda: master.switch_frame(PageEnd).pack())
        b1.pack()
        b1.place(x=550, y=300)


class PageWithdraw(tk.Frame):
    frame_no = 5
    pos = [550, 340]

    def __init__(self, master):
        Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        label1 = Label(self, text="Enter the amount", bg="#add8e6", width=100)
        label1.pack()
        label1.place(x=250, y=200)
        self.entry1 = Entry(self, width=40)
        self.entry1.pack()
        self.entry1.place(x=480, y=230)
        btn_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        r = 0
        c = 0
        for b in btn_list:
            b = Button(self, text=b, width=7, height=5, bg="#42adf5", command=lambda btn=b: self.digit_action(btn))
            b.pack()
            b.place(x=500 + c * 60, y=300 + r * 80)
            c += 1
            if c > 2:
                c = 0
                r += 1

        b1 = Button(self, text='C', width=7, height=4, bg='#42adf5', command=lambda: self.clear())
        b1.pack()
        b1.place(x=500, y=545)
        b1 = Button(self, text='0', width=7, height=4, bg='#42adf5', command=lambda btn=b: self.digit_action(btn))
        b1.pack()
        b1.place(x=560, y=545)
        b1 = Button(self, text='Enter', width=7, height=4, bg='#42adf5', command=lambda: master.switch_frame(PageEnd).pack())
        b1.pack()
        b1.place(x=620, y=545)

    def digit_action(self, btn):
        self.entry1.insert(END, btn)

    def clear(self):
        self.entry1.delete(0, END)


class PageTrans(tk.Frame):
    frame_no = 6
    pos = [550, 340]

    def __init__(self, master):
        Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        label1 = Label(self, text="Enter the recipient account number", bg="#add8e6", width=100)
        label1.pack()
        label1.place(x=250, y=200)
        self.entry1 = Entry(self, width=40)
        self.entry1.pack()
        self.entry1.place(x=480, y=230)
        btn_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        r = 0
        c = 0
        for b in btn_list:
            b = Button(self, text=b, width=7, height=5, bg="#42adf5", command=lambda btn=b: self.digit_action(btn))
            b.pack()
            b.place(x=500 + c * 60, y=300 + r * 80)
            c += 1
            if c > 2:
                c = 0
                r += 1

        b1 = Button(self, text='C', width=7, height=4, bg='#42adf5', command=lambda: self.clear())
        b1.pack()
        b1.place(x=500, y=545)
        b1 = Button(self, text='0', width=7, height=4, bg='#42adf5', command=lambda btn=b: self.digit_action(btn))
        b1.pack()
        b1.place(x=560, y=545)
        b1 = Button(self, text='Enter', width=7, height=4, bg='#42adf5',
                    command=lambda: master.switch_frame(PageWithdraw).pack())
        b1.pack()
        b1.place(x=620, y=545)

    def digit_action(self, btn):
        self.entry1.insert(END, btn)

    def clear(self):
        self.entry1.delete(0, END)


class PageBalance(tk.Frame):
    frame_no = 7
    pos = [590, 340]

    def __init__(self, master):
        Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        label1 = Label(self, text="Your account balance is : xxxx", bg="#add8e6", width=100)
        label1.pack()
        label1.place(x=250, y=200)
        b1 = Button(self, text='Done', width=10, height=3, bg='#42adf5', command=lambda: master.switch_frame(PageEnd).pack())
        b1.pack()
        b1.place(x=550, y=300)


class PageEnd(tk.Frame):
    frame_no = 8
    pos = [590, 340]

    def __init__(self, master):
        Frame.__init__(self, master, width=1200, height=700, background="#add8e6")
        label1 = Label(self, text="Thank you for using this ATM", bg="#add8e6", width=100)
        label1.pack()
        label1.place(x=250, y=200)
        b1 = Button(self, text='Main Page', width=10, height=3, bg='#42adf5',
                    command=lambda: master.switch_frame(PageOptions).pack())
        b1.pack()
        b1.place(x=550, y=300)


def rightmove():
    if app.frame_no == 1:
        if mouse.position[0] > 400:
            mouse.move(-200, 0)
        else:
            mouse.move(200, 0)
    elif app.frame_no == 2 or app.frame_no == 5 or app.frame_no == 6:
        if mouse.position[0] >= 600:
            if mouse.position[1] >= 540:
                mouse.position = (530, 340)
            else:
                mouse.move(-120, 80)
        else:
            mouse.move(60, 0)
    elif app.frame_no == 3:
        if mouse.position[0] > 600:
            mouse.move(-1000, 150)
        else:
            mouse.move(1000, 0)
    else:
        pass


def leftmove():
    if app.frame_no == 1:
        if mouse.position[0] < 200:
            mouse.move(200, 0)
        else:
            mouse.move(-200, 0)
    elif app.frame_no == 2 or app.frame_no == 5 or app.frame_no == 6:
        if mouse.position[0] <= 560:
            if mouse.position[1] <= 380:
                mouse.position = (650, 580)
            else:
                mouse.move(120, -80)
        else:
            mouse.move(-60, 0)
    elif app.frame_no == 3:
        if mouse.position[0] > 600:
            mouse.move(-1000, 0)
        else:
            if mouse.position[1] < 400:
                mouse.position = (1050, 650)
            else:
                mouse.move(1000, -150)
    else:
        pass


def select():
    mouse.click(Btn.left, 1)


def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


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

    eye = graay[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(eye, 20, 255, cv2.THRESH_BINARY)
    # eye = cv2.resize(eye, None, fx=5, fy=5)
    # threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)

    h, w = threshold_eye.shape
    left_threshold = threshold_eye[0: h, 0: int(w / 2)]
    left_white = cv2.countNonZero(left_threshold)
    right_threshold = threshold_eye[0: h, int(w / 2): w]
    right_white = cv2.countNonZero(right_threshold)

    ratio = left_white - right_white
    return ratio


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


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1200x700+0+0")
    cap = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    f = 0
    j = 0
    k = 0

    run = True
    while run:
        app.update()
        ret, frame = cap.read()
        graay = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(graay)

        for face in faces:
            landmarks = predictor(graay, face)
            cv2.rectangle(graay, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 255), 2)

            blink = blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
            if blink > 4.3:
                f += 1
                if f > 3:
                    select()
                    graay = cv2.putText(graay, "Blink" + str(blink), (50, 50), font, 0.5, (255, 255, 255), 1,
                                        cv2.LINE_AA)
                    f = 0
            # if f > 0 and blink < 4.12:
            #     select()
            #     i = 0
            # if blink > 4.12:
            #     f += 1
            #     graay = cv2.putText(graay, "Blink m8", (50, 250), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

            gaze = gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)

            if gaze > 20:
                j += 1
                if j > 7:
                    leftmove()
                    j = 0
                # left side of screen
                cv2.putText(graay, "Left", (50, 50), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(graay, str(gaze), (50, 70), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)

            elif gaze < -70:
                k += 1
                if k > 7:
                    rightmove()
                    k = 0
                # right side of screen
                cv2.putText(graay, "Right", (450, 50), font, 0.5, (255, 255, 0), 1, cv2.LINE_AA)
                cv2.putText(graay, str(gaze), (50, 70), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)

            else:
                # center
                cv2.putText(graay, "Center", (250, 50), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(graay, str(gaze), (50, 70), font, 0.5, (255, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow("hi", graay)

    cap.release()
    cv2.destroyAllWindows()
