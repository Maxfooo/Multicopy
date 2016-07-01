'''
Created on Jun 30, 2016

@author: maxr
'''

from tkinter import *
import csv
import xml.etree.ElementTree as ET
from FileIO import FileIO as fIO
import re

class MulticopyUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Multicopy")
        self.pack()
        
    def initUI(self):
        pass
    
    def intiMulticopy(self):
        fio = fIO()
        
        fio.filePrompt("folder", "Please select folder locations to copy to.\n"
                       + "These folder locations will be saved.\n"
                       + "When you are done loading in locations, simply\n" 
                       + "press the cancel button in the file explorer.\n")
        
        try:
            tree = ET.parse('filecopylocations.xml')
            xroot = tree.getroot()
            for locs in xroot.findall('Location'):
                xroot.remove(locs)
        except:
            froot = ET.Element('Directories')
            tree = ET.ElementTree(froot)
            tree.write('filecopylocations.xml')
            tree = ET.parse('filecopylocations.xml')
            xroot = tree.getroot()
    
        locnum = 1
        fio.folderLocation()
        floc = fio.getFolderLocation()
        while(floc != ''):
            try:
                loc = ET.SubElement(xroot, 'Location'.format(locnum))
                loc.set('index', '{0}'.format(locnum))
                locnum = locnum + 1
                loc.text = floc
                floc = fio.getFolderLocation()
            except:
                floc = ''
        
        tree.write('filecopylocations.xml')
        ET.dump(xroot)
    
    def getFileNameFromFilePath(self, fpath):
        return fpath.split('/').pop()
    
    def multicopy():    
        try:
            tree = ET.parse('filecopylocations.xml')
            xroot = tree.getroot()
            print "\nWould you like to edit the following copy desitinations?\n"
            ET.dump(xroot)
            edit = raw_input("\ny=yes : n=no\n")
            if edit == 'y':
                initMulticopy()
            else:
                pass
        except:
            initMulticopy()
            tree = ET.parse('filecopylocations.xml')
            xroot = tree.getroot()
    
        print "\nPlease select the file you wish to have copied."
    
        try:
            
            fcpyfrom = getFileLocation()
            fcpyname = getFileNameFromFilePath(fcpyfrom)
            fcpyfrom = open(fcpyfrom, 'r').read()
            for loc in xroot.findall('Location'):
                f = open(loc.text + '/' + fcpyname, 'w')
                f.write(fcpyfrom)
                f.close()
            print "\nFile was successfully copied!"
        except:
            print "\nCould not copy file!"
            pass
            
            
            
            
            
            
            
            
            
            
            
            
