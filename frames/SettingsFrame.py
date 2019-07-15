from tkinter import *
import pickle
import os


class SettingsFrame:
    def __init__(self, mf):
        self.main_frame = mf

        self.frame = Frame(self.main_frame, width=1050, height=560, bg="#f1f1f1")

        parent = os.path.abspath(os.path.join('frames', os.pardir))
        self.settings_data = pickle.loads(open(parent + "/data/settings.pickle", "rb").read())

        self.blue_mode = IntVar()
        self.create_mode_settings()

        self.blue_com = StringVar()
        self.blue_bauds = StringVar()
        self.refresh_blue = IntVar()

        self.create_bt_settings()

        self.history_refresh = IntVar()
        self.average_num = DoubleVar()
        self.votes_num = IntVar()

        self.create_general_settings()

    def create_mode_settings(self):

        frame_mode = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_mode, width=310, height=50, bg="#102027")
        Label(frame_title, text="Mode", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)
        frame_title.place(x=0, y=0)

        bt = Radiobutton(frame_mode, text="Use Bluetooth", bg="#FAFAFA",
                         borderwidth=4, font=("Roboto", 15), value=1, variable=self.blue_mode)

        no_bt = Radiobutton(frame_mode, text="Not use Bluetooth", bg="#FAFAFA",
                            borderwidth=4, font=("Roboto", 15), value=0, variable=self.blue_mode)

        if self.settings_data['blue_mode'] == 0:
            no_bt.select()
        else:
            bt.select()

        bt.place(x=20, y=80)
        no_bt.place(x=20, y=130)

        frame_mode.place(x=40, y=30)

    def create_bt_settings(self):

        frame_bt = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_bt, width=310, height=50, bg="#102027")
        Label(frame_title, text="Bluetooth", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)
        frame_title.place(x=0, y=0)

        Label(frame_bt, text="Puerto: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=80)
        com_entry = Entry(frame_bt, bg="#FAFAFA", width=8, font=("Roboto", 14), textvariable=self.blue_com)

        Label(frame_bt, text="Bauds: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=140)
        baud_entry = Entry(frame_bt, bg="#FAFAFA", width=8, font=("Roboto", 14), textvariable=self.blue_bauds)

        Label(frame_bt, text="Refresh: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=220)
        refresh_entry = Entry(frame_bt, bg="#FAFAFA", width=6, font=("Roboto", 14), textvariable=self.refresh_blue)

        com_entry.insert(0, self.settings_data['blue_com'])
        baud_entry.insert(0, self.settings_data['blue_bauds'])
        refresh_entry.delete(0, END)
        refresh_entry.insert(0, self.settings_data['refresh_blue'])

        com_entry.place(x=110, y=80)
        baud_entry.place(x=110, y=140)
        refresh_entry.place(x=110, y=220)

        frame_bt.place(x=370, y=30)

    def create_general_settings(self):

        frame_general = Frame(self.frame, width=310, height=480, bg="#FAFAFA")

        frame_title = Frame(frame_general, width=310, height=50, bg="#102027")
        Label(frame_title, text="General", bg="#102027", fg="#ffffff", font=("Roboto", 16)).place(x=20, y=10)
        frame_title.place(x=0, y=0)

        Label(frame_general, text="History: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=80)
        history_entry = Entry(frame_general, bg="#FAFAFA", width=8, font=("Roboto", 14),
                              textvariable=self.history_refresh)

        Label(frame_general, text="Average: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=140)
        average_entry = Entry(frame_general, bg="#FAFAFA", width=8, font=("Roboto", 14), textvariable=self.average_num)

        Label(frame_general, text="Votes: ", bg="#FAFAFA", fg="#000000", font=("Roboto", 15)).place(x=20, y=200)
        votes_entry = Entry(frame_general, bg="#FAFAFA", width=6, font=("Roboto", 14), textvariable=self.votes_num)

        history_entry.delete(0, END)
        average_entry.delete(0, END)
        votes_entry.delete(0, END)
        history_entry.insert(0, self.settings_data['refresh_history'])
        average_entry.insert(0, self.settings_data['average_num'])
        votes_entry.insert(0, self.settings_data['votes_num'])

        history_entry.place(x=110, y=80)
        average_entry.place(x=110, y=140)
        votes_entry.place(x=110, y=200)

        frame_general.place(x=700, y=30)

    def place_frame(self):
        self.frame.place(x=0, y=80)

    def forget_place(self):
        self.frame.place_forget()

    def save_settings(self):
        try:
            new_settings = {'blue_mode': self.blue_mode.get(),
                            'blue_com': self.blue_com.get(),
                            'blue_bauds': self.blue_bauds.get(),
                            'refresh_blue': self.refresh_blue.get(),
                            'refresh_history': self.history_refresh.get(),
                            'average_num': self.average_num.get(),
                            'votes_num': self.votes_num.get()}

            print(new_settings)
            f = open("data/settings.pickle", "wb")
            f.write(pickle.dumps(new_settings))
            f.close()
        except:
            print("ERROR")
