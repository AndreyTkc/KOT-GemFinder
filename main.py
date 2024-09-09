import os
import ctypes
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtGui
from main_window_ui import Ui_MainWindow
import cv2
import numpy as np
import pyautogui
import time
import keyboard
from PIL import ImageGrab
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import pathlib
from pathlib import Path
import json


class MainWindow(QMainWindow):
    oldPos = None
    is_enabled = False
    is_taken = False
    is_frozen = False
    data = {
        "file_paths": [],
        "s_key": "",
        "f_key": "",
        "delay": 0.7
    }

    def __init__(self):
        super(MainWindow, self).__init__()
        self.tracking_success_key = False
        self.tracking_false_key = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.thread_pool = QThreadPool()
        self.ui.TipSKey.setHidden(True)
        self.ui.TipFKey.setHidden(True)
        self.ui.TipDelay.setHidden(True)
        self.ui.TipDelayError.setHidden(True)
        self.ui.InfoBtn.setHidden(True)
        self.ui.InfoTip.setHidden(True)
        self.ui.DelayInput.setValidator(QDoubleValidator(0.99, 99.99, 3))
        self.ui.DelayInput.textChanged.connect(self.validate_input)
        # Hint events
        self.ui.SuccessKey.installEventFilter(self)
        self.ui.FalseKey.installEventFilter(self)
        self.ui.DelayInput.installEventFilter(self)
        self.ui.InfoBtn.installEventFilter(self)
        # Close button actions
        self.ui.CloseBtn.clicked.connect(self.close)
        self.ui.CloseBtn.installEventFilter(self)
        # Minimize button actions
        self.ui.MinimizeBtn.clicked.connect(self.showMinimized)
        self.ui.MinimizeBtn.installEventFilter(self)
        # Clear all button action
        self.ui.ClearBtn.clicked.connect(self.clear_all)
        # SuccessKey button action
        self.ui.SuccessKey.clicked.connect(self.set_success_key)
        # FalseKey button action
        self.ui.FalseKey.clicked.connect(self.set_false_key)
        # Save  button action
        self.ui.SaveBtn.clicked.connect(self.save_data)
        # Start  button action
        self.ui.StartBtn.clicked.connect(self.on_start_clicked)
        # Stop  button action
        self.ui.StopBtn.clicked.connect(self.stop)
        # Remove button actions
        self.ui.RemoveBtn1.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn1))
        self.ui.RemoveBtn2.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn2))
        self.ui.RemoveBtn3.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn3))
        self.ui.RemoveBtn4.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn4))
        self.ui.RemoveBtn5.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn5))
        self.ui.RemoveBtn6.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn6))
        self.ui.RemoveBtn7.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn7))
        self.ui.RemoveBtn8.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn8))
        self.ui.RemoveBtn9.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn9))
        self.ui.RemoveBtn10.clicked.connect(lambda: self.remove_position(self.ui.RemoveBtn10))
        # Add file button actions
        self.ui.Add1.clicked.connect(lambda: self.add_file(self.ui.Add1))
        self.ui.Add2.clicked.connect(lambda: self.add_file(self.ui.Add2))
        self.ui.Add3.clicked.connect(lambda: self.add_file(self.ui.Add3))
        self.ui.Add4.clicked.connect(lambda: self.add_file(self.ui.Add4))
        self.ui.Add5.clicked.connect(lambda: self.add_file(self.ui.Add5))
        self.ui.Add6.clicked.connect(lambda: self.add_file(self.ui.Add6))
        self.ui.Add7.clicked.connect(lambda: self.add_file(self.ui.Add7))
        self.ui.Add8.clicked.connect(lambda: self.add_file(self.ui.Add8))
        self.ui.Add9.clicked.connect(lambda: self.add_file(self.ui.Add9))
        self.ui.Add10.clicked.connect(lambda: self.add_file(self.ui.Add10))

        self.resize(800, 600)

        self.round_corners(10)

        self.get_data()

    def round_corners(self, radius):
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        path.addRoundedRect(rect, radius, radius)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    def validate_input(self):
        self.ui.TipDelayError.setHidden(True)
        text = self.ui.DelayInput.text()
        if text.startswith(",") or text.startswith("."):
            self.ui.DelayInput.setText("")
            self.ui.TipDelayError.setHidden(False)
            return
        elif "e" in text:
            self.ui.DelayInput.setText(text.replace("e", ""))

    def eventFilter(self, obj, ev):
        global is_taken
        global data
        if obj == self.ui.CloseBtn:
            if ev.type() == QEvent.Enter:
                icon = QIcon()
                icon.addFile(":/Close/icons/close_hover.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
                self.ui.CloseBtn.setIcon(icon)
                self.ui.CloseBtn.setIconSize(QSize(20, 20))
            elif ev.type() == QEvent.Leave:
                icon = QIcon()
                icon.addFile(":/Close/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
                self.ui.CloseBtn.setIcon(icon)
                self.ui.CloseBtn.setIconSize(QSize(20, 20))
        elif obj == self.ui.MinimizeBtn:
            if ev.type() == QEvent.Enter:
                icon = QIcon()
                icon.addFile(":/Minimize/icons/minimize_hover.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
                self.ui.MinimizeBtn.setIcon(icon)
                self.ui.MinimizeBtn.setIconSize(QSize(20, 20))
            elif ev.type() == QEvent.Leave:
                icon = QIcon()
                icon.addFile(":/Minimize/icons/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
                self.ui.MinimizeBtn.setIcon(icon)
                self.ui.MinimizeBtn.setIconSize(QSize(20, 20))
        elif obj == self.ui.SuccessKey and self.is_frozen:
            if ev.type() == QEvent.Enter:
                self.ui.TipSKey.setHidden(False)
            elif ev.type() == QEvent.Leave:
                self.ui.TipSKey.setHidden(True)
        elif obj == self.ui.FalseKey and self.is_frozen:
            if ev.type() == QEvent.Enter:
                self.ui.TipFKey.setHidden(False)
            elif ev.type() == QEvent.Leave:
                self.ui.TipFKey.setHidden(True)
        elif obj == self.ui.InfoBtn:
            if ev.type() == QEvent.Enter:
                self.ui.InfoTip.setHidden(False)
            elif ev.type() == QEvent.Leave:
                self.ui.InfoTip.setHidden(True)
        elif obj == self.ui.DelayInput and not self.is_frozen:
            self.is_taken = True
            if ev.type() == QEvent.Enter:
                self.ui.TipDelay.setHidden(False)
            elif ev.type() == QEvent.Leave:
                self.ui.TipDelay.setHidden(True)
            elif ev.type() == QEvent.FocusIn:
                self.is_taken = True
            elif ev.type() == QEvent.FocusOut:
                if self.ui.DelayInput.text() in ["0,", "0,00", "0,000", "00,0", "000,0", "00,00", "0.", "0.00",
                                                 "0.000", "00.0", "000.0", "00.00"]:
                    self.ui.DelayInput.setText("0")
                    self.data["delay"] = 0
                    return False
                elif self.ui.DelayInput.text() in ["0"]:
                    if self.ui.DelayInput.text().lstrip('0') == "":
                        self.ui.DelayInput.setText("0")
                        self.data["delay"] = 0
                        return False
                elif self.ui.DelayInput.text() == "":
                    self.ui.DelayInput.setText("")
                    self.data["delay"] = 0.7
                    self.ui.DelayInput.clearFocus()
                    self.ui.TipDelayError.setHidden(True)
                    return False
                self.update_status()
                self.is_taken = False
            elif ev.type() == QEvent.KeyPress:
                key = ev.key()
                if key == Qt.Key_Escape or key == Qt.Key_Enter or key == Qt.Key_Return:
                    if self.ui.DelayInput.text() in ["0,", "0,00", "0,000", "00,0", "000,0", "00,00", "0.", "0.00",
                                                     "0.000", "00.0", "000.0", "00.00"]:
                        self.ui.DelayInput.setText("0")
                        self.data["delay"] = 0
                        return False
                    elif self.ui.DelayInput.text() in ["0"]:
                        if self.ui.DelayInput.text().lstrip('0') == "":
                            self.ui.DelayInput.setText("0")
                            self.data["delay"] = 0
                            return False
                    elif self.ui.DelayInput.text() == "":
                        self.ui.DelayInput.setText("")
                        self.data["delay"] = 0.7
                        self.ui.DelayInput.clearFocus()
                        self.ui.TipDelayError.setHidden(True)
                        return False
                    self.update_status()
                    self.is_taken = False
        return False

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and not self.is_taken:
            self.oldPos = event.globalPos()
        elif event.button() == Qt.MouseButton.LeftButton and self.is_taken:
            if self.ui.DelayInput.text() in ["0,", "0,00", "0,000", "00,0", "000,0", "00,00", "0.", "0.00",
                                             "0.000", "00.0", "000.0", "00.00"]:
                self.ui.DelayInput.setText("0")
                self.data["delay"] = 0
                return False
            elif self.ui.DelayInput.text() in ["0"]:
                if self.ui.DelayInput.text().lstrip('0') == "":
                    self.ui.DelayInput.setText("0")
                    self.data["delay"] = 0
                    return False
            elif self.ui.DelayInput.text() == "":
                self.ui.DelayInput.setText("")
                self.data["delay"] = 0.7
                self.ui.DelayInput.clearFocus()
                self.ui.TipDelayError.setHidden(True)
                return False
            self.update_status()
            self.ui.DelayInput.clearFocus()
            self.is_taken = False
        return False

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()
        return False

    def mouseReleaseEvent(self, event):
        self.oldPos = None

    def add_file(self, object):
        global data
        self.file_path = ""
        self.file_name = ""
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Pictures (*.png *.jpg *.jpeg)")
        if file_dialog.exec():
            self.file_path = str(file_dialog.selectedFiles()[0])
            self.file_name = self.file_path.split("/")[-1]
            if (os.stat(self.file_path)).st_size > 10000000:
                ctypes.windll.user32.MessageBoxW(0, "The file size cannot be larger than 10 MB.", "Error", 0x10)
                return False
            self.data["file_paths"].append(self.file_path)
            if object == self.ui.Add10:
                self.object_number = str(object.objectName())[-2:]
            else:
                self.object_number = str(object.objectName())[-1]
            self.add_button = f"Add{self.object_number}"
            self.path_label = f"Path{self.object_number}"
            self.remove_button = f"RemoveBtn{self.object_number}"
            getattr(self.ui, self.add_button).setText(self.file_name)
            getattr(self.ui, self.path_label).setText(self.file_path)
            icon = QIcon()
            icon.addFile(u":/Remove/icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            getattr(self.ui, self.remove_button).setIcon(icon)
            getattr(self.ui, self.remove_button).setIconSize(QSize(15, 15))
            getattr(self.ui, self.remove_button).setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            getattr(self.ui, self.remove_button).setEnabled(True)
            self.object_number = int(self.object_number)
            if self.object_number < 10:
                self.object_number += 1
                self.next_add_button = f"Add{self.object_number}"
                getattr(self.ui, self.next_add_button).setEnabled(True)
            if self.data["s_key"] != "" and self.data["f_key"] != "":
                self.ui.StartBtn.setEnabled(True)

    def remove_position(self, object):
        global file_paths
        if object == self.ui.RemoveBtn10:
            self.object_number = str(object.objectName())[-2:]
        else:
            self.object_number = str(object.objectName())[-1]
        self.add_button = f"Add{self.object_number}"
        self.path_label = f"Path{self.object_number}"
        self.remove_button = f"RemoveBtn{self.object_number}"
        self.data["file_paths"].pop(int(self.object_number) - 1)
        getattr(self.ui, self.add_button).setText("Add...")
        getattr(self.ui, self.path_label).setText("")
        getattr(self.ui, self.remove_button).setIcon(QIcon())
        getattr(self.ui, self.remove_button).setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.arrange_positions_in_grid(self.add_button, self.path_label, self.remove_button, self.object_number)

    def arrange_positions_in_grid(self, add_button, path_label, remove_button, object_number):
        self.object_number = int(object_number)
        for i in range(self.object_number, 10):
            self.next_row = i + 1

            self.current_add_button = f"Add{self.object_number}"
            self.current_path_label = f"Path{self.object_number}"
            self.current_remove_button = f"RemoveBtn{self.object_number}"
            self.next_add_button = f"Add{self.next_row}"
            self.next_path_label = f"Path{self.next_row}"
            self.next_remove_button = f"RemoveBtn{self.next_row}"
            self.next_add_button_text = getattr(self.ui, self.next_add_button).text()
            self.next_path_label_text = getattr(self.ui, self.next_path_label).text()

            if self.next_add_button_text == "Add...":
                break

            getattr(self.ui, self.current_add_button).setText(self.next_add_button_text)
            getattr(self.ui, self.current_path_label).setText(self.next_path_label_text)
            icon = QIcon()
            icon.addFile(u":/Remove/icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            getattr(self.ui, self.current_remove_button).setIcon(icon)
            getattr(self.ui, self.current_remove_button).setIconSize(QSize(15, 15))
            getattr(self.ui, self.current_remove_button).setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            getattr(self.ui, self.next_remove_button).setIcon(QIcon())
            getattr(self.ui, self.next_remove_button).setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            getattr(self.ui, self.next_add_button).setText("Add...")
            getattr(self.ui, self.next_path_label).setText("")

            self.object_number += 1
        for k in range(1, 11):
            self.current_add_button_state = f"Add{k}"
            self.after_add_button_state = f"Add{k + 1}"
            self.current_remove_button_state = f"RemoveBtn{k}"
            self.after_remove_button_state = f"RemoveBtn{k + 1}"
            self.current_add_button_text = getattr(self.ui, self.current_add_button_state).text()
            if self.current_add_button_text == "Add...":
                getattr(self.ui, self.current_remove_button_state).setEnabled(False)
                if k < 10:
                    getattr(self.ui, self.after_remove_button_state).setEnabled(False)
                    getattr(self.ui, self.after_add_button_state).setEnabled(False)
                break

    def clear_all(self):
        for i in range(1, 11):
            self.add_button = f"Add{i}"
            self.path_label = f"Path{i}"
            self.remove_button = f"RemoveBtn{i}"

            getattr(self.ui, self.remove_button).setIcon(QIcon())
            getattr(self.ui, self.remove_button).setCursor(QCursor(Qt.CursorShape.ArrowCursor))
            getattr(self.ui, self.remove_button).setEnabled(False)
            getattr(self.ui, self.add_button).setText("Add...")
            getattr(self.ui, self.path_label).setText("")
            if i != 1:
                getattr(self.ui, self.add_button).setEnabled(False)
        self.data["file_paths"] = []
        self.ui.StartBtn.setEnabled(False)

    def set_success_key(self):
        self.tracking_success_key = True
        self.ui.SuccessKey.setText("...")

    def set_false_key(self):
        self.tracking_false_key = True
        self.ui.FalseKey.setText("...")

    def keyPressEvent(self, event):
        global data
        if self.tracking_success_key:
            if event.type() == QEvent.KeyPress:
                key = event.key()
                key_text = event.text()

                if key == Qt.Key_Escape:
                    self.ui.SuccessKey.setText("")
                    self.data["s_key"] = ""
                else:
                    if key_text:
                        self.ui.SuccessKey.setStyleSheet(u"#SuccessKey {\n"
                                                    "background-color: rgba(0, 0, 0, 0.4);\n"
                                                    "border-radius: 8px;\n"
                                                    "font: 12pt \"Sitka\";\n"
                                                    "}\n"
                                                    "#SuccessKey:hover {\n"
                                                    "background-color: rgba(0, 0, 0, 0.25);\n"
                                                    "}")
                        self.ui.SuccessKey.setText(key_text.upper())
                        self.data["s_key"] = key_text.upper()
                        self.update_status()
                    else:
                        self.ui.SuccessKey.setStyleSheet(u"#SuccessKey {\n"
                                                    "background-color: rgba(0, 0, 0, 0.4);\n"
                                                    "border-radius: 8px;\n"
                                                    "font: 8pt \"Sitka\";\n"
                                                    "}\n"
                                                    "#SuccessKey:hover {\n"
                                                    "background-color: rgba(0, 0, 0, 0.25);\n"
                                                    "}")
                        self.ui.SuccessKey.setText(QKeySequence(key).toString())
                        self.data["s_key"] = QKeySequence(key).toString()
                        self.update_status()
                self.tracking_success_key = False
        elif self.tracking_false_key:
            if event.type() == QEvent.KeyPress:
                key = event.key()
                key_text = event.text()

                if key == Qt.Key_Escape:
                    self.ui.FalseKey.setText("")
                    self.data["f_key"] = ""
                else:
                    if key_text:
                        self.ui.FalseKey.setStyleSheet(u"#FalseKey {\n"
                                                    "background-color: rgba(0, 0, 0, 0.4);\n"
                                                    "border-radius: 8px;\n"
                                                    "font: 12pt \"Sitka\";\n"
                                                    "}\n"
                                                    "#FalseKey:hover {\n"
                                                    "background-color: rgba(0, 0, 0, 0.25);\n"
                                                    "}")
                        self.ui.FalseKey.setText(key_text.upper())
                        self.data["f_key"] = key_text.upper()
                        self.update_status()
                    else:
                        self.ui.FalseKey.setStyleSheet(u"#FalseKey {\n"
                                                    "background-color: rgba(0, 0, 0, 0.4);\n"
                                                    "border-radius: 8px;\n"
                                                    "font: 8pt \"Sitka\";\n"
                                                    "}\n"
                                                    "#FalseKey:hover {\n"
                                                    "background-color: rgba(0, 0, 0, 0.25);\n"
                                                    "}")
                        self.ui.FalseKey.setText(QKeySequence(key).toString())
                        self.data["f_key"] = QKeySequence(key).toString()
                        self.update_status()
                self.tracking_false_key = False

    def on_start_clicked(self):
        global is_enabled
        if not self.is_enabled:
            self.is_enabled = True
            self.thread_pool.start(self.start)

    def save_data(self):
        self.file_path = Path.home() / "AppData" / "Local" / "KOT Gem Finder"
        pathlib.Path(self.file_path).mkdir(parents=True, exist_ok=True)
        self.file_path = Path.home() / "AppData" / "Local" / "KOT Gem Finder" / "settings.json"
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)
            self.thread_pool.start(self.change_icon)

    def change_icon(self):
        icon = QIcon()
        icon.addFile(u":/Done/icons/done.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ui.SaveBtn.setIcon(icon)
        self.ui.SaveBtn.setText("Saved!")
        time.sleep(2)
        self.ui.SaveBtn.setIcon(QIcon())
        self.ui.SaveBtn.setText("Save")

    def get_data(self):
        global data

        self.folder_path = Path.home() / "AppData" / "Local" / "KOT Gem Finder"
        self.folder_path.mkdir(parents=True, exist_ok=True)

        self.file_path = self.folder_path / "settings.json"

        if not self.file_path.exists():
            self.file_path.touch()

        try:
            with open(self.file_path, 'r') as f:
                self.file_content = f.read().strip()
                if self.file_content:
                    self.data = json.loads(self.file_content)
                else:
                    self.data["file_paths"] = []
        except json.JSONDecodeError:
            self.data["file_paths"] = []

        self.fill_grid()
        self.set_keys()

        self.update_status()

    def fill_grid(self):
        self.i = 0
        for file_path in self.data["file_paths"]:
            self.add_button = f"Add{self.i + 1}"
            self.next_add_button = f"Add{self.i + 2}"
            self.path_label = f"Path{self.i + 1}"
            self.remove_button = f"RemoveBtn{self.i + 1}"
            self.file_name = self.data["file_paths"][self.i].split("/")[-1]
            getattr(self.ui, self.add_button).setText(self.file_name)
            getattr(self.ui, self.path_label).setText(self.data["file_paths"][self.i])
            icon = QIcon()
            icon.addFile(u":/Remove/icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            getattr(self.ui, self.remove_button).setIcon(icon)
            getattr(self.ui, self.remove_button).setIconSize(QSize(15, 15))
            getattr(self.ui, self.remove_button).setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            getattr(self.ui, self.remove_button).setEnabled(True)
            if self.i < 9:
                getattr(self.ui, self.next_add_button).setEnabled(True)
            self.i += 1

    def set_keys(self):
        self.ui.SuccessKey.setText(self.data["s_key"].upper())
        self.ui.FalseKey.setText(self.data["f_key"].upper())
        self.ui.DelayInput.setText(str(self.data["delay"]))

    def update_status(self):
        if self.data["file_paths"] and self.data["s_key"] != "" and self.data[
            "f_key"] != "" and self.data["delay"] >= 0:
            self.ui.StartBtn.setEnabled(True)

    def start(self):
        global is_frozen
        self.is_frozen = True
        self.ui.StartBtn.setEnabled(False)
        self.ui.StopBtn.setEnabled(True)
        self.ui.InfoBtn.setHidden(False)
        for i in range(1, 11):
            self.add_button = f"Add{i}"
            self.remove_button = f"RemoveBtn{i}"
            getattr(self.ui, self.add_button).setEnabled(False)
            getattr(self.ui, self.remove_button).setEnabled(False)
        self.ui.ClearBtn.setEnabled(False)
        self.ui.SaveBtn.setEnabled(False)
        self.ui.SuccessKey.setEnabled(False)
        self.ui.FalseKey.setEnabled(False)
        self.ui.DelayInput.setEnabled(False)
        while self.is_enabled:
            self.window_title = str(pyautogui.getActiveWindowTitle())
            for file_path in self.data["file_paths"]:
                self.image = cv2.imread(file_path)
                if self.image is None:
                    ctypes.windll.user32.MessageBoxW(0,
                                                     "Failed to open/read file: check path or file integrity.",
                                                     "Error", 0x10)
                    self.stop()
                    return False
            else:
                if self.window_title == "Gem Finder":
                    time.sleep(2)
                else:
                    self.match_threshold = 0.9

                    time.sleep(self.data["delay"])

                    self.start_time = time.time()

                    self.found = self.find_any_image_on_screen(self.data["file_paths"], self.match_threshold)

                    self.end_time = time.time()
                    self.elapsed_time = self.end_time - self.start_time
                    self.current_time = datetime.now().strftime("%H:%M:%S")

                    if self.found:
                        print(f"Golden gem found! [{self.current_time}]   Search time: {self.elapsed_time:.2f} seconds")
                        pyautogui.press((self.data["s_key"]).lower())
                        time.sleep(0.5)
                        self.stop()
                        return False
                    else:
                        print(f"Skip... [{self.current_time}]   Search time: {self.elapsed_time:.2f} seconds")
                        pyautogui.press((self.data["f_key"]).lower())

    def stop(self):
        global is_enabled
        global is_frozen
        if self.is_enabled:
            self.is_enabled = False
        elif self.is_frozen:
            self.is_frozen = True
        self.ui.StartBtn.setEnabled(True)
        self.ui.StopBtn.setEnabled(False)
        self.ui.ClearBtn.setEnabled(True)
        self.ui.SaveBtn.setEnabled(True)
        self.ui.SuccessKey.setEnabled(True)
        self.ui.FalseKey.setEnabled(True)
        self.ui.DelayInput.setEnabled(True)
        self.ui.InfoBtn.setHidden(True)

        self.i = 0
        for file_path in self.data["file_paths"]:
            self.add_button = f"Add{self.i + 1}"
            self.next_add_button = f"Add{self.i + 2}"
            self.remove_button = f"RemoveBtn{self.i + 1}"
            getattr(self.ui, self.add_button).setEnabled(True)
            getattr(self.ui, self.remove_button).setEnabled(True)
            if self.i < 9:
                getattr(self.ui, self.next_add_button).setEnabled(True)
            self.i += 1

    def find_image_on_screen(self, template, screenshot, threshold):
        self.res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        self.loc = np.where(self.res >= threshold)
        return self.loc[0].size > 0

    def find_any_image_on_screen(self, template_paths, threshold):
        self.screenshot = ImageGrab.grab()
        self.screenshot = cv2.cvtColor(np.array(self.screenshot), cv2.COLOR_BGR2GRAY)

        with ThreadPoolExecutor() as executor:
            self.futures = []
            for template_path in template_paths:
                self.template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
                self.futures.append(executor.submit(self.find_image_on_screen, self.template, self.screenshot, threshold))

            for future in self.futures:
                if future.result():
                    return True

        return False


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
