from tkinter import *
import pickle
import os


class HistoryFrame:
    def __init__(self, mf):
        self.main_frame = mf

        self.frame = Frame(self.main_frame, width=1050, height=560, bg="#f1f1f1")

        # Loading the data history
        parent = os.path.abspath(os.path.join('frames', os.pardir))
        self.data = pickle.loads(open(parent+"/data/hist_data.pickle", "rb").read())

        self.header_frame_data()

        self.frame_container = Frame(self.frame, bg="#FAFAFA")
        self.frame_container.place(x=130, y=80)
        self.frame_data = None
        self.canvas_scroll()
        self.create_list()

    def header_frame_data(self):

        frame_header = Frame(self.frame, width=800, height=60, bg="#102027")
        Label(frame_header, text="ID", bg="#102027", fg="#ffffff", font=("Roboto", 17)).place(x=20, y=13)
        Label(frame_header, text="Date", bg="#102027", fg="#ffffff", font=("Roboto", 17)).place(x=190, y=13)
        Label(frame_header, text="Votes", bg="#102027", fg="#ffffff", font=("Roboto", 17)).place(x=440, y=13)
        Label(frame_header, text="Average", bg="#102027", fg="#ffffff", font=("Roboto", 17)).place(x=560, y=13)
        Label(frame_header, text="Mode", bg="#102027", fg="#ffffff", font=("Roboto", 17)).place(x=690, y=13)
        frame_header.place(x=130, y=20)

    def canvas_scroll(self):
        vscrollbar = Scrollbar(self.frame_container, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self.frame_container, height=450, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.frame_data = frame_data = Frame(canvas, bg="#FAFAFA")
        interior_id = canvas.create_window(0, 0, window=frame_data,
                                           anchor=NW)

        def _configure_interior(e):
            size = (frame_data.winfo_reqwidth(), frame_data.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if frame_data.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=frame_data.winfo_reqwidth())

        frame_data.bind('<Configure>', _configure_interior)

        def _configure_canvas(e):
            if frame_data.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

    def create_list(self):
        # Loading the data in labels
        for r, ob_list in enumerate(self.data):
            for c, ob_tup in enumerate(ob_list):
                Label(self.frame_data, text=ob_tup, bg="#FAFAFA", fg="#333333", font=("Roboto Lt", 16)).grid(row=r,
                                                                                                             column=c,
                                                                                                             sticky=W,
                                                                                                             ipady=10,
                                                                                                             ipadx=30)

    def place_frame(self):
        self.frame.place(x=0, y=80)

    def forget_place(self):
        self.frame.place_forget()

    def delete_history(self):
        print("DELETE")
