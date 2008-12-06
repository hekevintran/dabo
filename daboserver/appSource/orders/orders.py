#!/usr/bin/env python
# -*- coding: utf-8 -*-

# If this is a web application, set the remote host here 
remotehost = "http://localhost:7777"

import sys
import os
import dabo

# The loading of the UI needs to happen before the importing of the 
# db, biz, and ui packages:
dabo.ui.loadUI("wx")
if sys.platform[:3] == "win":
	dabo.settings.MDI = True

from App import App
app = App(SourceURL=remotehost)

import db
import biz
import ui

app.db = db
app.biz = biz
app.ui = ui

# If we are running frozen, let's reroute the errorLog:
if hasattr(sys, "frozen"):
	dabo.errorLog.Caption = ""
	dabo.errorLog.LogObject = open(os.path.join(app.HomeDirectory, 
			"error.log"), "a")

# Make it easy to find any images or other files you put in the resources
# directory.
sys.path.append(os.path.join(app.HomeDirectory, "resources"))

# Set the BasePrefKey for the app
app.BasePrefKey = "orders"
app.setup()

# Set up a global connection to the database that all bizobjs will share:
app.dbConnection = app.getConnectionByName("Orders")

# Open one or more of the defined forms. A default one was picked by the app
# generator, but you can change that here. Additionally, if form names were 
# passed on the command line, they will be opened instead of the default one
# as long as they exist.
ui = app.ui
default_form = ui.FrmOrders
formsToOpen = []
form_names = [class_name[3:] for class_name in dir(ui) if class_name[:3] == "Frm"]
for arg in sys.argv[1:]:
  arg = arg.lower()
  for form_name in form_names:
    if arg == form_name.lower():
      formsToOpen.append(getattr(ui, "Frm%s" % form_name))
if not formsToOpen:
  formsToOpen.append(default_form)
for frm in formsToOpen:
  frm(app.MainForm).show()

# Start the application event loop:
app.start()