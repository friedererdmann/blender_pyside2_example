import os
import bpy
from PySide2 import QtWidgets, QtCore
from . import QtWindowEventLoop
from .gui.main import Ui_Form


class CamControllerWindow(Ui_Form, QtWidgets.QDialog):
    def __init__(self):
        super(CamControllerWindow, self).__init__()
        # self.setupUi(self) # inherited UI method
        self.setWindowTitle('Cam Controller 1.0')
        self.default_camera = ['TOP', 'BOTTOM', 'FRONT', 'BACK']
        self.show()
        self.connect_buttons()

    # only implemented basic methods to show effect

    def connect_buttons(self):
        self.create_camera_PB.clicked.connect(self.create_new_camera)
        self.camera_CB.currentIndexChanged.connect(self.switch_camera)
        self.load_camera()

    def switch_camera(self):
        self.camera_name = self.camera_CB.currentText()
        self.camera_data = self.camera_CB.itemData(self.camera_CB.currentIndex())
        for window in bpy.context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    ctx = bpy.context.copy()
                    ctx['area'] = area
                    ctx['region'] = area.regions[-1]
                    if self.camera_name not in self.default_camera:
                        bpy.ops.view3d.view_camera(ctx)
                        camera_space = area.spaces[0]
                        camera_space.use_local_camera = True
                        camera_space.camera = bpy.data.objects[self.camera_name]
                    else:
                        bpy.ops.view3d.view_axis(ctx, type=self.camera_name)

    def load_camera(self):
        self.camera_CB.clear() # functionality to clear UI element of previous cameras
        scene_camera = bpy.data.cameras
        camera_list = [camera for camera in scene_camera]
        for index, camera in enumerate(camera_list):
            self.camera_CB.insertItem(index, camera.name) # insert each camera at given index
            self.camera_CB.setItemData(index, camera, QtCore.Qt.UserRole) # set connection to data
        self.camera_CB.addItems(self.default_camera) # populate camera list and add default cameras (orthagonals)

    def create_new_camera(self):
        bpy.ops.object.camera_add()
        self.load_camera()

class CustomWindowOperator(QtWindowEventLoop):
    bl_idname = 'screen.custom_window'
    bl_label = 'Cam Controller'

    def __init__(self):
        super().__init__(CamControllerWindow)

class CamControllerQtPanel(bpy.types.Panel):
    bl_label = 'VFX Pipeline' # give credit where credit is due
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'VFX Pipeline'

    '''
    def __init__(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator('screen.custom_window')
    '''
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator('screen.custom_window')

if __name__ == '__main__':
    bpy.utils.register_class(CustomWindowOperator)
    bpy.ops.screen.custom_window() # load the tool upon initializing the addon?