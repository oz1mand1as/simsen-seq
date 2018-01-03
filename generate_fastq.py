#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generate_fastq.py
#  
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  
#
# Author: Stefan Filges
# Version: 0.1 (2018)
#
#============================// HEADER //===============================
# Libraries
import string
import random as rand
import pandas as pd
import tkFileDialog
import matplotlib as mpl
import os
import sys

if sys.version_info[0] < 3:
   import Tkinter as tk
   from Tkinter import *
else:
   import tkinter as tk

# Usage


# Classes
class application(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.file = Button(self)
        self.file["text"] = "Run",
        self.file["command"] = run_debarcer
        self.file.pack({"side": "left"})
        
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")

        sys.stdout = text_redirector(self.text, "stdout")
        sys.stderr = text_redirector(self.text, "stderr")
        
        # user buttons to select visualization options
         #1 data normalization to largest VAF (all plots have same y-axis)
         #2 colour (yes/no)
         #3 single plot for each amplicon in each file or
           # merge all plots with the same amplicon
         #4 are there replicates? 
            # 4.1 if so, analyze together or separately
   
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

class text_redirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")    

class debarcer(object):
	def select_directory(self):
		print "Choose a directory containing debarcer output files"
		currdir = os.getcwd()
		tempdir = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
		if len(tempdir) > 0:
			print "You chose %s" % tempdir
		print "Running analysis of Debarcer output..."
		return tempdir
		
	def parse_files(self, directory):
		print "Parsing files in %s" % directory
		
		# Find valid files in sub directories
		
		# Save file in list
		
		# Return list of file paths
				
	def select_cons_depth(self):
		# function for the use to select consensus depth to be analyzed
		# options are at least one of: 1, 3, 5, 10, 20, 30
	
		
	def calculate_error(self, files, depths):
		c_depths = depths
		print "Computing error rates for depths %s" % c_depths

class plotting(object):
	# class contains functions for plotting different graphs

# Functions

def usage():
  print "\nThis is the usage function\n"
  print 'Usage: '+sys.argv[0]+' -i <file1> [option]'

# Generate random barcode of 6 characters
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# Generate output files
def run_debarcer():
	# initialize class
	deb = debarcer()
	
	# user selects working directory
	folder = deb.select_directory()
	
	# finding files to use
	files = deb.parse_files(folder)
	
	# user selects depths for which data is to be generated
	depths = deb.select_cons_depth()
	
	# compute error rates and save data into a new output folder
	deb.calculate_error(files, depths) # one results file per input file

# Generate plots for each amplicon in each file indivdually
def generate_plots_ind

# Generate plots for overlaying the same amplicon in all samples
def generate_plots_combined


#=============================// MAIN //================================
          
root = Tk()
app = application(master=root)
app.mainloop()
root.destroy()

	
	
