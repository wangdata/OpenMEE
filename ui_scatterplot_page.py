# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scatterplot_page.ui'
#
# Created: Thu Jan  2 10:45:27 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(341, 176)
        self.verticalLayout = QtGui.QVBoxLayout(WizardPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.xlab_layout = QtGui.QHBoxLayout()
        self.xlab_layout.setObjectName(_fromUtf8("xlab_layout"))
        self.xlabCheckBox = QtGui.QCheckBox(WizardPage)
        self.xlabCheckBox.setObjectName(_fromUtf8("xlabCheckBox"))
        self.xlab_layout.addWidget(self.xlabCheckBox)
        self.label_3 = QtGui.QLabel(WizardPage)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.xlab_layout.addWidget(self.label_3)
        self.xlab_le = QtGui.QLineEdit(WizardPage)
        self.xlab_le.setEnabled(False)
        self.xlab_le.setText(_fromUtf8(""))
        self.xlab_le.setObjectName(_fromUtf8("xlab_le"))
        self.xlab_layout.addWidget(self.xlab_le)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.xlab_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.xlab_layout)
        self.ylab_layout = QtGui.QHBoxLayout()
        self.ylab_layout.setObjectName(_fromUtf8("ylab_layout"))
        self.ylabCheckBox = QtGui.QCheckBox(WizardPage)
        self.ylabCheckBox.setObjectName(_fromUtf8("ylabCheckBox"))
        self.ylab_layout.addWidget(self.ylabCheckBox)
        self.label_2 = QtGui.QLabel(WizardPage)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ylab_layout.addWidget(self.label_2)
        self.ylab_le = QtGui.QLineEdit(WizardPage)
        self.ylab_le.setEnabled(False)
        self.ylab_le.setText(_fromUtf8(""))
        self.ylab_le.setObjectName(_fromUtf8("ylab_le"))
        self.ylab_layout.addWidget(self.ylab_le)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ylab_layout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.ylab_layout)
        self.xlim_layout = QtGui.QHBoxLayout()
        self.xlim_layout.setObjectName(_fromUtf8("xlim_layout"))
        self.xlimCheckBox = QtGui.QCheckBox(WizardPage)
        self.xlimCheckBox.setObjectName(_fromUtf8("xlimCheckBox"))
        self.xlim_layout.addWidget(self.xlimCheckBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(WizardPage)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.xlimLowSpinBox = QtGui.QDoubleSpinBox(WizardPage)
        self.xlimLowSpinBox.setEnabled(False)
        self.xlimLowSpinBox.setMinimum(-10000.0)
        self.xlimLowSpinBox.setMaximum(10000.0)
        self.xlimLowSpinBox.setSingleStep(0.1)
        self.xlimLowSpinBox.setObjectName(_fromUtf8("xlimLowSpinBox"))
        self.horizontalLayout.addWidget(self.xlimLowSpinBox)
        self.label_11 = QtGui.QLabel(WizardPage)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.xlimHighSpinBox = QtGui.QDoubleSpinBox(WizardPage)
        self.xlimHighSpinBox.setEnabled(False)
        self.xlimHighSpinBox.setMinimum(-10000.0)
        self.xlimHighSpinBox.setMaximum(10000.0)
        self.xlimHighSpinBox.setSingleStep(0.1)
        self.xlimHighSpinBox.setObjectName(_fromUtf8("xlimHighSpinBox"))
        self.horizontalLayout.addWidget(self.xlimHighSpinBox)
        self.label_9 = QtGui.QLabel(WizardPage)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.xlim_layout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.xlim_layout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.xlim_layout)
        self.ylim_layout_2 = QtGui.QHBoxLayout()
        self.ylim_layout_2.setObjectName(_fromUtf8("ylim_layout_2"))
        self.ylimCheckBox = QtGui.QCheckBox(WizardPage)
        self.ylimCheckBox.setObjectName(_fromUtf8("ylimCheckBox"))
        self.ylim_layout_2.addWidget(self.ylimCheckBox)
        self.ylim_layout = QtGui.QHBoxLayout()
        self.ylim_layout.setObjectName(_fromUtf8("ylim_layout"))
        self.label_8 = QtGui.QLabel(WizardPage)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.ylim_layout.addWidget(self.label_8)
        self.ylimLowSpinBox = QtGui.QDoubleSpinBox(WizardPage)
        self.ylimLowSpinBox.setEnabled(False)
        self.ylimLowSpinBox.setMinimum(-10000.0)
        self.ylimLowSpinBox.setMaximum(10000.0)
        self.ylimLowSpinBox.setSingleStep(0.1)
        self.ylimLowSpinBox.setObjectName(_fromUtf8("ylimLowSpinBox"))
        self.ylim_layout.addWidget(self.ylimLowSpinBox)
        self.label_12 = QtGui.QLabel(WizardPage)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.ylim_layout.addWidget(self.label_12)
        self.ylimHighSpinBox = QtGui.QDoubleSpinBox(WizardPage)
        self.ylimHighSpinBox.setEnabled(False)
        self.ylimHighSpinBox.setMinimum(-10000.0)
        self.ylimHighSpinBox.setMaximum(10000.0)
        self.ylimHighSpinBox.setSingleStep(0.1)
        self.ylimHighSpinBox.setObjectName(_fromUtf8("ylimHighSpinBox"))
        self.ylim_layout.addWidget(self.ylimHighSpinBox)
        self.label_10 = QtGui.QLabel(WizardPage)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.ylim_layout.addWidget(self.label_10)
        self.ylim_layout_2.addLayout(self.ylim_layout)
        spacerItem3 = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ylim_layout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.ylim_layout_2)
        self.label_3.setBuddy(self.xlab_le)
        self.label_2.setBuddy(self.ylab_le)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        self.xlabCheckBox.setText(_translate("WizardPage", "set xlabel?", None))
        self.label_3.setText(_translate("WizardPage", "xlabel:", None))
        self.ylabCheckBox.setText(_translate("WizardPage", "set ylabel?", None))
        self.label_2.setText(_translate("WizardPage", "ylabel:", None))
        self.xlimCheckBox.setToolTip(_translate("WizardPage", "x axis limits. If not checked, the function tries to set the xaxis limits to some sensible values.", None))
        self.xlimCheckBox.setText(_translate("WizardPage", "set xlims?", None))
        self.label_7.setText(_translate("WizardPage", "[", None))
        self.label_11.setText(_translate("WizardPage", ",", None))
        self.label_9.setText(_translate("WizardPage", "]", None))
        self.ylimCheckBox.setToolTip(_translate("WizardPage", "y axis limits. If not checked, the function tries to set the yaxis limits to some sensible values.", None))
        self.ylimCheckBox.setText(_translate("WizardPage", "set ylims?", None))
        self.label_8.setText(_translate("WizardPage", "[", None))
        self.label_12.setText(_translate("WizardPage", ",", None))
        self.label_10.setText(_translate("WizardPage", "]", None))
