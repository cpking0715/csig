# -*- coding:utf-8 -*-
# author:v_ppechen
# datetime:2020/11/19 16:23
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from script.pyqt_5.pyqt_tools.clat import Ui_Form



class mwindow(QWidget, Ui_Form):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)

    def ps_bt(self):
        self.textBrowser.clear()

    def ps_bt1(self):
        self.lineEdit.insert('/')

    def ps_bt2(self):
        self.lineEdit.insert('*')

    def ps_bt3(self):
        self.lineEdit.insert('+')

    def ps_bt4(self):
        self.lineEdit.insert('-')

    def ps_bt5(self):
        # self.lineEdit.insert('=')
        # self.calculate()
        self.rename_file()

    def ps_bt6(self):
        self.lineEdit.insert('.')

    def ps_bt7(self):
        self.lineEdit.insert('0')

    def ps_bt8(self):
        self.lineEdit.insert('1')

    def ps_bt9(self):
        self.lineEdit.insert('2')

    def ps_bt10(self):
        self.lineEdit.insert('3')

    def ps_bt11(self):
        self.lineEdit.insert('4')

    def ps_bt12(self):
        self.lineEdit.insert('5')

    def ps_bt13(self):
        self.lineEdit.insert('6')

    def ps_bt14(self):
        self.lineEdit.insert('7')

    def ps_bt15(self):
        self.lineEdit.insert('8')

    def ps_bt16(self):
        self.lineEdit.insert('9')

    def ps_bt17(self):
        self.lineEdit.backspace()

    def ps_bt18(self):
        self.lineEdit.clear()

    def ps_bt19(self):
        self.open_polt()
        self.close()

    def lineEdit_clear(self):
        self.lineEdit.clear()

    def open_polt(self):
        dir_path = QFileDialog.getExistingDirectory(self, "choose directory", "/")
        if os.path.exists(dir_path):
            self.lineEdit.insert(dir_path)
            # for root, dirs, files in os.walk(dir_path):
            #     for file in files:
            #         self.TextEdit.insert(os.path.join(root, file))
            #         self.TextEdit.show(os.path.join(root, file))
                    # self.lineEdit.insert('\n')
        # self.QFileDialog.getExistingDirectory(self, "choose directory", r"C:\Users\Administrator\Desktop")

    def rename_file(self):
        text = self.lineEdit.text()
        # print(text)
        for root, dirs, files in os.walk(text):
            for file in files:
                os.rename(os.path.join(root, file), os.path.join(root, os.path.splitext(file)[0] + "_test" + os.path.splitext(file)[-1]))
                self.textBrowser.append(os.path.join(root, os.path.splitext(file)[0] + "_test" + os.path.splitext(file)[-1]))

    def calculate(self):
        # text = self.lineEdit.text()
        # self.lineEdit.setText('%s= %.2f' % (text, eval(text)))
        text = self.lineEdit.text()
        self.textBrowser.append('%s= %.2f' % (text, eval(text)))
        self.lineEdit_clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.pushButton.clicked.connect(w.ps_bt)
    w.pushButton_1.clicked.connect(w.ps_bt1)
    w.pushButton_2.clicked.connect(w.ps_bt2)
    w.pushButton_3.clicked.connect(w.ps_bt3)
    w.pushButton_4.clicked.connect(w.ps_bt4)
    w.pushButton_5.clicked.connect(w.rename_file)
    w.pushButton_6.clicked.connect(w.ps_bt6)
    w.pushButton_7.clicked.connect(w.ps_bt7)
    w.pushButton_8.clicked.connect(w.ps_bt8)
    w.pushButton_9.clicked.connect(w.ps_bt9)
    w.pushButton_10.clicked.connect(w.ps_bt10)
    w.pushButton_11.clicked.connect(w.ps_bt11)
    w.pushButton_12.clicked.connect(w.ps_bt12)
    w.pushButton_13.clicked.connect(w.ps_bt13)
    w.pushButton_14.clicked.connect(w.ps_bt14)
    w.pushButton_15.clicked.connect(w.ps_bt15)
    w.pushButton_16.clicked.connect(w.ps_bt16)
    w.pushButton_17.clicked.connect(w.ps_bt17)
    w.pushButton_18.clicked.connect(w.ps_bt18)
    w.pushButton_19.clicked.connect(w.ps_bt19)
    w.show()
    sys.exit(app.exec_())