import tkinter

class Launcher():
    """This should run before the game"""

    def _load_settings(self):
        # TODO
        raise NotImplementedError('What settings are you loading anyways? TODO: make a game with settings')

    def open(self):
        """Open the launcher"""

        root = tkinter.Tk()
        my_label = tkinter.Label(root, text='Itsa me, the launcher!')
        my_label.pack()
        root.mainloop()