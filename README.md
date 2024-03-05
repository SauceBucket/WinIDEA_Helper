# WinIDEA_Helper
This is just a tool to automate some work processes. There is nothing proprietary in this tool to my knowledge. 


VERY IMPORTANT:

ENSURE YOUR SCALING SETTING IS SET TO 125%. The resolution I used was 1920x1080, but that should not be important. 
These settings can be found in your windows display options.
Do not attempt to move any folders or files from their original location.
This Folder should be located inside of your copy of the source code, see example here: C:\Users\z004ffaj\atc-main-2\WinIDEA_Helper

If the script starts messing up, let it finish it's current task before you try move your mouse or input anything. 
the reason for this is that if the script gains control of anything other than winidea, unexpected behavior can occur.

Not As Important:

If you need to get this working on your personal machine, Examine the images folder as the problem is likely there. 
Worst case, you may need to take your own images of the winIDEA icons yourself. 
These will need to be named the same as the existing images, as these are staticly linked.


I was too lazy/didn't want to take the time to make this very configurable. maybe in the future I will if this works on other machines well. 
As a result of this, your winIDEA path must be winIDEA_path = r"C:\iSYSTEM\winIDEA\2012\winIDEA.exe". 
If this is not where your winIDEA is located, then you can fix it by finding the corresponding line in the script.