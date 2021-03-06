from cx_Freeze import setup, Executable  # cw_Freeze needs to be installed, cmd : pip install cx_freeze
import sys
import os

__author__ = 'Maxim Dumortier'

"""
This program is used to freeze or main.py.
It allows us to make some .exe files or .msi files
To execute it, use the Create_exe.bat and Create_msi.bat files.
"""


build_exe_options = {"packages": ["os", "PS"], "includes" : ["PS"], "include_files":["res"]}

base = None
if sys.platform.startswith('win'):
    base = "Win32GUI"

icon = "./res/PS2DAq.ico"  # Desktop icon

setup(
    name = "(PS)²DAq",

    version = "0.2b",
    
    author = "Cerisic ASBL",

    description = "Python Serial Power Supply Data Acquisition - (PS)²DAq ; Graphical interface to communicate with a power supply in order to acquire some data",

    options = {"build_exe": build_exe_options},

    executables=[Executable("main.py",
                            base=base,
                            targetName = "ps2daq.exe",
                            compress = False,
                            shortcutName="(PS)²DAq",
                            shortcutDir="DesktopFolder",
                            copyDependentFiles = True,
                            icon=icon)],
    )
