from PySide6 import QtCore, QtWidgets, QtGui
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui
from . import AdvanceCameraHelperTool_util
import importlib
importlib.reload(AdvanceCameraHelperTool_util)


class MyStylToolDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Advance Camera Helper Tool')
        self.resize(850, 500)
        self.current_camera = None

        # ---------- Base Style ----------
        self.setStyleSheet(self._base_style())

        # ---------- Main Layout ----------
        mainLayout = QtWidgets.QHBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)
        self.setLayout(mainLayout)

        # ---------- Side Menu ----------
        self.sideMenu = QtWidgets.QFrame()
        self.sideMenu.setFixedWidth(80)
        self.sideMenu.setStyleSheet('''
            QFrame {
                border-right: 1px solid #2a2a2a;
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a,
                    stop:1 #2a2a2a
                );
            }
        ''')

        sideLayout = QtWidgets.QVBoxLayout(self.sideMenu)
        sideLayout.setContentsMargins(0, 15, 0, 15)
        sideLayout.setSpacing(20)
        sideLayout.setAlignment(QtCore.Qt.AlignTop)

        # Logo
        logo = QtWidgets.QLabel()
        logo.setPixmap(QtGui.QPixmap(
            "C:/Users/usEr/Documents/maya/2025/scripts/AdvanceCameraHelperTool/icon/logo.png"
        ).scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        logo.setAlignment(QtCore.Qt.AlignHCenter)
        sideLayout.addWidget(logo)

        sideLayout.addSpacing(25)

        ICON_PATH = "C:/Users/usEr/Documents/maya/2025/scripts/AdvanceCameraHelperTool/icon/"

        # Icon Buttons
        self.btn_camera = self._create_icon_button(f"{ICON_PATH}icon01.png", "Camera Creation")
        self.btn_transform = self._create_icon_button(f"{ICON_PATH}icon02.png", "Camera Transform")
        self.btn_shake = self._create_icon_button(f"{ICON_PATH}icon03.png", "Camera Shake")

        sideLayout.addWidget(self.btn_camera)
        sideLayout.addWidget(self.btn_transform)
        sideLayout.addWidget(self.btn_shake)
        sideLayout.addStretch()

        mainLayout.addWidget(self.sideMenu)

        # ---------- Right Main Area ----------
        rightWidget = QtWidgets.QWidget()
        rightLayout = QtWidgets.QVBoxLayout(rightWidget)
        rightLayout.setAlignment(QtCore.Qt.AlignTop)
        rightLayout.setSpacing(10)
        rightLayout.setContentsMargins(20, 20, 20, 20)
        mainLayout.addWidget(rightWidget)

        # ---------- Stacked Widget ----------
        self.stackedWidget = QtWidgets.QStackedWidget()
        rightLayout.addWidget(self.stackedWidget)

        # ---------- Page 1 : Camera Creation ----------
        self.page1 = QtWidgets.QWidget()
        page1Layout = QtWidgets.QVBoxLayout(self.page1)
        page1Layout.setAlignment(QtCore.Qt.AlignCenter)
        page1Layout.setSpacing(10)

        self.HeadNameLabel = QtWidgets.QLabel('Advance Camera Tool')
        self.HeadNameLabel.setStyleSheet("color:white; font-size:22px; font-weight:500;")
        self.CameraCreationNameLabel = QtWidgets.QLabel('Camera Creation')
        self.CameraCreationNameLabel.setStyleSheet("color:#C8C8C8; font-size:16px; font-weight:400;")

        self.CameraNameLineEdit = QtWidgets.QLineEdit()
        self.CameraNameLineEdit.setPlaceholderText("Camera Name")
        self.CameraNameLineEdit.setStyleSheet(self._line_style())
        self.FocalLengthLineEdit = QtWidgets.QLineEdit()
        self.FocalLengthLineEdit.setPlaceholderText("Focal Length")
        self.FocalLengthLineEdit.setStyleSheet(self._line_style())

        self.CreateCameraButton = QtWidgets.QPushButton('Create Camera')
        self.CreateCameraButton.setStyleSheet(self._button_style())

        for w in [self.HeadNameLabel, self.CameraCreationNameLabel,
                  self.CameraNameLineEdit, self.FocalLengthLineEdit,
                  self.CreateCameraButton]:
            page1Layout.addWidget(w, alignment=QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.page1)

        # ---------- Page 2 : Camera Transform ----------
        self.page2 = QtWidgets.QWidget()
        page2Layout = QtWidgets.QVBoxLayout(self.page2)
        page2Layout.setAlignment(QtCore.Qt.AlignCenter)
        page2Layout.setSpacing(10)

        self.CameraMovementLabel = QtWidgets.QLabel('Camera Movement')
        self.CameraMovementLabel.setStyleSheet("color:white; font-size:18px; font-weight:400;")
        page2Layout.addWidget(self.CameraMovementLabel, alignment=QtCore.Qt.AlignCenter)

        sliderLayout = QtWidgets.QHBoxLayout()
        sliderLayout.setSpacing(15)

        # Translate sliders
        translateLayout = QtWidgets.QVBoxLayout()
        translateLayout.setSpacing(5)
        translateLayout.setContentsMargins(10, 5, 10, 5)  # <-- เพิ่ม margin
        self.translateSliders = {}
        for axis in ['X', 'Y', 'Z']:
            label = QtWidgets.QLabel(f'Translate {axis}:')
            label.setStyleSheet("color:#D0D0D0; font-size:14px;")
            slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            slider.setMinimum(-100)
            slider.setMaximum(100)
            slider.setValue(0)
            slider.setStyleSheet(self._slider_style())
            translateLayout.addWidget(label)
            translateLayout.addWidget(slider)
            self.translateSliders[axis] = slider
        sliderLayout.addLayout(translateLayout)

        # Rotation sliders
        rotationLayout = QtWidgets.QVBoxLayout()
        rotationLayout.setSpacing(5)
        rotationLayout.setContentsMargins(10, 5, 10, 5)  # <-- เพิ่ม margin
        self.rotationSliders = {}
        for axis in ['X', 'Y', 'Z']:
            label = QtWidgets.QLabel(f'Rotation {axis}:')
            label.setStyleSheet("color:#D0D0D0; font-size:14px;")
            slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            slider.setMinimum(-180)
            slider.setMaximum(180)
            slider.setValue(0)
            slider.setStyleSheet(self._slider_style())
            rotationLayout.addWidget(label)
            rotationLayout.addWidget(slider)
            self.rotationSliders[axis] = slider
        sliderLayout.addLayout(rotationLayout)
        page2Layout.addLayout(sliderLayout)

        # Buttons under sliders
        self.SetKeyButton = QtWidgets.QPushButton('Set Key Frame')
        self.SetKeyButton.setStyleSheet(self._small_button_style_custom())
        page2Layout.addWidget(self.SetKeyButton, alignment=QtCore.Qt.AlignCenter)

        # Reset Transform Button
        self.ResetButton = QtWidgets.QPushButton('Reset Transform')
        self.ResetButton.setStyleSheet(self._reset_button_style())
        page2Layout.addWidget(self.ResetButton, alignment=QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.page2)

        # ---------- Page 3 : Camera Shake ----------
        self.page3 = QtWidgets.QWidget()
        page3Layout = QtWidgets.QVBoxLayout(self.page3)
        page3Layout.setAlignment(QtCore.Qt.AlignCenter)
        page3Layout.setSpacing(10)

        self.CameraShakeLabel = QtWidgets.QLabel('Camera Shake Generator')
        self.CameraShakeLabel.setStyleSheet("color:white; font-size:18px; font-weight:400;")
        page3Layout.addWidget(self.CameraShakeLabel, alignment=QtCore.Qt.AlignCenter)

        self.IntensityLineEdit = QtWidgets.QLineEdit()
        self.IntensityLineEdit.setPlaceholderText("Intensity")
        self.IntensityLineEdit.setStyleSheet(self._line_style())
        self.StartFrameLineEdit = QtWidgets.QLineEdit()
        self.StartFrameLineEdit.setPlaceholderText("Start Frame")
        self.StartFrameLineEdit.setStyleSheet(self._line_style())
        self.EndFrameLineEdit = QtWidgets.QLineEdit()
        self.EndFrameLineEdit.setPlaceholderText("End Frame")
        self.EndFrameLineEdit.setStyleSheet(self._line_style())

        for w in [self.IntensityLineEdit, self.StartFrameLineEdit, self.EndFrameLineEdit]:
            page3Layout.addWidget(w, alignment=QtCore.Qt.AlignCenter)

        self.ConfirmButton = QtWidgets.QPushButton('Confirm')
        self.ConfirmButton.setStyleSheet(self._small_button_style_custom())
        page3Layout.addWidget(self.ConfirmButton, alignment=QtCore.Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page3)

        # ---------- SIGNALS ----------
        self.CreateCameraButton.clicked.connect(self.create_camera)
        self.SetKeyButton.clicked.connect(self.set_keyframe)
        self.ConfirmButton.clicked.connect(self.on_camera_shake)
        self.ResetButton.clicked.connect(self.reset_transform)

        self.btn_camera.clicked.connect(lambda: self.switch_page(0))
        self.btn_transform.clicked.connect(lambda: self.switch_page(1))
        self.btn_shake.clicked.connect(lambda: self.switch_page(2))

        for s in self.translateSliders.values():
            s.valueChanged.connect(self.update_camera_transform)
        for s in self.rotationSliders.values():
            s.valueChanged.connect(self.update_camera_transform)

        self.switch_page(0)

    # ---------- UI Utility ----------
    def _create_icon_button(self, icon_path, tooltip):
        btn = QtWidgets.QPushButton()
        btn.setToolTip(tooltip)
        btn.setFixedSize(65, 65)
        btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        if QtCore.QFile.exists(icon_path):
            btn.setIcon(QtGui.QIcon(icon_path))
            btn.setIconSize(QtCore.QSize(54, 54))
        else:
            print(f"[Warning] Missing icon: {icon_path}")

        btn.setStyleSheet(self._icon_button_style(False))
        btn.clicked.connect(lambda: self._highlight_button(btn))
        return btn

    def _highlight_button(self, active_btn):
        for btn in [self.btn_camera, self.btn_transform, self.btn_shake]:
            is_active = (btn == active_btn)
            btn.setStyleSheet(self._icon_button_style(is_active))

    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)
        btn_list = [self.btn_camera, self.btn_transform, self.btn_shake]
        for i, btn in enumerate(btn_list):
            btn.setStyleSheet(self._icon_button_style(i == index))

    # ---------- CAMERA LOGIC ----------
    def create_camera(self):
        name = self.CameraNameLineEdit.text() or "MyCamera"
        try:
            focal = float(self.FocalLengthLineEdit.text())
        except ValueError:
            focal = 35
        self.current_camera = utill.create_camera(name, focal)
        self.switch_page(1)

    def update_camera_transform(self):
        if self.current_camera:
            translate = {axis: self.translateSliders[axis].value() for axis in ['X', 'Y', 'Z']}
            rotate = {axis: self.rotationSliders[axis].value() for axis in ['X', 'Y', 'Z']}
            utill.set_camera_transform(self.current_camera, translate, rotate)

    def reset_transform(self):
        for s in self.translateSliders.values():
            s.blockSignals(True)
            s.setValue(0)
            s.blockSignals(False)
        for s in self.rotationSliders.values():
            s.blockSignals(True)
            s.setValue(0)
            s.blockSignals(False)
        if self.current_camera:
            utill.set_camera_transform(self.current_camera,
                                       {'X': 0, 'Y': 0, 'Z': 0},
                                       {'X': 0, 'Y': 0, 'Z': 0})

    def set_keyframe(self):
        if self.current_camera:
            utill.set_keyframe(self.current_camera)

    def on_camera_shake(self):
        if not self.current_camera:
            return
        try:
            intensity = float(self.IntensityLineEdit.text())
        except ValueError:
            intensity = 1.0
        try:
            start = int(self.StartFrameLineEdit.text())
        except ValueError:
            start = 1
        try:
            end = int(self.EndFrameLineEdit.text())
        except ValueError:
            end = start + 24 - 1
        utill.camera_shake(self.current_camera, intensity, start, end)

    # ---------- STYLE ----------
    def _base_style(self):
        return '''
            QWidget {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop:0 #111111,
                    stop:1 #2b2b2b
                );
                color: #E0E0E0;
                font-family: "Segoe UI", "Helvetica Neue", "Arial";
            }
            QFrame { background-color: transparent; }
        '''

    def _line_style(self):
        return '''
            QLineEdit {
                background-color: #222;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 6px 10px;
                color: #EEE;
                font-size: 13px;
            }
            QLineEdit:hover {
                border: 1px solid #666;
                background-color: #292929;
            }
        '''

    def _button_style(self):
        return '''
            QPushButton {
                background-color: #242424;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 8px 18px;
                font-size: 13px;
                color: #E0E0E0;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #2E2E2E;
            }
        '''

    def _small_button_style_custom(self):
        return '''
            QPushButton {
                background-color: #2a2a2a;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 6px 14px;
                color: #EAEAEA;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #333;
            }
        '''

    def _reset_button_style(self):
        return '''
            QPushButton {
                background-color: #3a2922;
                border: 1px solid #664b42;
                border-radius: 6px;
                padding: 6px 14px;
                color: #ffb09a;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #52352e;
                color: #ffd2c2;
            }
        '''

    def _slider_style(self):
        return '''
            QSlider {
                background: transparent;   /* ไม่มีพื้นหลังใด ๆ */
            }
            QSlider::groove:horizontal {
                background: #2A2A2A;
                height: 4px;
                border-radius: 2px;
            }
            QSlider::handle:horizontal {
                background: #666;
                border: 1px solid #777;
                width: 12px;
                border-radius: 6px;
            }
            QSlider::handle:horizontal:hover {
                background: #AAA;
            }
        '''

    def _icon_button_style(self, active):
        if active:
            return '''
                QPushButton {
                    background-color: #2f2f2f;
                    border: 1px solid #555;
                    border-radius: 12px;
                    padding: 4px;
                }
                QPushButton:hover {
                    background-color: #3a3a3a;
                }
            '''
        else:
            return '''
                QPushButton {
                    background-color: transparent;
                    border: none;
                    border-radius: 12px;
                    padding: 4px;
                }
                QPushButton:hover {
                    background-color: #2a2a2a;
                }
            '''


def run():
    global ui
    try:
        ui.close()
    except:
        pass
    ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
    ui = MyStylToolDialog(parent=ptr)
    ui.show()
