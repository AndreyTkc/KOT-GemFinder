# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/WindowIcon/icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.023, y1:0, x2:0.995, y2:1, stop:0.0140845 rgba(53, 55, 84, 255), stop:0.507042 rgba(81, 81, 124, 255));\n"
"font-family: Montserrat;\n"
"border-radius: 10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ClearBtn = QPushButton(self.centralwidget)
        self.ClearBtn.setObjectName(u"ClearBtn")
        self.ClearBtn.setGeometry(QRect(10, 500, 161, 31))
        self.ClearBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ClearBtn.setStyleSheet(u"#ClearBtn {\n"
"background-color: rgba(0, 0, 0, 0.3);\n"
"border-radius: 8px;\n"
"font: 8pt \"Sitka\";\n"
"}\n"
"#ClearBtn:hover {\n"
"background-color: rgba(0, 0, 0, 0.2);\n"
"}\n"
"#ClearBtn:pressed {\n"
"background-color: rgba(0, 0, 0, 0.5);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Remove/icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ClearBtn.setIcon(icon1)
        self.StartBtn = QPushButton(self.centralwidget)
        self.StartBtn.setObjectName(u"StartBtn")
        self.StartBtn.setEnabled(False)
        self.StartBtn.setGeometry(QRect(550, 550, 115, 35))
        self.StartBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.StartBtn.setStyleSheet(u"#StartBtn {\n"
"background-color: rgba(0, 0, 0, 0.5);\n"
"border-radius: 8px;\n"
"font: 10pt \"Sitka\";\n"
"}\n"
"#StartBtn:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#StartBtn:pressed {\n"
"background-color: rgba(0, 0, 0, 0.7);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Start/icons/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StartBtn.setIcon(icon2)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 120, 780, 371))
        self.widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.15);\n"
"border-radius: 8px;\n"
"font: 8pt \"Sitka\";")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Add3 = QPushButton(self.widget)
        self.Add3.setObjectName(u"Add3")
        self.Add3.setEnabled(False)
        self.Add3.setMinimumSize(QSize(150, 20))
        self.Add3.setMaximumSize(QSize(150, 20))
        self.Add3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add3.setStyleSheet(u"#Add3 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add3:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add3:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add3, 3, 0, 1, 1)

        self.RemoveBtn5 = QPushButton(self.widget)
        self.RemoveBtn5.setObjectName(u"RemoveBtn5")
        self.RemoveBtn5.setEnabled(False)
        self.RemoveBtn5.setMinimumSize(QSize(20, 20))
        self.RemoveBtn5.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn5, 5, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Path9 = QLabel(self.widget)
        self.Path9.setObjectName(u"Path9")

        self.gridLayout.addWidget(self.Path9, 9, 1, 1, 1)

        self.Path10 = QLabel(self.widget)
        self.Path10.setObjectName(u"Path10")

        self.gridLayout.addWidget(self.Path10, 10, 1, 1, 1)

        self.RemoveBtn4 = QPushButton(self.widget)
        self.RemoveBtn4.setObjectName(u"RemoveBtn4")
        self.RemoveBtn4.setEnabled(False)
        self.RemoveBtn4.setMinimumSize(QSize(20, 20))
        self.RemoveBtn4.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn4, 4, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Add2 = QPushButton(self.widget)
        self.Add2.setObjectName(u"Add2")
        self.Add2.setEnabled(False)
        self.Add2.setMinimumSize(QSize(150, 20))
        self.Add2.setMaximumSize(QSize(150, 20))
        self.Add2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add2.setStyleSheet(u"#Add2 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add2:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add2:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add2, 2, 0, 1, 1)

        self.RemoveBtn7 = QPushButton(self.widget)
        self.RemoveBtn7.setObjectName(u"RemoveBtn7")
        self.RemoveBtn7.setEnabled(False)
        self.RemoveBtn7.setMinimumSize(QSize(20, 20))
        self.RemoveBtn7.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn7, 7, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Add10 = QPushButton(self.widget)
        self.Add10.setObjectName(u"Add10")
        self.Add10.setEnabled(False)
        self.Add10.setMinimumSize(QSize(150, 20))
        self.Add10.setMaximumSize(QSize(150, 20))
        self.Add10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add10.setStyleSheet(u"#Add10 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add10:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add10:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add10, 10, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.RemoveBtn6 = QPushButton(self.widget)
        self.RemoveBtn6.setObjectName(u"RemoveBtn6")
        self.RemoveBtn6.setEnabled(False)
        self.RemoveBtn6.setMinimumSize(QSize(20, 20))
        self.RemoveBtn6.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn6, 6, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Path5 = QLabel(self.widget)
        self.Path5.setObjectName(u"Path5")

        self.gridLayout.addWidget(self.Path5, 5, 1, 1, 1)

        self.Path2 = QLabel(self.widget)
        self.Path2.setObjectName(u"Path2")

        self.gridLayout.addWidget(self.Path2, 2, 1, 1, 1)

        self.Add9 = QPushButton(self.widget)
        self.Add9.setObjectName(u"Add9")
        self.Add9.setEnabled(False)
        self.Add9.setMinimumSize(QSize(150, 20))
        self.Add9.setMaximumSize(QSize(150, 20))
        self.Add9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add9.setStyleSheet(u"#Add9 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add9:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add9:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add9, 9, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.RemoveBtn2 = QPushButton(self.widget)
        self.RemoveBtn2.setObjectName(u"RemoveBtn2")
        self.RemoveBtn2.setEnabled(False)
        self.RemoveBtn2.setMinimumSize(QSize(20, 20))
        self.RemoveBtn2.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn2, 2, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Path8 = QLabel(self.widget)
        self.Path8.setObjectName(u"Path8")

        self.gridLayout.addWidget(self.Path8, 8, 1, 1, 1)

        self.Add7 = QPushButton(self.widget)
        self.Add7.setObjectName(u"Add7")
        self.Add7.setEnabled(False)
        self.Add7.setMinimumSize(QSize(150, 20))
        self.Add7.setMaximumSize(QSize(150, 20))
        self.Add7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add7.setStyleSheet(u"#Add7 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add7:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add7:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add7, 7, 0, 1, 1)

        self.RemoveBtn1 = QPushButton(self.widget)
        self.RemoveBtn1.setObjectName(u"RemoveBtn1")
        self.RemoveBtn1.setEnabled(False)
        self.RemoveBtn1.setMinimumSize(QSize(20, 20))
        self.RemoveBtn1.setMaximumSize(QSize(20, 20))
        self.RemoveBtn1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.RemoveBtn1, 1, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Add4 = QPushButton(self.widget)
        self.Add4.setObjectName(u"Add4")
        self.Add4.setEnabled(False)
        self.Add4.setMinimumSize(QSize(150, 20))
        self.Add4.setMaximumSize(QSize(150, 20))
        self.Add4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add4.setStyleSheet(u"#Add4 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add4:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add4:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add4, 4, 0, 1, 1)

        self.Path4 = QLabel(self.widget)
        self.Path4.setObjectName(u"Path4")

        self.gridLayout.addWidget(self.Path4, 4, 1, 1, 1)

        self.Path6 = QLabel(self.widget)
        self.Path6.setObjectName(u"Path6")

        self.gridLayout.addWidget(self.Path6, 6, 1, 1, 1)

        self.Path1 = QLabel(self.widget)
        self.Path1.setObjectName(u"Path1")

        self.gridLayout.addWidget(self.Path1, 1, 1, 1, 1)

        self.RemoveBtn3 = QPushButton(self.widget)
        self.RemoveBtn3.setObjectName(u"RemoveBtn3")
        self.RemoveBtn3.setEnabled(False)
        self.RemoveBtn3.setMinimumSize(QSize(20, 20))
        self.RemoveBtn3.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn3, 3, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Add1 = QPushButton(self.widget)
        self.Add1.setObjectName(u"Add1")
        self.Add1.setMinimumSize(QSize(150, 20))
        self.Add1.setMaximumSize(QSize(150, 20))
        self.Add1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add1.setAutoFillBackground(False)
        self.Add1.setStyleSheet(u"#Add1 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add1:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add1:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add1, 1, 0, 1, 1)

        self.PathColumn = QLabel(self.widget)
        self.PathColumn.setObjectName(u"PathColumn")
        self.PathColumn.setMinimumSize(QSize(550, 0))
        self.PathColumn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.PathColumn, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.NameColumn = QLabel(self.widget)
        self.NameColumn.setObjectName(u"NameColumn")
        self.NameColumn.setMinimumSize(QSize(150, 0))
        self.NameColumn.setMaximumSize(QSize(100, 20))
        self.NameColumn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.NameColumn, 0, 0, 1, 1)

        self.Add8 = QPushButton(self.widget)
        self.Add8.setObjectName(u"Add8")
        self.Add8.setEnabled(False)
        self.Add8.setMinimumSize(QSize(150, 20))
        self.Add8.setMaximumSize(QSize(150, 20))
        self.Add8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add8.setStyleSheet(u"#Add8 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add8:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add8:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add8, 8, 0, 1, 1)

        self.RemoveBtn8 = QPushButton(self.widget)
        self.RemoveBtn8.setObjectName(u"RemoveBtn8")
        self.RemoveBtn8.setEnabled(False)
        self.RemoveBtn8.setMinimumSize(QSize(20, 20))
        self.RemoveBtn8.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn8, 8, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.Add5 = QPushButton(self.widget)
        self.Add5.setObjectName(u"Add5")
        self.Add5.setEnabled(False)
        self.Add5.setMinimumSize(QSize(150, 20))
        self.Add5.setMaximumSize(QSize(150, 20))
        self.Add5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add5.setStyleSheet(u"#Add5 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add5:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add5:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add5, 5, 0, 1, 1)

        self.Path7 = QLabel(self.widget)
        self.Path7.setObjectName(u"Path7")

        self.gridLayout.addWidget(self.Path7, 7, 1, 1, 1)

        self.Add6 = QPushButton(self.widget)
        self.Add6.setObjectName(u"Add6")
        self.Add6.setEnabled(False)
        self.Add6.setMinimumSize(QSize(150, 20))
        self.Add6.setMaximumSize(QSize(150, 20))
        self.Add6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Add6.setStyleSheet(u"#Add6 {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"#Add6:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}\n"
"#Add6:pressed {\n"
"background-color: rgba(0, 0, 0, 0.6);\n"
"}")

        self.gridLayout.addWidget(self.Add6, 6, 0, 1, 1)

        self.Path3 = QLabel(self.widget)
        self.Path3.setObjectName(u"Path3")

        self.gridLayout.addWidget(self.Path3, 3, 1, 1, 1)

        self.RemoveBtn10 = QPushButton(self.widget)
        self.RemoveBtn10.setObjectName(u"RemoveBtn10")
        self.RemoveBtn10.setEnabled(False)
        self.RemoveBtn10.setMinimumSize(QSize(20, 20))
        self.RemoveBtn10.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn10, 10, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.PreviewColumn = QLabel(self.widget)
        self.PreviewColumn.setObjectName(u"PreviewColumn")
        self.PreviewColumn.setMinimumSize(QSize(50, 20))
        self.PreviewColumn.setMaximumSize(QSize(50, 20))
        self.PreviewColumn.setStyleSheet(u"padding: 1px;")

        self.gridLayout.addWidget(self.PreviewColumn, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.RemoveBtn9 = QPushButton(self.widget)
        self.RemoveBtn9.setObjectName(u"RemoveBtn9")
        self.RemoveBtn9.setEnabled(False)
        self.RemoveBtn9.setMinimumSize(QSize(20, 20))
        self.RemoveBtn9.setMaximumSize(QSize(20, 20))

        self.gridLayout.addWidget(self.RemoveBtn9, 9, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.StopBtn = QPushButton(self.centralwidget)
        self.StopBtn.setObjectName(u"StopBtn")
        self.StopBtn.setEnabled(False)
        self.StopBtn.setGeometry(QRect(670, 550, 115, 35))
        self.StopBtn.setStyleSheet(u"#StopBtn {\n"
"background-color: rgba(0, 0, 0, 0.3);\n"
"border-radius: 8px;\n"
"font: 10pt \"Sitka\";\n"
"}\n"
"#StopBtn:hover {\n"
"background-color: rgba(0, 0, 0, 0.15);\n"
"}\n"
"#StopBtn:pressed {\n"
"background-color: rgba(0, 0, 0, 0.5);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Stop/icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StopBtn.setIcon(icon3)
        self.FalseLabel = QLabel(self.centralwidget)
        self.FalseLabel.setObjectName(u"FalseLabel")
        self.FalseLabel.setGeometry(QRect(10, 550, 61, 35))
        self.FalseLabel.setMinimumSize(QSize(0, 0))
        self.FalseLabel.setMaximumSize(QSize(1000, 1000))
        self.FalseLabel.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.15);\n"
"border-radius: 8px;\n"
"font: 10pt \"Sitka\";\n"
"padding: 5px;")
        self.SuccessLabel = QLabel(self.centralwidget)
        self.SuccessLabel.setObjectName(u"SuccessLabel")
        self.SuccessLabel.setGeometry(QRect(155, 550, 80, 35))
        self.SuccessLabel.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.15);\n"
"border-radius: 8px;\n"
"font: 10pt \"Sitka\";\n"
"padding: 3px;")
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(-10, 40, 811, 71))
        self.widget1.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.15);")
        self.LabelLayout = QVBoxLayout(self.widget1)
        self.LabelLayout.setObjectName(u"LabelLayout")
        self.Name1 = QLabel(self.widget1)
        self.Name1.setObjectName(u"Name1")
        self.Name1.setMinimumSize(QSize(0, 35))
        self.Name1.setStyleSheet(u"background-color: none;\n"
"font: 20pt \"Sitka\";\n"
"alignement: center;")

        self.LabelLayout.addWidget(self.Name1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Name2 = QLabel(self.widget1)
        self.Name2.setObjectName(u"Name2")
        self.Name2.setStyleSheet(u"background-color: none;\n"
"font: 12pt \"Sitka\";")

        self.LabelLayout.addWidget(self.Name2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.SuccessKey = QPushButton(self.centralwidget)
        self.SuccessKey.setObjectName(u"SuccessKey")
        self.SuccessKey.setGeometry(QRect(75, 550, 60, 35))
        self.SuccessKey.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SuccessKey.setStyleSheet(u"#SuccessKey {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"border-radius: 8px;\n"
"font: 12pt \"Sitka\";\n"
"}\n"
"#SuccessKey:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}")
        self.SuccessKey.setIconSize(QSize(20, 20))
        self.FalseKey = QPushButton(self.centralwidget)
        self.FalseKey.setObjectName(u"FalseKey")
        self.FalseKey.setGeometry(QRect(240, 550, 60, 35))
        self.FalseKey.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.FalseKey.setStyleSheet(u"#FalseKey {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"border-radius: 8px;\n"
"font: 12pt \"Sitka\";\n"
"}\n"
"#FalseKey:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}")
        self.FalseKey.setIconSize(QSize(20, 20))
        self.CloseBtn = QPushButton(self.centralwidget)
        self.CloseBtn.setObjectName(u"CloseBtn")
        self.CloseBtn.setGeometry(QRect(760, 5, 30, 30))
        self.CloseBtn.setStyleSheet(u"#CloseBtn {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Close/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CloseBtn.setIcon(icon4)
        self.CloseBtn.setIconSize(QSize(20, 20))
        self.MinimizeBtn = QPushButton(self.centralwidget)
        self.MinimizeBtn.setObjectName(u"MinimizeBtn")
        self.MinimizeBtn.setGeometry(QRect(730, 4, 30, 30))
        self.MinimizeBtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/Minimize/icons/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MinimizeBtn.setIcon(icon5)
        self.MinimizeBtn.setIconSize(QSize(20, 20))
        self.SaveBtn = QPushButton(self.centralwidget)
        self.SaveBtn.setObjectName(u"SaveBtn")
        self.SaveBtn.setGeometry(QRect(630, 500, 161, 31))
        self.SaveBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveBtn.setStyleSheet(u"#SaveBtn {\n"
"background-color: rgba(0, 0, 0, 0.3);\n"
"border-radius: 8px;\n"
"font: 10pt \"Sitka\";\n"
"}\n"
"#SaveBtn:hover {\n"
"background-color: rgba(0, 0, 0, 0.2);\n"
"}\n"
"#SaveBtn:pressed {\n"
"background-color: rgba(0, 0, 0, 0.5);\n"
"}")
        self.DelayLabel = QLabel(self.centralwidget)
        self.DelayLabel.setObjectName(u"DelayLabel")
        self.DelayLabel.setGeometry(QRect(320, 550, 50, 35))
        self.DelayLabel.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.15);\n"
"border-radius: 8px;\n"
"font: 10pt \"Sitka\";\n"
"padding: 2px;")
        self.TipSKey = QLabel(self.centralwidget)
        self.TipSKey.setObjectName(u"TipSKey")
        self.TipSKey.setEnabled(True)
        self.TipSKey.setGeometry(QRect(45, 485, 120, 60))
        self.TipSKey.setStyleSheet(u"#TipSKey {\n"
"background-color: rgba(0, 0, 0, 0.8);\n"
"border-radius: 8px;\n"
"font: 7.5pt \"Sitka\";\n"
"padding: 1px;\n"
"}")
        self.TipSKey.setTextFormat(Qt.TextFormat.AutoText)
        self.TipSKey.setScaledContents(False)
        self.TipSKey.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.TipSKey.setWordWrap(True)
        self.TipSKey.setMargin(2)
        self.TipFKey = QLabel(self.centralwidget)
        self.TipFKey.setObjectName(u"TipFKey")
        self.TipFKey.setGeometry(QRect(210, 485, 120, 60))
        self.TipFKey.setStyleSheet(u"#TipFKey {\n"
"background-color: rgba(0, 0, 0, 0.8);\n"
"border-radius: 8px;\n"
"font: 7.5pt \"Sitka\";\n"
"padding: 1px;\n"
"}")
        self.TipFKey.setTextFormat(Qt.TextFormat.AutoText)
        self.TipFKey.setScaledContents(False)
        self.TipFKey.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.TipFKey.setWordWrap(True)
        self.TipFKey.setMargin(2)
        self.TipDelay = QLabel(self.centralwidget)
        self.TipDelay.setObjectName(u"TipDelay")
        self.TipDelay.setGeometry(QRect(340, 495, 130, 50))
        self.TipDelay.setStyleSheet(u"#TipDelay {\n"
"background-color: rgba(0, 0, 0, 0.8);\n"
"border-radius: 8px;\n"
"font: 7.5pt \"Sitka\";\n"
"padding: 1px;\n"
"}")
        self.TipDelay.setTextFormat(Qt.TextFormat.AutoText)
        self.TipDelay.setScaledContents(False)
        self.TipDelay.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.TipDelay.setWordWrap(True)
        self.TipDelay.setMargin(2)
        self.DelayInput = QLineEdit(self.centralwidget)
        self.DelayInput.setObjectName(u"DelayInput")
        self.DelayInput.setGeometry(QRect(375, 550, 60, 35))
        self.DelayInput.setStyleSheet(u"#DelayInput {\n"
"background-color: rgba(0, 0, 0, 0.4);\n"
"border-radius: 8px;\n"
"font: 12pt \"Sitka\";\n"
"padding: 3px;\n"
"}\n"
"#DelayInput:hover {\n"
"background-color: rgba(0, 0, 0, 0.25);\n"
"}")
        self.DelayInput.setMaxLength(5)
        self.DelayInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DelayInput.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.DelayInput.setClearButtonEnabled(False)
        self.TipDelayError = QLabel(self.centralwidget)
        self.TipDelayError.setObjectName(u"TipDelayError")
        self.TipDelayError.setGeometry(QRect(441, 552, 103, 31))
        self.TipDelayError.setStyleSheet(u"#TipDelayError {\n"
"background-color: rgba(0, 0, 0, 0.8);\n"
"border-radius: 8px;\n"
"font: 7.5pt \"Sitka\";\n"
"padding: 1px;\n"
"}")
        self.TipDelayError.setTextFormat(Qt.TextFormat.AutoText)
        self.TipDelayError.setScaledContents(False)
        self.TipDelayError.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.TipDelayError.setWordWrap(True)
        self.TipDelayError.setMargin(2)
        self.InfoBtn = QPushButton(self.centralwidget)
        self.InfoBtn.setObjectName(u"InfoBtn")
        self.InfoBtn.setGeometry(QRect(515, 550, 30, 35))
        self.InfoBtn.setStyleSheet(u"#InfoBtn {\n"
"background-color: rgba(0, 0, 0, 0.3);\n"
"border-radius: 8px;\n"
"font: 8pt \"Sitka\";\n"
"}\n"
"#InfoBtn:hover {\n"
"background-color: rgba(0, 0, 0, 0.2);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Info/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.InfoBtn.setIcon(icon6)
        self.InfoBtn.setIconSize(QSize(20, 20))
        self.InfoTip = QLabel(self.centralwidget)
        self.InfoTip.setObjectName(u"InfoTip")
        self.InfoTip.setGeometry(QRect(475, 495, 111, 51))
        self.InfoTip.setStyleSheet(u"#InfoTip {\n"
"background-color: rgba(0, 0, 0, 0.8);\n"
"border-radius: 8px;\n"
"font: 6.5pt \"Sitka\";\n"
"padding: 1px;\n"
"}")
        self.InfoTip.setTextFormat(Qt.TextFormat.AutoText)
        self.InfoTip.setScaledContents(False)
        self.InfoTip.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.InfoTip.setWordWrap(True)
        self.InfoTip.setMargin(2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gem Finder", None))
        self.ClearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.StartBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Add3.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.RemoveBtn5.setText("")
        self.Path9.setText("")
        self.Path10.setText("")
        self.RemoveBtn4.setText("")
        self.Add2.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.RemoveBtn7.setText("")
        self.Add10.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.RemoveBtn6.setText("")
        self.Path5.setText("")
        self.Path2.setText("")
        self.Add9.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.RemoveBtn2.setText("")
        self.Path8.setText("")
        self.Add7.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.RemoveBtn1.setText("")
        self.Add4.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.Path4.setText("")
        self.Path6.setText("")
        self.Path1.setText("")
        self.RemoveBtn3.setText("")
        self.Add1.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.PathColumn.setText(QCoreApplication.translate("MainWindow", u"                                                                                Path", None))
        self.NameColumn.setText(QCoreApplication.translate("MainWindow", u"                   Name", None))
        self.Add8.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.RemoveBtn8.setText("")
        self.Add5.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.Path7.setText("")
        self.Add6.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.Path3.setText("")
        self.RemoveBtn10.setText("")
        self.PreviewColumn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.RemoveBtn9.setText("")
        self.StopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.FalseLabel.setText(QCoreApplication.translate("MainWindow", u"Found:", None))
        self.SuccessLabel.setText(QCoreApplication.translate("MainWindow", u"Not found:", None))
        self.Name1.setText(QCoreApplication.translate("MainWindow", u"King of Thieves", None))
        self.Name2.setText(QCoreApplication.translate("MainWindow", u"Golden Gem Finder", None))
        self.SuccessKey.setText("")
        self.FalseKey.setText("")
        self.CloseBtn.setText("")
        self.MinimizeBtn.setText("")
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.DelayLabel.setText(QCoreApplication.translate("MainWindow", u"Delay:", None))
        self.TipSKey.setText(QCoreApplication.translate("MainWindow", u"If any of the images are found on the screen, this key will be pressed.", None))
        self.TipFKey.setText(QCoreApplication.translate("MainWindow", u"If none of the images are found on the screen, this key will be pressed.", None))
        self.TipDelay.setText(QCoreApplication.translate("MainWindow", u"Delay between searches. Recommended at least 0.5 seconds.", None))
        self.DelayInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0,7", None))
        self.TipDelayError.setText(QCoreApplication.translate("MainWindow", u"The value cannot start with ' , ' or ' . '", None))
        self.InfoBtn.setText("")
        self.InfoTip.setText(QCoreApplication.translate("MainWindow", u"The script is running. To make the script work, you need to collapse this window.", None))
    # retranslateUi

