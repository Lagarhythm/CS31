# Christopher Earl, Chapter 13 Lab 1
import tkinter
import tkinter.messagebox


class Ch13Lab1:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Christopher Earl, Ch 13 Lab 1')             # displayed in title bar

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create labels
        self.label1 = tkinter.Label(self.top_frame, text='Christopher Earl', borderwidth=4, relief='solid')
        self.label2 = tkinter.Label(self.bottom_frame, text='LBCC', borderwidth=4, relief='groove')
        self.label3 = tkinter.Label(self.bottom_frame, text='Computer Science', borderwidth=4, relief='sunken')

        # Pack the labels
        self.label1.pack(ipadx=40, ipady=20)
        self.label2.pack(ipadx=20, ipady=20, side='left')
        self.label3.pack(ipadx=20, ipady=20, side='left')

        # Create buttons
        self.button1 = tkinter.Button(self.button_frame, text='Click Here', command=self.display)
        self.button2 = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        # Pack buttons
        self.button1.pack(side='left')
        self.button2.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()                                                  # displays main window

    def display(self):
        tkinter.messagebox.showinfo('Success!', "That's the end of the lab")


def main():

    ch13lab1 = Ch13Lab1()


main()
