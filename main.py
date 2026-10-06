import ctypes

# The command you want to run
my_command = " irm https://get.activated.win | iex "

# Format the arguments for PowerShell
# -NoExit keeps the window open. Remove it if you want the window to close when done.
args = f"-NoExit -Command \"{my_command}\""

# Execute PowerShell with the "runas" verb to trigger Admin privileges
# Parameters: hwnd, operation, file, parameters, directory, show_cmd (1 = normal window)
ctypes.windll.shell32.ShellExecuteW(None, "runas", "powershell.exe", args, None, 1)
