# -*- coding: utf-8 -*-
import wx
import dabo
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
import dabo.dEvents as dEvents
import dabo.dException as dException
from dabo.dLocalize import _, n_
import dControlMixin as dcm


class dStatusBar(dcm.dControlMixin, wx.StatusBar):
	"""Creates a status bar, which displays information to the user.

	The status bar is displayed at the bottom of the form. Add the status bar
	to your form using form.StatusBar=dStatusBar().
	"""
	def __init__(self, parent, properties=None, attProperties=None, *args, **kwargs):
		self._baseClass = dStatusBar
		preClass = wx.PreStatusBar
		dcm.dControlMixin.__init__(self, preClass, parent, properties, attProperties, 
				*args, **kwargs)


	def layout(self):
		""" Wrap the wx version of the call, if possible. """
		self.Layout()
		for child in self.Children:
			try:
				child.layout()
			except AttributeError:
				pass
		try:
			# Call the Dabo version, if present
			self.Sizer.layout()
		except AttributeError:
			pass
		if self._platformIsWindows:
			self.refresh()
		