#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ToolbarExample:
	def delete_event(self, widget, event=None):
		gtk.main_quit()
		return False
	def radio_event(self, widget, toolbar):
		if self.text_button.get_active():
			toolbar.set_style(gtk.TOOLBAR_TEXT)
		elif self.icon_button.get_active():
			toolbar.set_style(gtk.TOOLBAR_ICONS)
		elif self.both_button.get_active():
			toolbar.set_style(gtk.TOOLBAR_BOTH)
	def toggle_event(self, widget, toolbar):
		toolbar.set_tooltips(widget.get_active())
	def __init__(self):
		dialog = gtk.Dialog()
		dialog.set_title("GTKToolbar Tutorial")
		dialog.set_size_request(450, 250)
		dialog.set_resizable(True)
		
		dialog.connect("delete_event", self.delete_event)
		
		handlebox = gtk.HandleBox()
		dialog.vbox.pack_start(handlebox,False, False, 5)
		
		toolbar = gtk.Toolbar()
		toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
		toolbar.set_style(gtk.TOOLBAR_BOTH)
		toolbar.set_border_width(5)
		handlebox.add(toolbar)
		
		iconw = gtk.Image()
		iconw.set_from_file("gtk.xpm")
		close_button = toolbar.append_item(
			"close",
			"closes this app",
			"private",
			iconw,
			self.delete_event)
		toolbar.append_space()
		
		iconw = gtk.Image()
		iconw.set_from_file("gtk.xpm")
		icon_button = toolbar.append_element(
			gtk.TOOLBAR_CHILD_RADIOBUTTON, # type of element
			None,                          # widget
			"Icon",                        # label
			"Only icons in toolbar",       # tooltip
			"Private",                     # tooltip private string
			iconw,                         # icon
			self.radio_event,              # signal
			toolbar)                       # data for signal
		toolbar.append_space()
		self.icon_button = icon_button
		
		iconw = gtk.Image()
		iconw.set_from_file("gtk.xpm")
		text_button = toolbar.append_element(
			gtk.TOOLBAR_CHILD_RADIOBUTTON, 
			icon_button, 
			"Text",
			"Only texts in toolbar",
			"Private",
			iconw,
			self.radio_event,
			toolbar)
		toolbar.append_space()
		self.text_button = text_button
		
		iconw = gtk.Image()
		iconw.set_from_file("gtk.xpm")
		both_button = toolbar.append_element(
			gtk.TOOLBAR_CHILD_RADIOBUTTON, 
			text_button, 
			"Both", 
			"Icons and text in toolbar", 
			"Private",
			iconw,
			self.radio_event,
			toolbar)
		toolbar.append_space()
		self.both_button = both_button
		both_button.set_active(True)
		
		iconw = gtk.Image()
		iconw.set_from_file("gtk.xpm")
		tooltips_button = toolbar.append_element(
			gtk.TOOLBAR_CHILD_TOGGLEBUTTON,
			None, 
			"Tooltips",
			"Toolbar with or without tips",
			"Private",
			iconw,
			self.toggle_event,
			toolbar)
		toolbar.append_space()
		tooltips_button.set_active(True)
		
		entry = gtk.Entry()
		toolbar.append_widget(entry, "this is just an entry", "Private")
		entry.show()
		
		toolbar.show()
		handlebox.show()
		dialog.show()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	ToolbarExample()
	main()
