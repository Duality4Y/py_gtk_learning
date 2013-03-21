#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class FrameExample:
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Frame Example")
		window.connect("destroy", lambda w: gtk.main_quit())
		window.set_size_request(300, 300)
		window.set_border_width(10)
		
		frame = gtk.Frame()
		window.add(frame)
		frame.set_label("GTK Frame Widget")
		frame.set_label_align(1.0, 0.0)
		frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
		frame.show()
		
		window.show()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	FrameExample()
	main()
