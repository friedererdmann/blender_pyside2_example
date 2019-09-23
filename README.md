# blender_pyside2_example
Example to run Qt/PySide2 applications in Blender, based on Rajiv Sharma's VFX Pipeline video:
https://www.youtube.com/watch?v=QYgHyi7jd9c

[![Link to video](https://img.youtube.com/vi/QYgHyi7jd9c/0.jpg)](https://www.youtube.com/watch?v=QYgHyi7jd9c)

## What is the purpose of this repository
This is a simplified version of the code shown in the video of Rajiv Sharma. The intend is to make it easy to follow along and discuss the techniques shown.

The functionality of the Qt tool is now limited to only create new cameras and switch to existing cameras.

All other methods are identical to the video (outside of some fixes to get Blender to load the addon).

## How to install or run this code
Put the whole setup into Blender\addons\blender_pyside2_example or your custom scripts/addons path.

In Blender press N in the viewport, and open the VFXPipeline panel on the side. Press the button in the panel to launch the Qt Application.

*If you haven't installed PySide2 yet, check "How to install Pyside2 into Blender" further down*

## Remarks on structure
* The entire setup is a self contained addon.
  * In actual production, it would make sense to put the core.py contents into a module, rather than one specific addon, so other operators can also inherit from it.

## Inner workings
The main content here is the QtWindowEventLoop in core.py, which inherits the Blender operator and sets up modal execution with a QEventLoop that is triggered at 120Hz by Blender's window manager.

The actual tool is the CamControllerWindow, (originally inheriting the Ui_Form class, created by Qt designer, simplified here) and QDialog.

The only Blender UI element is CamControllerQtPanel (a regular bpy panel), containing the CustomWindowOperator as a UI button. The CustomWindowOperator is a QtWindowEventLoop Operator. It launches the eventloop and the (Qt) CamControllerWindow.

## File structure
```
+ Blender/Addons/Camtools/
|           (Camtools is the name of the addon in the video, here: Blender_Pyside2_Example)
+-- __init__.py
|           register() and unregister() are in here (Blender addon initialization)
+-- core.py
|           QtEventLoop() (this is the most important part)
+-- camController.py
|           The actual Blender Addon code and Qt Window
+-- gui/
|   +-- main.py
|           Originally this was a Designer UI, now just a simple replacement
+-- venv/ (In the video a venv is used, not here)
|   +-- Lib/
|   |   +-- site-packages/
|   |   |   +-- PySide2
|   |   |   +-- shiboken2
|   |   +-- pyvenv.cfg
```     

## How to install PySide2 into Blender
1) Install Python 3.7 64 bit on system if not done yet
   * https://www.python.org/downloads/release/python-370/
2) Grab PySide2 via pip in your local Python 3.7 installation
   * pip is in %AppData%\Local\Programs\Python\Python37\Scripts
   * pip install PySide2
3) Copy PySide2 and Shiboken side packages into Blender
   * find them in: venv or Python37/Lib/site-packages/
   * default path to copy them in Blender: Blender/2.80/python/lib/site-packages/
     * (or other path that Blender knows (e.g extend sys.path))
4) Copy Python3.dll into the shiboken directory if you're encountering issues
   * take from %AppData%\Local\Programs\Python\Python37\python3.dll
   * copy to Blender/2.80/python/lib/site-packages/shiboken2/python3.dll (or your alternative location)

## Special credit
__Rajiv Sharma__ did all the difficult work on this, and graciously shared his knowledge in his VFX Pipeline video (see link at the top of this document). This repository is just to help show how the implementation is done and contains only minor fixes.