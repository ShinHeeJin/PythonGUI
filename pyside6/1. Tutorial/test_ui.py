# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QCalendarWidget,
    QCheckBox,
    QCommandLinkButton,
    QGridLayout,
    QGroupBox,
    QListView,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSlider,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 1009)
        self.actionTest = QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionTest2 = QAction(MainWindow)
        self.actionTest2.setObjectName("actionTest2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 1, 1, 1, 1)

        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName("webEngineView")
        self.webEngineView.setUrl(QUrl("https://www.naver.com/"))

        self.gridLayout_2.addWidget(self.webEngineView, 2, 1, 1, 1)

        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 3, 0, 1, 1)

        self.list_view = QListView(self.centralwidget)
        self.list_view.setObjectName("list_view")

        self.gridLayout_2.addWidget(self.list_view, 3, 1, 1, 1)

        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")

        self.gridLayout_2.addWidget(self.calendarWidget, 4, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.commandLinkButton = QCommandLinkButton(self.groupBox)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.gridLayout.addWidget(self.commandLinkButton, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.groupBox, 5, 1, 1, 1)

        self.openGLWidget = QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setObjectName("openGLWidget")

        self.gridLayout_2.addWidget(self.openGLWidget, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 878, 22))
        self.menuTest_Application = QMenu(self.menubar)
        self.menuTest_Application.setObjectName("menuTest_Application")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuTest_Application.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionTest)
        self.menu.addAction(self.actionTest2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionTest.setText(QCoreApplication.translate("MainWindow", "Test", None))
        self.actionTest2.setText(
            QCoreApplication.translate("MainWindow", "Test2", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Click Me!", None)
        )
        self.checkBox.setText(
            QCoreApplication.translate("MainWindow", "Check me!", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "GroupBox", None)
        )
        self.commandLinkButton.setText(
            QCoreApplication.translate("MainWindow", "CommandLinkButton", None)
        )
        self.menuTest_Application.setTitle(
            QCoreApplication.translate("MainWindow", "Test Application", None)
        )
        self.menu.setTitle(
            QCoreApplication.translate("MainWindow", "\uba54\ub274", None)
        )
        # retranslateUi

        self.gridLayout_2.addWidget(self.openGLWidget, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 878, 22))
        self.menuTest_Application = QMenu(self.menubar)
        self.menuTest_Application.setObjectName("menuTest_Application")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuTest_Application.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionTest)
        self.menu.addAction(self.actionTest2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionTest.setText(QCoreApplication.translate("MainWindow", "Test", None))
        self.actionTest2.setText(
            QCoreApplication.translate("MainWindow", "Test2", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Click Me!", None)
        )
        self.checkBox.setText(
            QCoreApplication.translate("MainWindow", "Check me!", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "GroupBox", None)
        )
        self.commandLinkButton.setText(
            QCoreApplication.translate("MainWindow", "CommandLinkButton", None)
        )
        self.menuTest_Application.setTitle(
            QCoreApplication.translate("MainWindow", "Test Application", None)
        )
        self.menu.setTitle(
            QCoreApplication.translate("MainWindow", "\uba54\ub274", None)
        )

    # retranslateUi
