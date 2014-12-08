from Tkinter import *
from mainWindow import *


def main():
	root = Tk()
	root.title("Mini Yelp")
	app = mainWindow(root)
	root.mainloop()

if __name__ == '__main__':
	main()