import subprocess
import os
import time
import pygetwindow as gw
import dearpygui as gui
import dearpygui.dearpygui as dpg
from PIL import Image
import pyautogui
import threading
import glob
import sys

#region globals
winidea_title = "winIDEA"
dpg_title = "WinIDEA Timing Helper"
#endregion
log_box_id = None
#region functions
def is_winidea_open():
    try:
        win = gw.getWindowsWithTitle()[0]
        return win.isActive
    except IndexError:
        return False
def find_window(wintitle):
    try:
        all_titles = gw.getAllTitles()
        for title in all_titles:
            if wintitle in title:
                return gw.getWindowsWithTitle(title)[0]  # Return the Window object
        return None
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def activate_window(wintitle):
    try:
        window = find_window(wintitle)
        if window:
            window.activate()
        else:
            raise Exception(r"Timeout: No window with {wintitle} in the title found.")
        time.sleep(.25)   
        pyautogui.click()
        time.sleep(.1) 
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def open_winidea():
    try:
        # Replace 'your_script.ahk' with the path to your AutoHotKey script#TODO hardcode
        winIDEA_path = r"C:\iSYSTEM\winIDEA\2012\winIDEA.exe"
        # Start WinIDEA in the background
        winidea_process = subprocess.Popen([winIDEA_path])

        # Wait for up to 60 seconds for a WinIDEA window to be found
        timeout = 60
        start_time = time.time()
        winidea_window_title = ""

        while not winidea_window_title:
            winidea_window = find_window(winidea_title)

            if winidea_window:
                winidea_window_title = winidea_window.title
                winidea_window.activate()
            elif time.time() - start_time > timeout:
                raise Exception("Timeout: No window with 'winIDEA' in the title found.")

            time.sleep(1)

        # Continue with the rest of your script after finding and activating the WinIDEA window
        print(f"WinIDEA window found and activated with title: {winidea_window_title}")
        
        while winidea_window:
            print("keeping window open")
            time.sleep(20)
            winidea_window = find_window(winidea_title)
        print("window closed")
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def open_winidea_handler():
    try:
        # Create a thread for the callback function
        winIDEA_Thread = threading.Thread(target=open_winidea)

        # Start the thread
        winIDEA_Thread.start()
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def Find_and_Click_Button(imagepath,delay=0, y_offset = 0):
    try:
        # Open the image to be recognized
        image_to_find = Image.open(imagepath)

        # Search for the image on the screen
        location = pyautogui.locateOnScreen(image_to_find)

        #print(location)
        if(location!=None):
            location = (location[0], location[1], location[2], location[3] + y_offset)
            pyautogui.click(location)
            pyautogui.moveTo(10,10)
            time.sleep(delay)
        else:
            print("pyautogui image search failed with image: " + imagepath)
        return location
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def Find_and_Right_Click_Button(imagepath,delay=0, y_offset = 0):
    try:
        # Open the image to be recognized
        image_to_find = Image.open(imagepath)

        # Search for the image on the screen
        location = pyautogui.locateOnScreen(image_to_find)

        #print(location)
        if(location!=None):
            location = (location[0], location[1], location[2], location[3] + y_offset)
            pyautogui.rightClick(location)
            pyautogui.moveTo(10,10)
            time.sleep(delay)
        else:
            print("couldnt find image at: " + imagepath)
        return location
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def Find_and_Enter_695():
    try:
        # Specify the extension you're looking for
        extension = "*.695"

        # Get the path of the parent directory
        parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))

        # Find files in the parent directory with the specified extension
        files_with_extension = glob.glob(os.path.join(parent_directory, extension))

        # Print the list of files
        print("Files with .695 extension in the current directory:")
        if len(files_with_extension)> 1:
            raise Exception("Download_Files: We found too many .695 files!!")
        elif len(files_with_extension) == 1:
            file_path = os.path.abspath(files_with_extension[0])
            print(f"File path to the .695 file: {file_path}")
            pyautogui.typewrite(file_path, interval=0.005)
            for num in range(0,3):
                pyautogui.press("enter")
                time.sleep(.3)
        else:
            raise Exception("Download_Files: We did not find any .695 files!!")
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def Find_and_Enter_Address(address_symbol):
    try:
        extension = "*.map"
        address = ""
        # Get the path of the parent directory
        parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))

        # Find files in the parent directory with the specified extension
        files_with_extension = glob.glob(os.path.join(parent_directory, extension))

        # Print the list of files
        print("Files with .map extension in the current directory:")
        if len(files_with_extension)> 1:
            raise Exception("Download_Files: We found too many .map files!!")
        elif len(files_with_extension) == 1:
            file_path = os.path.abspath(files_with_extension[0])
            print(f"File path to the .map file: {file_path}")
            # Open the file in read mode
            with open(file_path, "r") as file:
                search_string = address_symbol
                # Iterate through each line in the file
                for line_number, line in enumerate(file, 1):  # enumerate starts counting from 1
                # Check if the search string is present in the line
                    if len(line.strip().split()) > 1 and search_string == line.strip().split()[0]:
                        print(f"Found '{search_string}' in line {line_number}: {line.strip()}")
                        split_values  = line.strip().split()
                        # Access the second index (index 1) and prepend "0x"
                        if len(split_values) > 1:
                            address = "0x" + split_values[1]
            print("address is: |" + address)
            pyautogui.typewrite(address, interval=0.005)
        else:
            raise Exception("Download_Files: We did not find any .map files!!")
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def Download_Files(sender,appdata):
    try:
        activate_window(winidea_title)
        
        dpg.configure_item(download_enabled_button, show=False)
        dpg.configure_item(download_disabled_button, show=True)  

        result = Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "debug_ribbon.PNG"), 0.1)
        if(result == None):
            result = Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "debug_ribbon2.PNG"), 0.1)
        if(result == None):
            result = Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "debug_ribbon3.PNG"), 0.1)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Files_For_Download.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "NewFileForDownload.PNG"), 0.2)
        Find_and_Enter_695()
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Finish_Selecting_Files_OK.PNG"),.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Download2.PNG"))

        print("Downloading Files Finished!")   
        dpg.configure_item(download_disabled_button, show=False)
        dpg.configure_item(download_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def BG_Timings(sender,appdata):

    try:
        activate_window(winidea_title)
        dpg.configure_item(timing_BGTasks_enabled_button, show=False)
        dpg.configure_item(timing_BGTasks_disabled_button, show=True)  
        
        EnterAddress("_debugBackGndTaskNum",fetch=False)    
        GetTimings("debugBackGndTaskNum", 1)
        RemoveAddress()

        dpg.configure_item(timing_BGTasks_disabled_button, show=False)
        dpg.configure_item(timing_BGTasks_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")       
def FG_Timings(sender,appdata):
    
    try:
        activate_window(winidea_title)
        dpg.configure_item(timing_FGTasks_enabled_button, show=False)
        dpg.configure_item(timing_FGTasks_disabled_button, show=True)  
        
        EnterAddress("_debugForeGndTaskNum",fetch=False)    
        GetTimings("debugForeGndTaskNum", 1)
        RemoveAddress()

        dpg.configure_item(timing_FGTasks_disabled_button, show=False)
        dpg.configure_item(timing_FGTasks_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def Exec_Timings(sender,appdata):
    
    try:
        activate_window(winidea_title)
        dpg.configure_item(timing_ExecClock_enabled_button, show=False)
        dpg.configure_item(timing_ExecClock_disabled_button, show=True)  
        
        EnterAddress("_execClock", fetch=True)    
        GetTimings("ExecClock", 5)
        RemoveAddress()

        dpg.configure_item(timing_ExecClock_disabled_button, show=False)
        dpg.configure_item(timing_ExecClock_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def GetTimings(name, time_to_sample = 1 ):
    try:
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Analyzer_Start.PNG"))
        analyzer_start_time = time.time()
        while time.time() - analyzer_start_time < time_to_sample:
            time.sleep(.1)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Analyzer_Stop.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "export.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Text_to_CSV.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "CSV.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "EntireSession.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "CSV_Path_TextBox.PNG"), 0.2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        filepath = os.getcwd() + f"\\Timings\\" + name + "_abs.csv"
        pyautogui.typewrite(filepath, interval=0.005)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "CSV_OK.PNG"), 2.0)

        Find_and_Right_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Trigger.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Relative_Time.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "export.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "CSV_Path_TextBox.PNG"), 0.2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        filepath = os.getcwd() + f"\\Timings\\" + name + "_rel.csv"
        pyautogui.typewrite(filepath, interval=0.005)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "CSV_OK.PNG"), 2.0)
        Find_and_Right_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Trigger.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Relative_Time.PNG"), 0.2)

        print("GetTimings Finished")
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def EnterAddress(addr_symbol, fetch = False):
    try:
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "timing_hammer.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "TimingConfigure2.PNG"), 0.2)
        result = Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Address_Enter_Button.PNG"), 0.2)
        if(result == None):
            Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Address_Enter_Button2.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Enter_Address_TextBox.PNG"), 0.2)
        Find_and_Enter_Address(addr_symbol)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Enter_Address_OK.PNG"), 0.2)
        if (fetch):
            Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Control_Add_Button.PNG"), 0.2)
            Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Control_Add_OK.PNG"), 0.2)
        else:
            Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Control_Add_Button.PNG"), 0.2) 
            Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "MemoryWrite.PNG"), 0.2)
            Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Control_Add_OK.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "timing_window_ok.PNG"), 0.3)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "AnalyzerOK.PNG"), 0.2)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def RemoveAddress(fetch=False):
    try:
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "timing_hammer.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "TimingConfigure2.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "AddressBox.PNG"), 0.2, 36)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Address_Remove_Button.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Control_TextBox.PNG"), 0.2,36)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "Control_Remove_Button.PNG"), 0.2)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "timing_window_ok.PNG"), 0.3)
        Find_and_Click_Button(os.path.join(os.getcwd(), "Winidea Icons", "AnalyzerOK.PNG"), 0.2)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def GSTV_Timings(sender,appdata):
    
    try:
        activate_window(winidea_title)
        dpg.configure_item(GSTV_Timings_enabled_button, show=False)
        dpg.configure_item(GSTV_Timings_disabled_button, show=True)  
        
        BG_Timings(sender,appdata)
        FG_Timings(sender,appdata)
        Exec_Timings(sender,appdata)

        print("Finished GSTV Timings!")
        dpg.configure_item(GSTV_Timings_disabled_button, show=False)
        dpg.configure_item(GSTV_Timings_enabled_button, show=True)
        activate_window(dpg_title) 
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def Exec_Timings(sender,appdata):
    try:
        activate_window(winidea_title)
        dpg.configure_item(timing_ExecClock_enabled_button, show=False)
        dpg.configure_item(timing_ExecClock_disabled_button, show=True)  
        
        EnterAddress("_execClock", fetch=True)    
        GetTimings("ExecClock", 5)
        RemoveAddress()

        dpg.configure_item(timing_ExecClock_disabled_button, show=False)
        dpg.configure_item(timing_ExecClock_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def VPS_Timings(sender,appdata):
    try:
        activate_window(winidea_title)
        dpg.configure_item(timing_VPS_enabled_button, show=False)
        dpg.configure_item(timing_VPS_disabled_button, show=True)  
        
        EnterAddress("_manageVPS", fetch=True)    
        GetTimings("manageVPS", 5)
        RemoveAddress()

        dpg.configure_item(timing_VPS_disabled_button, show=False)
        dpg.configure_item(timing_VPS_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def DebugCkSum_Timings(sender,appdata):
    try:
        activate_window(winidea_title)
        dpg.configure_item(timing_DebugCKSum_enabled_button, show=False)
        dpg.configure_item(timing_DebugCKSum_disabled_button, show=True)  
        
        EnterAddress("_debugCksumSegDone",fetch=False)    
        GetTimings("debugCksumSegDone", 8)
        RemoveAddress()

        dpg.configure_item(timing_DebugCKSum_disabled_button, show=False)
        dpg.configure_item(timing_DebugCKSum_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def StackTest_Timings(sender,appdata):
    try:
        activate_window(winidea_title)
        dpg.configure_item(timing_StackTest_enabled_button, show=False)
        dpg.configure_item(timing_StackTest_disabled_button, show=True)  
        
        EnterAddress("_debugStackTestCompleted",fetch=False )    
        GetTimings("debugStackTestCompleted", 5)
        RemoveAddress()

        dpg.configure_item(timing_StackTest_disabled_button, show=False)
        dpg.configure_item(timing_StackTest_enabled_button, show=True)
        activate_window(dpg_title)
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def FSTV_Timings(sender,appdata):
    try:
        activate_window(winidea_title)
        dpg.configure_item(FSTV_Timings_enabled_button, show=False)
        dpg.configure_item(FSTV_Timings_disabled_button, show=True)  
        
        VPS_Timings(sender,appdata)
        DebugCkSum_Timings(sender,appdata)
        StackTest_Timings(sender,appdata)

        print("Finished FSTV Timings!")
        dpg.configure_item(FSTV_Timings_disabled_button, show=False)
        dpg.configure_item(FSTV_Timings_enabled_button, show=True)
        activate_window(dpg_title) 
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def ALL_Timings(sender,appdata):
    try:
        dpg.configure_item(ALL_Timings_enabled_button, show=False)
        dpg.configure_item(ALL_Timings_disabled_button, show=True)  
        
        GSTV_Timings(sender,appdata)
        FSTV_Timings(sender,appdata)

        print("Finished All Timings!")
        dpg.configure_item(ALL_Timings_disabled_button, show=False)
        dpg.configure_item(ALL_Timings_enabled_button, show=True)
        activate_window(dpg_title) 
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")   
def dpg_print(*args, **kwargs):
    # Convert arguments to a string
    output = " ".join(map(str, args))

    # Append the output to the text box
    if log_box_id is not None:
        dpg.set_value(log_box_id, dpg.get_value(log_box_id) +output)
def excepthook(type, value, traceback):
    # Print the uncaught exception to the debug text box
    if log_box_id is not None:
        dpg.set_value(log_box_id, dpg.get_value(log_box_id) + f"Uncaught Exception: {type.__name__} - {str(value)}")

def SetupIOFault(sender,appdata):
    try:
        activate_window(winidea_title)
        EnterAddress("_systemFault",fetch=True)
        EnterAddress("_ioFault",fetch=True)
        EnterAddress("_reset",fetch=True) 
        EnterAddress("_COPCTL",fetch=False)
        EnterAddress("_debugIOFaultArg",fetch=False)
        EnterAddress("_debugIOFaultCode",fetch=False)
        EnterAddress("_debugIOFaultDriver",fetch=False)
        activate_window(dpg_title) 
    except Exception as e:
        # Log the exception to the debug text box
        dpg_print(f"\nException in Find_and_Enter_Address: {str(e)}")      

#endregion










#############################START START START #########################################################################



sys.stdout.write = dpg_print
open_winidea_handler()
time.sleep(2)


dpg.create_context()
dpg.create_viewport(title=dpg_title, width=700, height=500)

with dpg.window(label="WinIDEA Timing Helper",width=700,height=200):
    with dpg.group(horizontal=True, horizontal_spacing=50):
        with dpg.group():
            dpg.add_text("Extras:")
            download_enabled_button = dpg.add_button(label="Download files",callback=Download_Files)
            download_disabled_button = dpg.add_button(label="Downloading Files", callback=lambda s, a: None, show=False)

            ALL_Timings_enabled_button = dpg.add_button(label="Take All Timings",callback=ALL_Timings)
            ALL_Timings_disabled_button = dpg.add_button(label="Taking All Timings", callback=lambda s, a: None, show=False)

            SetupIOFault_enabled_button = dpg.add_button(label="Set Up IOFault Testing",callback=SetupIOFault)
            SetupIOFault_disabled_button = dpg.add_button(label="Setting Up IOFault Testing", callback=lambda s, a: None, show=False)

        with dpg.group():
            dpg.add_text("GSTV:")
            timing_BGTasks_enabled_button = dpg.add_button(label="Take Background Task Timings",callback=BG_Timings)
            timing_BGTasks_disabled_button = dpg.add_button(label="Taking Background Task Timings", callback=lambda s, a: None, show=False)

            timing_FGTasks_enabled_button = dpg.add_button(label="Take Foreground Task Timings",callback=FG_Timings)
            timing_FGTasks_disabled_button = dpg.add_button(label="Taking Foreground Task Timings", callback=lambda s, a: None, show=False)

            timing_ExecClock_enabled_button = dpg.add_button(label="Take ExecClock Timings",callback=Exec_Timings)
            timing_ExecClock_disabled_button = dpg.add_button(label="Taking ExecClock Timings", callback=lambda s, a: None, show=False)

            GSTV_Timings_enabled_button = dpg.add_button(label="Take GSTV Timings",callback=GSTV_Timings)
            GSTV_Timings_disabled_button = dpg.add_button(label="Taking GSTV Timings", callback=lambda s, a: None, show=False)
        with dpg.group():
            dpg.add_text("FSTV:")
            timing_VPS_enabled_button = dpg.add_button(label="Take VPS Timings",callback=VPS_Timings)
            timing_VPS_disabled_button = dpg.add_button(label="Taking VPS Timings", callback=lambda s, a: None, show=False)

            timing_DebugCKSum_enabled_button = dpg.add_button(label="Take DebugCKSum Timings",callback=DebugCkSum_Timings)
            timing_DebugCKSum_disabled_button = dpg.add_button(label="Taking DebugCKSum Task Timings", callback=lambda s, a: None, show=False)

            timing_StackTest_enabled_button = dpg.add_button(label="Take StackTest Timings",callback=StackTest_Timings)
            timing_StackTest_disabled_button = dpg.add_button(label="Taking StackTest Timings", callback=lambda s, a: None, show=False)

            FSTV_Timings_enabled_button = dpg.add_button(label="Take FSTV Timings",callback=FSTV_Timings)
            FSTV_Timings_disabled_button = dpg.add_button(label="Taking FSTV Timings", callback=lambda s, a: None, show=False)

    with dpg.window(horizontal_scrollbar=True,height=250,width=700) as loggerwindow:
        dpg.set_item_pos(loggerwindow,[0,200])
        log_box_id = dpg.add_input_text(multiline=True, readonly=True, height=250,width=700)



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

ahk_script_path = r'C:\Users\z004ffaj\atc-main-2\StartWinidea.Ahk'
ahk_script_path = ahk_directory = r'C:\Program Files\AutoHotkey'
os.environ['PATH'] += os.pathsep + ahk_directory