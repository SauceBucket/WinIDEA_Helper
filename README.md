# WinIDEA_Helper
This is just a tool to automate some work processes. There is nothing proprietary in this tool to my knowledge. 


VERY IMPORTANT:

Do not attempt to move any folders or files from their original location.
This Folder should be located inside of your copy of the source code, see example here: C:\Users\z004ffaj\"source code folder"\WinIDEA_Helper

If the script starts messing up, let it finish it's current task before you try move your mouse or input anything. 
the reason for this is that if the script gains control of anything other than winidea, unexpected behavior can occur.
Fixing this is outside the scope of the script since this is just supposed to be a quick personal script.

Not As Important:

If you need to get this working on your personal machine, Examine the images folder as the problem is likely there. 
Worst case, you may need to take your own images of the winIDEA icons yourself. I used 125% windows scaling. This setting in in display options.
These will need to be named the same as the existing images, as these are staticly linked.


I didn't want to take the time to make this very configurable due to time constraints. maybe in the future I will if this works on other machines well. 
As a result of this, your winIDEA path must be winIDEA_path = r"C:\iSYSTEM\winIDEA\2012\winIDEA.exe". 
If this is not where your winIDEA is located, then you can fix it by finding the corresponding line in the script.
