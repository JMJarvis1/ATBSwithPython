import sys
import os
import datetime
import re

launcherVersion = sys.argv[1]
programToLaunch = sys.argv[2]

# Change the cwd to the folder that contains the program
os.chdir(os.path.dirname(programToLaunch))

if "pygame_games/" in programToLaunch:
    print("(On Rapsberry Pis, close this window to shutdown the game.)")

# Technically any Ctrl-C should be caught here, making catching it unnecessary for
# for the .py files unless they aren't run from this computer.

try:
    exitCode = os.system(sys.executable + " " + programToLaunch)
except (KeyboardInterrupt, EOFError):
    exitCode = 0  # Do nothing if Ctrl-C was pressed to exit the game

    # NOTE: We are currently disabling this on macOS because it keeps reporting
    # keyboard interrupts, etc.
    if exitCode != 0 and sys.platform != "darwin":
        # Get the program's __version__ variable:
        with open(programToLaunch) as fo:
            content = fo.read()
            mo = re.search(r"__version__ = (\d)+", content)
            if mo is None:
                programVersion = "N/A"
            else:
                programVersion = mo.group(1)

        sys.stderr.write(f"""
   
* * * * * CRASH DETECTED! * * * * * 

You can help fix this by reporting it. Go to this website:
    https://github.com/asweigart/pythonstdiogames/issues

...andd click the "New Issue" button. (You need a GitHub account to do this.
It is free to sign up. Or, you can email me at al@inventwithpython.com)

NOTE!!! If the error is KeyboardInterrupt, EOFError, or ModuleNotFoundError,
you don't need to report it. Just disregard this message.

In your issue report, copy/paste the above "Traceback" along with this text:
            Program: {programToLaunch}
    Program Version: {programVersion}
   Launcher Version: {launcherVersion}
           Platform: {sys.platform}  
     Python Version: {sys.version}
         Executable: {sys.executable} 
          Timestamp: {datetime.datetime.now()}
          
""")
       
sys.exit(1)  # Exit code of 1 signals to __terminalopener__.py to leave it open even if we are running a Pygame game.
