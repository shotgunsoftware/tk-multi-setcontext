# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from tank.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from ..entity_browser import EntityBrowserWidget
from ..task_browser import TaskBrowserWidget

from  . import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(797, 546)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.new_task = QToolButton(Dialog)
        self.new_task.setObjectName(u"new_task")
        icon = QIcon()
        icon.addFile(u":/res/icon_Task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_task.setIcon(icon)
        self.new_task.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.new_task)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.left_browser = EntityBrowserWidget(Dialog)
        self.left_browser.setObjectName(u"left_browser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_browser.sizePolicy().hasHeightForWidth())
        self.left_browser.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.left_browser, 0, 0, 1, 1)

        self.right_browser = TaskBrowserWidget(Dialog)
        self.right_browser.setObjectName(u"right_browser")
        sizePolicy.setHeightForWidth(self.right_browser.sizePolicy().hasHeightForWidth())
        self.right_browser.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.right_browser, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.change_context = QPushButton(Dialog)
        self.change_context.setObjectName(u"change_context")

        self.horizontalLayout_3.addWidget(self.change_context)

        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hide_tasks = QCheckBox(Dialog)
        self.hide_tasks.setObjectName(u"hide_tasks")
        self.hide_tasks.setChecked(True)

        self.horizontalLayout.addWidget(self.hide_tasks)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Change your Work Area", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Below is a list of Shotgun Items and their associated Tasks.\n"
"Double click a Task to set the current Work Area to point at it.", None))
        self.new_task.setText(QCoreApplication.translate("Dialog", u"Create New Task...", None))
        self.change_context.setText(QCoreApplication.translate("Dialog", u"Switch Work Area", None))
        self.hide_tasks.setText(QCoreApplication.translate("Dialog", u"Show My Tasks Only", None))
    # retranslateUi
