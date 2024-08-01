# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_task.ui'
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


class Ui_NewTask(object):
    def setupUi(self, NewTask):
        if not NewTask.objectName():
            NewTask.setObjectName(u"NewTask")
        NewTask.resize(451, 289)
        self.verticalLayout = QVBoxLayout(NewTask)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(NewTask)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.label_4 = QLabel(NewTask)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.entity = QLabel(NewTask)
        self.entity.setObjectName(u"entity")

        self.gridLayout.addWidget(self.entity, 2, 1, 1, 1)

        self.label_6 = QLabel(NewTask)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.assigned_to = QLabel(NewTask)
        self.assigned_to.setObjectName(u"assigned_to")

        self.gridLayout.addWidget(self.assigned_to, 3, 1, 1, 1)

        self.label = QLabel(NewTask)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.pipeline_step = QComboBox(NewTask)
        self.pipeline_step.setObjectName(u"pipeline_step")

        self.gridLayout.addWidget(self.pipeline_step, 4, 1, 1, 1)

        self.label_2 = QLabel(NewTask)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.task_name = QLineEdit(NewTask)
        self.task_name.setObjectName(u"task_name")

        self.gridLayout.addWidget(self.task_name, 5, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(NewTask)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewTask)
        self.buttonBox.accepted.connect(NewTask.accept)
        self.buttonBox.rejected.connect(NewTask.reject)

        QMetaObject.connectSlotsByName(NewTask)
    # setupUi

    def retranslateUi(self, NewTask):
        NewTask.setWindowTitle(QCoreApplication.translate("NewTask", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("NewTask", u"<b><big>Create a new Task</big></b>\n"
"<br><br>\n"
"Type in a Task Name and select a Pipeline Step below.\n"
"<br><br>", None))
        self.label_4.setText(QCoreApplication.translate("NewTask", u"Entity", None))
        self.entity.setText(QCoreApplication.translate("NewTask", u"Shot ABC 123", None))
        self.label_6.setText(QCoreApplication.translate("NewTask", u"Assigned to", None))
        self.assigned_to.setText(QCoreApplication.translate("NewTask", u"Mr John Smith", None))
        self.label.setText(QCoreApplication.translate("NewTask", u"Pipeline Step", None))
        self.label_2.setText(QCoreApplication.translate("NewTask", u"Task Name", None))
    # retranslateUi
