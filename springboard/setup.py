"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import sys
import os
import glob
import dabo
import dabo.icons

DATA_FILES = []
plat = sys.platform
if plat == "darwin":
	# OS X
	OPTIONS = {"argv_emulation": True, "excludes": ["psycopg2", "MySQLdb", "numpy"],
		"iconfile": "springboard.icns"}
elif plat == "win32":
	# Windows
	import py2exe
	OPTIONS = {"excludes": ["psycopg2", "MySQLdb", "numpy", "kinterbasdb"]}


daboDir = os.path.split(dabo.__file__)[0]

# Find the location of the dabo icons:
iconDir = os.path.split(dabo.icons.__file__)[0]
iconSubDirs = []
def getIconSubDir(arg, dirname, fnames):
	if os.path.split(dirname)[1] in (".svn", "cards"):
		return
	icons = glob.glob(os.path.join(dirname, "*.png"))
	if icons:
		subdir = (os.path.join("resources", dirname[len(arg)+1:]), icons)
		iconSubDirs.append(subdir)
os.path.walk(iconDir, getIconSubDir, iconDir)
DATA_FILES.extend(iconSubDirs)

# locales:
localeDir = os.path.join(daboDir, "locale")
locales = []
def getLocales(arg, dirname, fnames):
	if os.path.split(dirname)[1] in (".svn", ):
		return
	mo_files = tuple(glob.glob(os.path.join(dirname, "*.mo")))
	if mo_files:
		subdir = os.path.join("locale", dirname[len(arg)+1:])
		locales.append((subdir, mo_files))
os.path.walk(localeDir, getLocales, localeDir)
DATA_FILES.extend(locales)


# Application files. Include all but .pyc
appDir = os.getcwd()
appFiles = []
def getAppFiles(arg, dirname, fnames):
	if os.path.split(dirname)[1] in (".svn", "supplemental", "test"):
		return
	currnames = glob.glob(os.path.join(dirname, "*"))
	filtered = tuple([nm for nm in currnames 
			if not nm.endswith(".pyc")
			and not os.path.isdir(nm)])
	if filtered:
		subdir = dirname[len(arg)+1:]
		appFiles.append((subdir, filtered))
os.path.walk(appDir, getAppFiles, appDir)
DATA_FILES.extend(appFiles)

setup(
		data_files=DATA_FILES,
		version = "1.0",
		description = "Dabo Springboard",
		name = "dabo_springboard",
		# targets to build
		app = ["main.py"],
		#windows = [{"script": "tweezer.py", "icon_resources": [(0, "tweezer.ico")]}],
		#console = [{"script": "tweezer.py", "icon_resources": [(0, "tweezer.ico")]}],
		options={"py2app": OPTIONS,
			"py2exe": OPTIONS},
)