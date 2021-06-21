This little command line python program has increased my productivity (YMMV) in developing and submitting MVS JCL and programs  stored locally on Linux rather than in MVS TSO, to the Hercules mainframe emulator, I also use it to submit AWSTAPE files (virtual tapes).

I store my JCL and programs (wrapped in JCL) locally on Linux. It creates the proper 'devinit' command for hercules. If the extention is '.aws' (virtual tape), it uses 'devinit 480' otherwise it uses 'devinit 00c'. 

The command is then **automatically placed in your clipboard** ready to be pasted into the Hercules console.

This program assumes that your virtual tapes (AWSTAPE) are stored in the 'tapes' subdirectory of tk4-. But if you store them elsewhere if you just comment out that line.

Obviously using *command completion* can also help in entering filenames.

The program is small and can be placed/run in the directory where your files are in. Or copied where it can run anywhere.../usr/local/bin/toherc on my computer. Make sure permissions set to execute!

The program requires the **pyperclip** cross-platform Python module to copy the command to your clipboard.
