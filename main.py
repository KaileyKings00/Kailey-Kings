#!/usr/bin/env -S uv run --script

import sys

from PySide6.QtCore import QFile
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QColorDialog, QMainWindow, QWidget

from PyNGLScene import PyNGLScene


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui("MainWidget.ui")
        self.setWindowTitle("Firework PyNGL Project  Demo")
        self.resize(1024, 720)

        ##Firework Particle System On the Left Side
        self.scene = PyNGLScene()
        self.centralWidget().layout().addWidget(self.scene, 0, 0, 2, 2)


        ##List of Signals and Slots Function for GUI Controls
        self.restart_button.clicked.connect(self.scene.RestartTime)             #For Restart Button
        self.pause_button.clicked.connect(self.scene.pause)                     #For Pause Button
        self.continue_button.clicked.connect(self.scene.resume)                 #For Continue Button
        self.quit_button.clicked.connect(self.closeEvent)                       #For Quit Button
        self.reset_button.clicked.connect(self.scene.reset)                     #For Resetting Fireworks
        self.speed_numbers.valueChanged.connect(self.scene.set_Particle_Run)    #For Max Speed box
        self.size_numbers.valueChanged.connect(self.scene.set_Particle_Resize)  #For Max Alive box
        self.camera_slider.valueChanged.connect(self.scene.set_Camera_ZoomView) #For Viewport Slider
        self.grow_numbers.valueChanged.connect(self.scene.set_GrowParticle)     #For Max Grow box


    ##Very Challenging Function for QColorDialog Button Palette Control
        self.colour_button.clicked.connect(self.set_ColourDialogs)              #For Colour Palette Box

    def set_ColourDialogs(self):
        color = QColorDialog.getColor()
        if not color.isValid():
            return
        rgb = [
            color.redF(),
            color.greenF(),
            color.blueF(),
        ]
        self.scene.set_ColourPicker(rgb)



    ##Closing the Firework Project Application Test
    def closeEvent(self, event):
        self.close()
        print(f"Firework Window Application Close {self.close}")


    ##Running of UI, QWidget, QApplication for MainWindow
    def load_ui(self, ui_file_name: str) -> None:
        """load ui from a file"""
        try:
            loader = QUiLoader()
            ui_file = QFile(ui_file_name)
            ui_file.open(QFile.ReadOnly)
            loaded_ui = loader.load(ui_file, self)
            self.setCentralWidget(loaded_ui)
            # add all children with object names as attributes of this class
            for child in loaded_ui.findChildren(QWidget):
                name = child.objectName()
                if name:
                    setattr(self, name, child)
            ui_file.close()
        except Exception:
            print(f"Error loading ui file {ui_file_name}")
            raise


def main():
    app = QApplication(sys.argv)
    format = QSurfaceFormat()
    format.setMajorVersion(4)
    format.setMinorVersion(6)
    format.setProfile(QSurfaceFormat.CoreProfile)
    QSurfaceFormat.setDefaultFormat(format)

    print(f"{format.profile()} OpenGL {format.majorVersion()} {format.minorVersion()}")

    try:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Application error {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
