# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'methods_and_parameters_page.ui'
#
# Created: Mon Jul 29 17:07:42 2013
#      by: PyQt4 UI code generator 4.10.1
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
        WizardPage.resize(557, 533)
        WizardPage.setTitle(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(WizardPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.specs_tab = QtGui.QTabWidget(WizardPage)
        self.specs_tab.setObjectName(_fromUtf8("specs_tab"))
        self.methods_tab = QtGui.QWidget()
        self.methods_tab.setObjectName(_fromUtf8("methods_tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.methods_tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.method_lbl = QtGui.QLabel(self.methods_tab)
        self.method_lbl.setMinimumSize(QtCore.QSize(200, 0))
        self.method_lbl.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.method_lbl.setFont(font)
        self.method_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.method_lbl.setObjectName(_fromUtf8("method_lbl"))
        self.gridLayout.addWidget(self.method_lbl, 0, 0, 1, 1)
        self.method_cbo_box = QtGui.QComboBox(self.methods_tab)
        self.method_cbo_box.setObjectName(_fromUtf8("method_cbo_box"))
        self.gridLayout.addWidget(self.method_cbo_box, 0, 1, 1, 1)
        self.parameter_grp_box = QtGui.QGroupBox(self.methods_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.parameter_grp_box.sizePolicy().hasHeightForWidth())
        self.parameter_grp_box.setSizePolicy(sizePolicy)
        self.parameter_grp_box.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.parameter_grp_box.setFont(font)
        self.parameter_grp_box.setTitle(_fromUtf8(""))
        self.parameter_grp_box.setObjectName(_fromUtf8("parameter_grp_box"))
        self.gridLayout.addWidget(self.parameter_grp_box, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.specs_tab.addTab(self.methods_tab, _fromUtf8(""))
        self.plot_tab = QtGui.QWidget()
        self.plot_tab.setObjectName(_fromUtf8("plot_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.plot_tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.plot_tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.col1_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col1_str_edit.setObjectName(_fromUtf8("col1_str_edit"))
        self.gridLayout_2.addWidget(self.col1_str_edit, 0, 1, 1, 1)
        self.show_1 = QtGui.QCheckBox(self.groupBox)
        self.show_1.setChecked(True)
        self.show_1.setObjectName(_fromUtf8("show_1"))
        self.gridLayout_2.addWidget(self.show_1, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.col2_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col2_str_edit.setObjectName(_fromUtf8("col2_str_edit"))
        self.gridLayout_2.addWidget(self.col2_str_edit, 1, 1, 1, 1)
        self.show_2 = QtGui.QCheckBox(self.groupBox)
        self.show_2.setChecked(True)
        self.show_2.setObjectName(_fromUtf8("show_2"))
        self.gridLayout_2.addWidget(self.show_2, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.col3_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col3_str_edit.setObjectName(_fromUtf8("col3_str_edit"))
        self.gridLayout_2.addWidget(self.col3_str_edit, 2, 1, 1, 1)
        self.show_3 = QtGui.QCheckBox(self.groupBox)
        self.show_3.setChecked(True)
        self.show_3.setObjectName(_fromUtf8("show_3"))
        self.gridLayout_2.addWidget(self.show_3, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.col4_str_edit = QtGui.QLineEdit(self.groupBox)
        self.col4_str_edit.setObjectName(_fromUtf8("col4_str_edit"))
        self.gridLayout_2.addWidget(self.col4_str_edit, 3, 1, 1, 1)
        self.show_4 = QtGui.QCheckBox(self.groupBox)
        self.show_4.setChecked(True)
        self.show_4.setObjectName(_fromUtf8("show_4"))
        self.gridLayout_2.addWidget(self.show_4, 3, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_7 = QtGui.QLabel(self.plot_tab)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.x_lbl_le = QtGui.QLineEdit(self.plot_tab)
        self.x_lbl_le.setObjectName(_fromUtf8("x_lbl_le"))
        self.gridLayout_3.addWidget(self.x_lbl_le, 0, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.plot_tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.x_ticks_le = QtGui.QLineEdit(self.plot_tab)
        self.x_ticks_le.setObjectName(_fromUtf8("x_ticks_le"))
        self.gridLayout_3.addWidget(self.x_ticks_le, 4, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.plot_tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.plot_lb_le = QtGui.QLineEdit(self.plot_tab)
        self.plot_lb_le.setObjectName(_fromUtf8("plot_lb_le"))
        self.gridLayout_3.addWidget(self.plot_lb_le, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.plot_tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.plot_ub_le = QtGui.QLineEdit(self.plot_tab)
        self.plot_ub_le.setObjectName(_fromUtf8("plot_ub_le"))
        self.gridLayout_3.addWidget(self.plot_ub_le, 2, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.plot_tab)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)
        self.show_summary_line = QtGui.QCheckBox(self.plot_tab)
        self.show_summary_line.setText(_fromUtf8(""))
        self.show_summary_line.setChecked(True)
        self.show_summary_line.setObjectName(_fromUtf8("show_summary_line"))
        self.gridLayout_3.addWidget(self.show_summary_line, 5, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.plot_tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.image_path = QtGui.QLineEdit(self.plot_tab)
        self.image_path.setObjectName(_fromUtf8("image_path"))
        self.horizontalLayout_4.addWidget(self.image_path)
        self.save_btn = QtGui.QPushButton(self.plot_tab)
        self.save_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.specs_tab.addTab(self.plot_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.specs_tab)

        self.retranslateUi(WizardPage)
        self.specs_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "Methods & Parameters", None))
        self.method_lbl.setText(_translate("WizardPage", "analysis method:", None))
        self.specs_tab.setTabText(self.specs_tab.indexOf(self.methods_tab), _translate("WizardPage", "method", None))
        self.groupBox.setTitle(_translate("WizardPage", "column labels", None))
        self.label_2.setToolTip(_translate("WizardPage", "Text for column title that appears on forest plot", None))
        self.label_2.setText(_translate("WizardPage", "col 1 label:", None))
        self.col1_str_edit.setText(_translate("WizardPage", "Studies", None))
        self.show_1.setText(_translate("WizardPage", "show", None))
        self.label_4.setToolTip(_translate("WizardPage", "Text for column title that appears on forest plot", None))
        self.label_4.setText(_translate("WizardPage", "col 2 label:", None))
        self.col2_str_edit.setText(_translate("WizardPage", "[default]", None))
        self.show_2.setText(_translate("WizardPage", "show", None))
        self.label_5.setToolTip(_translate("WizardPage", "Text for column title that appears on forest plot", None))
        self.label_5.setText(_translate("WizardPage", "col 3 label:", None))
        self.col3_str_edit.setText(_translate("WizardPage", "Ev/Trt", None))
        self.show_3.setText(_translate("WizardPage", "show", None))
        self.label_6.setToolTip(_translate("WizardPage", "Text for column title that appears on forest plot", None))
        self.label_6.setText(_translate("WizardPage", "col 4 label:", None))
        self.col4_str_edit.setText(_translate("WizardPage", "Ev/Ctrl", None))
        self.show_4.setText(_translate("WizardPage", "show", None))
        self.label_7.setText(_translate("WizardPage", "x label:", None))
        self.x_lbl_le.setText(_translate("WizardPage", "[default]", None))
        self.label_8.setText(_translate("WizardPage", "x ticks:", None))
        self.x_ticks_le.setText(_translate("WizardPage", "[default]", None))
        self.label_9.setText(_translate("WizardPage", "x-axis lower bound", None))
        self.plot_lb_le.setText(_translate("WizardPage", "[default]", None))
        self.label_10.setText(_translate("WizardPage", "x-axis upper bound", None))
        self.plot_ub_le.setText(_translate("WizardPage", "[default]", None))
        self.label_11.setText(_translate("WizardPage", "show summary line:", None))
        self.label_3.setText(_translate("WizardPage", "save image to:", None))
        self.image_path.setText(_translate("WizardPage", "./r_tmp/forest.png", None))
        self.save_btn.setText(_translate("WizardPage", "...", None))
        self.specs_tab.setTabText(self.specs_tab.indexOf(self.plot_tab), _translate("WizardPage", "forest plot", None))

