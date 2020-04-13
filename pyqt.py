import os
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class FirstMainWin(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 设置窗口标题
        self.setWindowTitle('测试')

        # 设置窗口的尺寸
        self.setObjectName("MainWindow")
        self.resize(1200, 650)
        self.setMinimumSize(QtCore.QSize(1200, 650))
        self.setMaximumSize(QtCore.QSize(1920, 1080))

        all_widget = QWidget(self)

        w1 = QGridLayout(all_widget)
        vlayout_1 = QVBoxLayout()
        vlayout_2 = QVBoxLayout()
        hlayout_1 = QHBoxLayout()
        hlayout_2 = QHBoxLayout()


        tabwidget_1 = QTabWidget()
        tab_1 = QWidget()


        tablewidget_1 = QTableWidget()
        # tableview_1.setModel(model)
        # tableview_1.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中
        # tableview_1.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置只能选中一行
        # tableview_1.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        # # tableview_1.resizeColumnsToContents()  # 根据内容调整大小
        # tableview_1.verticalHeader().setVisible(False)  # 行表头隐藏
        # tableview_1.setAutoScroll(True)  # 自动滚动条
        # tableview_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列都扩展自适应宽度，填充充满整个屏幕宽度
        #
        #
        # tableview_1.setContextMenuPolicy(Qt.ActionsContextMenu)
        #
        # tableview_1.setContextMenuPolicy(Qt.CustomContextMenu)
        # tableview_1.customContextMenuRequested.connect(self.rightMenuShow)  # 开放右键策略
        # indexs = tableview_1.selectionModel().selection().indexes()


        # tableview_1.setColumnWidth(0, 50)
        # tableview_1.setColumnWidth(1, 200)
        # tableview_1.setColumnWidth(2, 200)
        # tableview_1.setColumnWidth(3, 150)
        # tableview_1.setColumnWidth(4, 200)
        # tableview_1.setColumnWidth(5, 200)




        # tablewidget_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # tablewidget_1.setSelectionBehavior(QAbstractItemView.SelectRows)
        # tablewidget_1.setShowGrid(False)
        # tablewidget_1.verticalHeader().setVisible(False)
        # tablewidget_1.horizontalHeader().setVisible(True)
        tablewidget_1.setColumnCount(5)
        tablewidget_1.setHorizontalHeaderLabels(['账号', '密码', '服务器\区服', '任务', '开始时间'])
        tablewidget_1.setColumnWidth(0, 200)
        tablewidget_1.setColumnWidth(1, 200)
        tablewidget_1.setColumnWidth(2, 150)
        tablewidget_1.setColumnWidth(3, 200)
        tablewidget_1.setColumnWidth(4, 100)


        vlayout_2.addWidget(tablewidget_1)
        tab_1.setLayout(vlayout_2)
        tabwidget_1.addTab(tab_1, "七战")

        vlayout_1.addWidget(tabwidget_1)


        hwg_1 = QWidget()
        btn_1 = QPushButton()
        btn_1.setText("打开文件")
        btn_1.setObjectName('btn_1')
        # print(btn_1.text())
        line_1 = QLineEdit()
        line_1.setObjectName('line_1')
        btn_2 = QPushButton()
        btn_2.setText("保存配置")
        btn_2.setObjectName('btn_2')
        # print(btn_2.text())
        btn_3 = QPushButton()
        btn_3.setText("删除配置")
        btn_3.setObjectName('btn_3')
        # print(btn_3.text())
        btn_1.clicked.connect(lambda: self.OpenTxt(line_1, tablewidget_1, btn_4))
        btn_2.clicked.connect(lambda:self.SaveIni(tablewidget_1))
        btn_3.clicked.connect(lambda:self.DelIni(tablewidget_1))
        # btn_3.clicked.connect(self.SaveIni)


        hlayout_1.addWidget(btn_1)
        hlayout_1.addWidget(line_1)
        hlayout_1.addWidget(btn_2)
        hlayout_1.addWidget(btn_3)

        hwg_1.setLayout(hlayout_1)



        hwg_2 = QWidget()
        btn_4 = QPushButton()
        btn_4.setText("全部启动")
        btn_4.setObjectName('btn_4')


        btn_5 = QPushButton()
        btn_5.setText("全部停止")
        btn_5.setObjectName('btn_5')
        btn_6 = QPushButton()
        btn_6.setText("全部暂停")
        btn_6.setObjectName('btn_6')
        hlayout_2.addWidget(btn_4)
        hlayout_2.addWidget(btn_5)
        hlayout_2.addWidget(btn_6)
        if tablewidget_1.rowCount() == 0:
            btn_4.setEnabled(False)
            btn_5.setEnabled(False)
            btn_6.setEnabled(False)
        btn_4.clicked.connect(lambda: self.AllRun(btn_4, btn_5, btn_6))
        hwg_2.setLayout(hlayout_2)


        w1.addWidget(tabwidget_1)
        w1.addWidget(hwg_1)
        w1.addWidget(hwg_2)

        self.setLayout(w1)

        self.show()

    def AllRun(self, btn_4, btn_5, btn_6):
        btn_4.setEnabled(False)
        btn_5.setEnabled(True)
        btn_6.setEnabled(True)
        self.mythreaf = MyThread()
        self.mythreaf.start()



    def OpenTxt(self, line, tablewidget, btn_4):
        FullFileName, _ = QFileDialog.getOpenFileName(self, '打开', r'./', 'TXT (*.txt)')
        if FullFileName == "":
            return
        line.setText(FullFileName)
        with open(FullFileName, 'rt') as f:
            txt_line = f.read()
        txt_lists = txt_line.split("\n")
        print(txt_lists)
        if txt_lists[-1] == "" or str(txt_lists[-1]) == '\n':
            txt_lists.pop(-1)
        print(txt_lists)
        rowcount = tablewidget.rowCount()
        tablewidget.setRowCount(rowcount + len(txt_lists))
        for rc in range(len(txt_lists)):
            # tablewidget.insertRow(rowcount + rc)
            txt_strs = str(txt_lists[rc]).split(';')[0].split(',')
            for i in range(len(txt_strs)):
                Item = QTableWidgetItem(str(txt_strs[i]).split()[0])
                tablewidget.setItem(rowcount + rc, i, Item)

        rowcount = tablewidget.rowCount()
        if rowcount != 0:
            btn_4.setEnabled(True)


    def SaveIni(self, tablewidget):
        propath = os.getcwd()
        infor_path = os.path.join(propath, '保存配置.txt')
        Rmax = tablewidget.rowCount()

        with open(infor_path, mode='w', encoding='utf-8') as f:
            for R in range(Rmax):
                str1 = ','
                txt_strs = []
                for C in range(3):
                    itemstr = str(tablewidget.item(R, C).text()).split()[0]
                    print(itemstr)
                    txt_strs.append(itemstr)
                str1 = str1.join(txt_strs)
                str1 = str1 + ";\n"
                f.write(str1)


    def DelIni(self, tablewidget):
        Rowmax = tablewidget.rowCount()
        for R in range(Rowmax, 0, -1):
            tablewidget.removeRow(R-1)
        set_path = os.path.join(os.getcwd(), '保存配置.txt')
        if os.path.exists(set_path):

            os.remove(set_path)
        else:
            pass

class MyThread(QThread):
    singal = pyqtSignal()

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        os.startfile('七战.exe')






if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = FirstMainWin()

    sys.exit(app.exec_())
