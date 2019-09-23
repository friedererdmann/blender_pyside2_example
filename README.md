# blender_pyside2_example
Based on Rajiv Sharma's VFX Pipeline video to show Qt in Blender
https://www.youtube.com/watch?v=QYgHyi7jd9c

## What is this?
To better understand the video this is a simplified code example that is aligned with the video of Rajiv Sharma. The Qt tool can now only create new cameras and switch to existing cameras. Everything else is identical to the video (plus some fixes to get Blender to actually load it).

## Notes QT VFX Pipeline video
Whole setup as Addon - in a production put the core.py into modules rather than one specific addon?
Panel in View_3D with Button to launch QT window

## Inner workings
The main content here is the QtWindowEventLoop in core.py, which inherits the Blender operator and sets up modal execution with a QEventLoop that is triggered at 120Hz by Blender.

The actual tool is the CamControllerWindow, which is inheriting the Ui_Form (UI from designer, simplified here) and QDialog

The actual Blender UI element is CamControllerQtPanel (a regular bpy panel), containing the CustomWindowOperator as a UI button. The CustomWindowOperator is a QtWindowEventLoop Operator. It launches the eventloop and the (Qt) CamControllerWindow.

## File structure
    Blender/Addons/Camtools/ (in the video, here: Blender_Pyside2_Example)
        __init__.py
            register and unregister are in here (Blender defaults)
        core.py
            QtEventLoop (this is the most important part)
        gui/
            main.py (Originally this was a Designer UI, now just a simple replacement)
            camController.py (actual Blender Addon code and Qt Window)
        venv/ (in the video, not here)
            Lib/
                site-packages/
                    PySide2
                    shiboken2
            pyvenv.cfg
        

## How to install PySide2 into Blender
    Install Python 3.7 64 bit on system if not done yet
        https://www.python.org/downloads/release/python-370/
    Grab PySide2 via pip in your local Python 3.7 installation
        pip is in %AppData%\Local\Programs\Python\Python37\Scripts
        pip install PySide2
    Copy PySide2 and Shiboken side packages into Blender
        find them in: venv or Python37/Lib/site-packages/
        default path to copy them in Blender: Blender/2.80/python/lib/site-packages/
        (or other path that Blender knows (e.g extend sys.path))
    Copy Python3.dll into the shiboken directory if you're encountering issue
        take from %AppData%\Local\Programs\Python\Python37\python3.dll
        copy to Blender/2.80/python/lib/site-packages/shiboken2/python3.dll (or your alternative location)
