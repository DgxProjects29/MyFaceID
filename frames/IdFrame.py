import os
import pickle
from tkinter import *

import PIL.Image
import PIL.ImageTk

from classes import CameraView, FaceScan3, DataBase, BluePy


class IdFrame:
    def __init__(self, mf):
        self.main_frame = mf

        self.frame = Frame(self.main_frame, width=1050, height=560, bg="#f1f1f1")

        parent = os.path.abspath(os.path.join('frames', os.pardir))
        self.data_settings = pickle.loads(open(parent + "/data/settings.pickle", "rb").read())

        self.Cview = CameraView.CameraView()
        self.Cview.start()  # it does nothing

        self.canvas = None
        self.canvas_camera()

        self.data = DataBase.get_id_data()
        self.history_data = []

        # data labels, where the data of the person is placed
        self.id_label = None
        self.name_label = None
        self.age_label = None
        self.company_label = None
        self.create_frame_data()

        # delay of the camera loop, 15 milliseconds
        self.delay = 15
        self.id = "UnKnown"
        self.face_scan = FaceScan3.FaceScan()

        # Variables for the bluetooth reset
        self.reset_blue_start = False
        self.reset_blue_count = 0

        # Variables for taking an example for the history
        self.scan_write = True
        self.scan_write_count = 0

        # Variables for recognizing an unknown person
        self.unknown_p = True
        self.count_unknown_p = 0

        self.bluepy = None

    # When you close the window this method is called to save the history data
    def save_hist_data(self):

        parent = os.path.abspath(os.path.join('frames', os.pardir))
        old_data = pickle.loads(open(parent + "/data/hist_data.pickle", "rb").read())
        new_data = self.history_data
        for i in new_data:
            old_data.append(i)

        f = open(parent + "/data/hist_data.pickle", "wb")
        f.write(pickle.dumps(old_data))
        f.close()

    def canvas_camera(self):
        self.canvas = Canvas(self.frame, width=640, height=480, bg="#FAFAFA", bd=0, highlightthickness=0,
                             relief='ridge')
        self.canvas.place(x=40, y=40)  # 640 y 480

    # the Main loop of the program
    def camera_loop(self):
        ret, frame = self.Cview.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

            # Part of the loop for scanning the face

            # a different scan if you choose bluetooth method or not
            if self.data_settings['blue_mode'] == 1:
                self.blue_option(frame)
            else:
                _id, vot, av = self.face_scan.scanning(frame)

                if _id != "NoFace":

                    if _id == "UnKnown":
                        self.count_unknown_p += 1
                        print(self.count_unknown_p)
                        if self.count_unknown_p >= self.data_settings['unknown_num']:
                            print("UnKnown")
                            self.count_unknown_p = 0
                    else:
                        print("ID:", _id)
                        self.count_unknown_p = 0

                else:
                    print("NoFace")
                    self.count_unknown_p = 0

                self.put_label_data(_id)

                # Part of the loop for the history data

                if self.scan_write:
                    self.scan_write_count += 1
                    if self.scan_write_count >= self.data_settings['refresh_history']:
                        self.scan_write = False
                        self.scan_write_count = 0
                else:
                    self.put_history_data(_id, vot, av, 'No Bt')
                    self.scan_write = True

        self.frame.after(self.delay, self.camera_loop)

    def start_blue(self):
        self.bluepy = BluePy.BluePy()
        self.bluepy.start()

    # If you choose bluetooth method, this method runs
    def blue_option(self, frame):

        if not self.reset_blue_start:

            _id, vot, av = self.face_scan.scanning(frame)
            print("Scanning")

            if _id != "NoFace":

                if _id == "UnKnown":
                    if self.bluepy.is_connected():
                        self.bluepy.send_turn_off_message()
                        print("Turn Off")
                    else:
                        print("Error")
                    self.count_unknown_p += 1
                    print("unknown count -->  ", self.count_unknown_p)
                    if self.count_unknown_p >= self.data_settings['unknown_num']:
                        if self.bluepy.is_connected():
                            self.bluepy.send_close_message()
                            print("Send Unknown")
                            self.count_unknown_p = 0
                        else:
                            print("Error")
                            self.count_unknown_p = 0
                else:
                    if self.bluepy.is_connected():
                        self.bluepy.send_open_message()
                        print("Send Known")
                        self.count_unknown_p = 0
                        self.reset_blue_start = True
                    else:
                        print("Error")
                        self.count_unknown_p = 0

            else:
                if self.bluepy.is_connected():
                    self.bluepy.send_turn_off_message()
                    print("Send NoFace Turn off")
                    self.count_unknown_p = 0
                else:
                    print("Error")
                    self.count_unknown_p = 0

            self.put_label_data(_id)

        else:
            self.reset_blue_count += 1
            if self.reset_blue_count >= self.data_settings['refresh_blue']:  # wait 5 seconds
                self.reset_blue_start = False
                self.reset_blue_count = 0


    def create_frame_data(self):
        frame_data = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_data, width=310, height=50, bg="#102027")
        frame_title.place(x=0, y=0)

        Label(frame_data, text="Card", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)

        Label(frame_data, text="Id :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=80)
        Label(frame_data, text="Name :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=160)
        Label(frame_data, text="Age :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=240)
        Label(frame_data, text="Company :", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 15)).place(x=20, y=320)

        self.id_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))
        self.name_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))
        self.age_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))
        self.company_label = Label(frame_data, text="", bg="#FAFAFA", fg="#000000", font=("Roboto Lt", 13))

        self.id_label.place(x=20, y=115)
        self.name_label.place(x=20, y=195)
        self.age_label.place(x=20, y=275)
        self.company_label.place(x=20, y=355)

        frame_data.place(x=700, y=40)

    def put_label_data(self, _id):
        if _id != "UnKnown" and _id != "NoFace":
            self.id_label.config(text=_id)
            self.name_label.config(text=self.data[_id][1])
            self.age_label.config(text=self.data[_id][2])
            self.company_label.config(text=self.data[_id][3])
        else:
            self.id_label.config(text=_id)
            self.name_label.config(text="")
            self.age_label.config(text="")
            self.company_label.config(text="")

    def put_history_data(self, _id, vot, av, bt_text):
        if _id != "UnKnown" and _id != "NoFace":
            self.history_data.append(
                (_id, DataBase.get_current_time(), DataBase.dic_to_text(vot, False), DataBase.dic_to_text(av, True),
                 bt_text))
        elif _id == "UnKnown":
            self.history_data.append(
                ("UnKnown", DataBase.get_current_time(), DataBase.dic_to_text(vot, False),
                 DataBase.dic_to_text(av, True), bt_text))
        print('<--Save-->', self.history_data)

    def place_frame(self):
        self.frame.place(x=0, y=80)

    def forget_place(self):
        self.frame.place_forget()

    def start_loop(self):
        if self.data_settings['blue_mode'] == 1:
            self.start_blue()

        self.camera_loop()
