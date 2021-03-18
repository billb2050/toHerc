#!/usr/bin/python3
"""
    This program was created to aid Hercules/MVS development
    locally on Linux, rather than in MVS TSO! I store my JCL and 
    programs (wrapped in JCL) locally on Linux. It creates the proper 
    'devinit' command for hercules. If the extention is '.aws'...
    it uses 'devinit 480' otherwise it uses 'devinit 00c'. 

    The command is then automatically placed in your clipboard ready 
    to be pasted into the Hercules console.
    
    This program assmues that your virtual tapes (AWSTAPE) are stored
    in the 'tapes' subdirectory of tk4-. But if you store them elsewhere
    just comment out that line

    The program is meant to be run in the directory where your files are

    import pyperclip is required to copy command to your clipboard

    By: Bill Blasingim
    On: 10/18/2019

    02/26/2021 Was getting strange errors such as "qt5ct: using qt5ct plugin"
               For some reason I had to..."sudo apt-get install xclip"
    03/08/2021 Allow tape files to be anywhere like job files.
               Don't assume tape files are in Hercules /tapes directory           

"""
import os, string, sys
import pyperclip

if (len(sys.argv)!=2):
    print("Format: toHerc.py filename\n")
    print("This program creates a command in your clipboard")
    print("ready to paste in to the Hercules console.")
    print("This makes it easy to send files to Hercules!")
    sys.exit()
fil=sys.argv[1]
ext=os.path.splitext(fil)
ext=ext[1]
ext=ext.lower()
 
dirpath = os.getcwd()+"/"
if ext==".aws":
    #dirpath = "tapes/"
    cmd="devinit 480 "+dirpath+fil
else:
    cmd="devinit 00c "+dirpath+fil
pyperclip.copy(cmd)
print("Command ready to paste into Hercules console!")
