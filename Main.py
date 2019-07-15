from tkinter import *
from frames import HistoryFrame, IdFrame, SettingsFrame


class Main:

    def __init__(self, vt):
        self.main_frame = vt

        self.settings()

        self.up_toolbar = Frame(self.main_frame, width=1050, height=15, bg="#000a12")  # 80 star
        self.toolbar = Frame(self.main_frame, width=1050, height=65, bg="#263238")
        self.put_toolbar()

        self.hist_frame = HistoryFrame.HistoryFrame(self.main_frame)
        self.sett_frame = SettingsFrame.SettingsFrame(self.main_frame)
        self.id_frame = IdFrame.IdFrame(self.main_frame)

        self.frame_id_place = 0

        self.history_but = None
        self.settings_but = None
        self.idimage_but = None
        self.create_toolbar_buttons()
        self.button_id = None
        self.create_id_button()

        self.put_id_frame()

        self.main_frame.protocol("WM_DELETE_WINDOW", self.command_save_close)

    def settings(self):
        self.main_frame.config(bg="#f1f1f1")
        self.main_frame.title("")
        self.main_frame.resizable(0, 0)

        winx = self.main_frame.winfo_screenwidth()
        winy = self.main_frame.winfo_screenheight()
        # screen center
        cx = int((winx - 1050) / 2)
        cy = int((winy - 640) / 2) - 28
        self.main_frame.geometry(f"1050x640+{cx}+{cy}")

    def put_toolbar(self):
        Label(self.toolbar, text="Face ID", bg="#263238", fg="#ffffff", font=("Roboto", 21)).place(x=20, y=10)
        self.up_toolbar.pack()
        self.toolbar.pack()

    def put_id_frame(self):
        self.frame_id_place = 0

        self.hist_frame.forget_place()
        self.sett_frame.forget_place()
        self.id_frame.forget_place()

        self.id_frame.place_frame()

        play_image = PhotoImage(file="images/play.png")
        self.button_id.config(image=play_image)
        self.button_id.image = play_image

    def put_history_frame(self):
        self.frame_id_place = 1

        self.hist_frame.forget_place()
        self.sett_frame.forget_place()
        self.id_frame.forget_place()

        self.hist_frame.place_frame()

        delete_image = PhotoImage(file="images/delete.png")
        self.button_id.config(image=delete_image)
        self.button_id.image = delete_image

    def put_settings_frame(self):
        self.frame_id_place = 2

        self.hist_frame.forget_place()
        self.sett_frame.forget_place()
        self.id_frame.forget_place()

        self.sett_frame.place_frame()

        save_image = PhotoImage(file="images/save.png")
        self.button_id.config(image=save_image)
        self.button_id.image = save_image

    def create_toolbar_buttons(self):
        history_but_image = PhotoImage(file="images/history.png")
        self.history_but = Button(self.toolbar, bg="#263238", image=history_but_image, relief="flat",
                                  activebackground="#263238", overrelief="ridge", command=self.put_history_frame)

        self.history_but.place(x=910, y=6)
        self.history_but.image = history_but_image

        settings_but_image = PhotoImage(file="images/settings.png")
        self.settings_but = Button(self.toolbar, bg="#263238", image=settings_but_image, relief="flat",
                                   activebackground="#263238", overrelief="ridge", command=self.put_settings_frame)

        self.settings_but.place(x=980, y=6)
        self.settings_but.image = settings_but_image

        idimage_but_image = PhotoImage(file="images/idimage.png")
        self.idimage_but = Button(self.toolbar, bg="#263238", image=idimage_but_image, relief="flat",
                                  activebackground="#263238", overrelief="ridge", command=self.put_id_frame)

        self.idimage_but.place(x=840, y=6)
        self.idimage_but.image = idimage_but_image

    def create_id_button(self):
        image_but_id = PhotoImage(file="images/play.png")
        self.button_id = Button(self.toolbar, bg="#263238", image=image_but_id, relief="flat",
                                activebackground="#263238", overrelief="ridge", command=self.command_for_id_button)

        self.button_id.place(x=730, y=6)
        self.button_id.image = image_but_id

    def command_for_id_button(self):
        if self.frame_id_place == 0:
            self.id_frame.start_loop()
        elif self.frame_id_place == 1:
            self.hist_frame.delete_history()
        elif self.frame_id_place == 2:
            self.sett_frame.save_settings()

    def command_save_close(self):
        self.id_frame.save_hist_data()
        self.main_frame.destroy()


Vt = Tk()
v = Main(Vt)
Vt.mainloop()
