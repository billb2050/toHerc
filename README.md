This little command line python program has greatly increased my productivity in developing and submitting MVS JCL and programs  stored locally on Linux rather than in MVS TSO, to the Hercules mainframe emulator, I also use it to submit AWSTAPE files (virtual tapes).

I store my JCL and programs (wrapped in JCL) locally on Linux. It creates the proper 'devinit' command for hercules. If the extention is '.aws', it uses 'devinit 480' otherwise it uses 'devinit 00c'. 

The command is then **automatically placed in your clipboard** ready to be pasted into the Hercules console.

This program assmues that your virtual tapes (AWSTAPE) are stored in the 'tapes' subdirectory of tk4-. But if you store them elsewhere if you just comment out that line.

Obviously using *command completion* can help in entering filenames.

The program is meant to be run in the directory where your files are in.

The program requires the **pyperclip** cross-platform Python module to copy the command to your clipboard.

By: Bill Blasingim
On: 10/18/2019