#!/usr/bin/env pyton

import pygtk
pygtk.require('2.0')
import gtk

class Labels:
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", lambda w: gtk.main_quit())
		
		self.window.set_title("Label")
		vbox = gtk.VBox(False, 5)
		hbox = gtk.HBox(False, 5)
		self.window.add(hbox)
		hbox.pack_start(vbox, False, False, 0)
		self.window.set_border_width(5)
		
		frame = gtk.Frame("Normal Label")
		label = gtk.Label("This is a normal label")
		frame.add(label)
		vbox.pack_start(frame, False, False, 0)
		
		frame = gtk.Frame("multi line label")
		label = gtk.Label("this is a multi-line labe.\nsecond line\n""third line")
		
		frame.add(label)
		vbox.pack_start(frame, False, False, 0)
		
		frame = gtk.Frame("Left justfied label")
		label = gtk.Label("this is a left-justified\n""multi-line label.\nThird      Line")
		label.set_justify(gtk.JUSTIFY_LEFT)
		frame.add(label)
		vbox.pack_start(frame, False, False, 0)
		
		frame = gtk.Frame("right jusified label")
		label = gtk.Label("this a right justified\n""multiline labe.\nthird      line")
		label.set_justify(gtk.JUSTIFY_RIGHT)
		frame.add(label)
		vbox.pack_start(frame, False, False, 0)
		
		vbox = gtk.VBox(False, 5)
		hbox.pack_start(vbox, False, False, 0)
		frame = gtk.Frame("line wraped label")
		label = gtk.Label("this is an example of a line wraped label. it"
							"should not be taking up the entire"
							"width allocated to it but automaticlly"
							"wraps the words to fit."
							"the time has com for al good men to com to"
							"the ait of their party"
							"the sixth sheik's six sheeps sick.\n"
							"it support multipl paragraphs correctly"
							"and correctly adds "
							"many     extra   spaces.")
		label.set_line_wrap(True)
		frame.add(label)
		vbox.pack_start(frame, False, False, 0)
		
		frame = gtk.Frame("filled, wrapped label")
		label = gtk.Label("This is an example of a line-wrapped, filled label.  "
							"It should be taking "
							"up the entire              width allocated to it.  "
							"Here is a sentence to prove "
							"my point.  Here is another sentence. "
							"Here comes the sun, do de do de do.\n"
							"    This is a new paragraph.\n"
							"    This is another newer, longer, better "
							"paragraph.  It is coming to an end, "
							"unfortunately.")
		label.set_justify(gtk.JUSTIFY_FILL)
		label.set_line_wrap(True)
		frame.add(label)
		vbox.pack_start(frame, False, False, 0)
		
		frame = gtk.Frame("under line label")
		label = gtk.Label("this labe is underlined!\n""this one is underlined in a funky fashion")
		label.set_justify(gtk.JUSTIFY_LEFT)
		label.set_pattern("________________________ _ _________ _____      ____    ______  __ ___")
		frame.add(label)
		vbox.pack_start(frame, False, False, 0)
		self.window.show_all()
def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	Labels()
	main()
