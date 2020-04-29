from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Configuration.MSConfig import *
from Configuration.MSConfigFile import *
from Configuration.MSConfigUI import *
from PyQt5.QtGui import QColor

from Configuration.UI_mainwindow import Ui_MainWindow

import os
import configparser
import tempfile

# import_file = ''

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        global import_file
        import_file = ''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.cwd = os.getcwd()
        self.color_warning = QColor(255, 0, 0)
        self.color_normal = QColor(255, 255, 255)

        # 配置文件列表
        self.config_list = [
            ['config_1.txt', CConfigOne, CConfigFileOne, CConfigUiOne],
        ]

        self.setMouseTracking(True)

        self.setTips(self.tbl_If)
        self.setTips(self.tbl_D)
        self.setTips(self.tbl_IR)
        self.setTips(self.tbl_Q)

        self.addItemsToTypeList()
        self.initUI()

    def initUI(self):
        self.btn_run.setDisabled(True)
        cconfig = CConfigOne()
        cconfig_file = CConfigFileOne()
        cconfig_ui = CConfigUiOne()
        path = os.path.dirname(os.path.abspath(__file__)) + '\default.txt'
        print(path)

        cconfig = cconfig_file.file2config(path, cconfig)
        cconfig_ui.config2ui(self, cconfig)

    def addItemsToTypeList(self):
        self.cbox_dat_TM1.addItems(['0', '1', '2'])
        self.cbox_dat_TM2.addItems(['0', '1', '2'])
        self.cbox_qua_TQ.addItems(['0', '1', '2'])
        self.cbox_qua_DFC.addItems(['0', '1', '2'])
        self.cbox_idr_TIR.addItems(['0', '1', '2'])
        self.cbox_exp_FCNF.addItems(['0', '1', '2'])
        self.cbox_exp_FEE.addItems(['0', '1', '2'])
        self.cbox_exp_TE.addItems(['0', '1', '2'])

    def setTips(self, table):
        table.setMouseTracking(True)
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            item.setToolTip(item.text())

    def checkSBox(self, table, row, value):
        table.setItem(row, 1, QTableWidgetItem(value))
        table.item(row, 1).setBackground(self.color_normal if Decimal(value) > 0 else self.color_warning)
        return 0 if Decimal(value) > 0 else 1

    def checkPathsExist(self, table, row, list):
        item_num = list.count()
        table.setItem(row, 1, QTableWidgetItem('|'.join([list.item(i).text() for i in range(item_num)])))
        flag = True
        for i in range(item_num):
            if not os.path.exists(list.item(i).text()):
                print(list.item(i).text())
                flag = False
        if item_num == 0:
            flag = False
        table.item(row, 1).setBackground(self.color_normal if flag else self.color_warning)
        return 0 if flag else 1

    def checkPathExist(self, table, row, value):
        table.setItem(row, 1, QTableWidgetItem(value))
        flag = os.path.exists(value)
        table.item(row, 1).setBackground(self.color_normal if flag else self.color_warning)
        return 0 if flag else 1

    def check_pannels(self):
        num_error = 0
        #Ini files
        item_ledt_ini_PA = self.ledt_ini_PA.text()
        num_error += self.checkPathExist(self.tbl_If, 0, item_ledt_ini_PA)
        item_ledt_ini_PE = self.ledt_ini_PE.text()
        num_error += self.checkPathExist(self.tbl_If, 1, item_ledt_ini_PE)
        item_ledt_ini_PM = self.ledt_ini_PM.text()
        num_error += self.checkPathExist(self.tbl_If, 2, item_ledt_ini_PM)
        item_ledt_ini_PG = self.ledt_ini_PG.text()
        num_error += self.checkPathExist(self.tbl_If, 3, item_ledt_ini_PG)

        #Data
        self.tbl_D.setItem(0, 1, QTableWidgetItem(self.cbox_dat_TM1.currentText()))
        item_list_dat_PM1 = self.list_dat_PM1
        num_error += self.checkPathsExist(self.tbl_D, 1, item_list_dat_PM1)
        self.tbl_D.setItem(2, 1, QTableWidgetItem(self.cbox_dat_TM2.currentText()))
        item_list_dat_PM2 = self.list_dat_PM2
        num_error += self.checkPathsExist(self.tbl_D, 3, item_list_dat_PM2)

        #Identification Results
        self.tbl_IR.setItem(0, 1, QTableWidgetItem(self.cbox_idr_TIR.currentText()))
        item_list_idr_PIR = self.list_idr_PIR
        num_error += self.checkPathsExist(self.tbl_IR, 1, item_list_idr_PIR)
        item_sbox_idr_TF = self.sbox_idr_TF.text()
        num_error += self.checkSBox(self.tbl_IR, 2, item_sbox_idr_TF)

        #Quantitation
        self.tbl_Q.setItem(0, 1, QTableWidgetItem(self.cbox_qua_TQ.currentText()))
        item_sbox_qua_RPHWAP = self.sbox_qua_RPHWAP.text()
        num_error += self.checkSBox(self.tbl_Q, 1, item_sbox_qua_RPHWAP)
        self.tbl_Q.setItem(2, 1, QTableWidgetItem(self.ledt_qua_RMRI.text()))
        self.tbl_Q.item(2, 1).setBackground(self.color_normal if self.ledt_qua_RMRI.text() != '' else self.color_warning)
        num_error += 1 if self.ledt_qua_RMRI.text() == '' else 0
        item_sbox_qua_DLRHWIM = self.sbox_qua_DLRHWIM.text()
        num_error += self.checkSBox(self.tbl_Q, 3, item_sbox_qua_DLRHWIM)
        item_sbox_qua_DLPHWAP = self.sbox_qua_DLPHWAP.text()
        num_error += self.checkSBox(self.tbl_Q, 4, item_sbox_qua_DLPHWAP)
        self.tbl_Q.setItem(5, 1, QTableWidgetItem(self.ledt_qua_DLLI.text()))
        self.tbl_Q.item(5, 1).setBackground(self.color_normal if self.ledt_qua_DLLI.text() != '' else self.color_warning)
        num_error += 1 if self.ledt_qua_DLLI.text() == '' else 0
        self.tbl_Q.setItem(6, 1, QTableWidgetItem(self.cbox_qua_DFC.currentText()))
        item_sbox_qua_DFRHWIM = self.sbox_qua_DFRHWIM.text()
        num_error += self.checkSBox(self.tbl_Q, 7, item_sbox_qua_DFRHWIM)
        item_sbox_qua_DFPHWAP = self.sbox_qua_DFPHWAP.text()
        num_error += self.checkSBox(self.tbl_Q, 8, item_sbox_qua_DFPHWAP)

        #Export
        item_ledt_exp_PE = self.ledt_exp_PE.text()
        num_error += self.checkPathExist(self.tbl_E, 0, item_ledt_exp_PE)
        self.tbl_E.setItem(1, 1, QTableWidgetItem(self.cbox_exp_TE.currentText()))
        self.tbl_E.setItem(2, 1, QTableWidgetItem(self.cbox_exp_FCNF.currentText()))
        self.tbl_E.setItem(3, 1, QTableWidgetItem(self.cbox_exp_FEE.currentText()))

        return num_error

    @pyqtSlot(int)
    def on_tab_box_currentChanged(self, index):
        if index == 1:
            num_error = self.check_pannels()
            if num_error==0:
                self.btn_run.setDisabled(False)


    @pyqtSlot()
    def on_btn_run_clicked(self):
        global import_file
        if import_file == '':
            QMessageBox.information(self, '消息', '你需要先导入文件或导出文件', QMessageBox.Yes)
            return
        print(os.path.dirname(os.path.abspath(__file__)) + '\\UltraQuant\\UltraQuant.exe ' + import_file)
        os.system(os.path.dirname(os.path.abspath(__file__)) + '\\UltraQuant\\UltraQuant.exe ' + import_file)

    @pyqtSlot()
    def on_btn_save_clicked(self):
        global import_file
        if import_file == '':
            QMessageBox.information(self, '消息', '你需要先导入文件', QMessageBox.Yes)
            return
        else:
            for config in self.config_list:
                cconfig = config[1]()
                cconfig_file = config[2]()
                cconfig_ui = config[3]()

                cconfig = cconfig_ui.ui2config(self, cconfig)
                cconfig_file.config2file(import_file, cconfig)

            QMessageBox.information(self, '消息', '保存成功', QMessageBox.Yes)

    @pyqtSlot()
    def on_btn_exp_PE_clicked(self):
        path= QFileDialog.getExistingDirectory(self, 'PATH_AA File Select', "/")
        if not os.path.exists(path):
            return
        self.ledt_exp_PE.setText('{}'.format(path))

    @pyqtSlot()
    def on_btn_save_as_clicked(self):
        global import_file
        if len(self.config_list) == 0:
            QMessageBox.warning(self, '消息', '无可供导出的配置文件，请先尝试导入', QMessageBox.Yes)
            return
        file_name, file_type = QFileDialog.getSaveFileName(self, '文件保存', self.cwd, 'Text Files(*.txt)')
        if file_name == '':
            return
        else:
            path_configs = os.path.join(os.path.dirname(file_name), 'params')
            if not os.path.exists(path_configs):
                os.makedirs(path_configs)
            for config in self.config_list:
                cconfig = config[1]()
                cconfig_file = config[2]()
                cconfig_ui = config[3]()
                import_file = file_name

                cconfig = cconfig_ui.ui2config(self, cconfig)
                cconfig_file.config2file(file_name, cconfig)

            QMessageBox.information(self, '消息', '保存成功', QMessageBox.Yes)

    @pyqtSlot()
    def on_btn_import_clicked(self):
        global import_file
        file_name, file_type = QFileDialog.getOpenFileName(self, '配置文件选择', self.cwd, 'Text Files(*.txt)')
        if file_name == '':
            return
        for config in self.config_list:
            cconfig = config[1]()
            cconfig_file = config[2]()
            cconfig_ui = config[3]()

            import_file = file_name
            cconfig = cconfig_file.file2config(file_name, cconfig)
            cconfig_ui.config2ui(self, cconfig)

        QMessageBox.information(self, 'Success', 'Config File Load Success!', QMessageBox.Yes)
        return

    # @pyqtSlot()
    # def on_btn_import_clicked(self):
    #     global import_file
    #     file_name, file_type = QFileDialog.getOpenFileName(self, '配置文件选择', self.cwd, 'Text Files(*.txt)')
    #     if not os.path.exists(file_name) or file_name == '':
    #         return
    #
    #     path_configs = os.path.join(os.path.dirname(file_name), 'params')
    #     if not os.path.exists(path_configs):
    #         QMessageBox.warning(self, '警告', '无可供导入的配置文件，请先尝试重新导入', QMessageBox.Yes)
    #         return
    #     name_configs = os.listdir(path_configs)
    #     self.config_list = list(filter(lambda c: c[0] in name_configs, self.config_list))
    #
    #     for config in self.config_list:
    #         cconfig = config[1]()
    #         cconfig_file = config[2]()
    #         cconfig_ui = config[3]()
    #
    #         config_file_name = os.path.join(path_configs, config[0])
    #         import_file = config_file_name
    #
    #         cconfig = cconfig_file.file2config(config_file_name, cconfig)
    #         cconfig_ui.config2ui(self, cconfig)
    #
    #     QMessageBox.information(self, 'Success', 'Config File Load Success!', QMessageBox.Yes)
    #     return

    @pyqtSlot()
    def on_btn_ini_PA_clicked(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, 'PATH_AA File Select', self.cwd, 'Ini Files(*.ini)')
        if not os.path.exists(file_name) or file_name=='':
            return
        self.ledt_ini_PA.setText('{}'.format(file_name))

    @pyqtSlot()
    def on_btn_ini_PE_clicked(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, 'PATH_ELEMENT File Select', self.cwd, 'Ini Files(*.ini)')
        if not os.path.exists(file_name) or file_name=='':
            return
        self.ledt_ini_PE.setText('{}'.format(file_name))

    @pyqtSlot()
    def on_btn_ini_PM_clicked(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, 'PATH_MOD File Select', self.cwd, 'Ini Files(*.ini)')
        if not os.path.exists(file_name) or file_name=='':
            return
        self.ledt_ini_PM.setText('{}'.format(file_name))

    @pyqtSlot()
    def on_btn_ini_PG_clicked(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, 'PATH_GLYCO File Select', self.cwd, 'Ini Files(*.ini)')
        if not os.path.exists(file_name) or file_name=='':
            return
        self.ledt_ini_PG.setText('{}'.format(file_name))

    @pyqtSlot()
    def on_btn_ini_PL_clicked(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, 'PATH_LINKER File Select', self.cwd, 'Ini Files(*.ini)')
        if not os.path.exists(file_name) or file_name=='':
            return
        self.ledt_ini_PL.setText('{}'.format(file_name))

    @pyqtSlot()
    def on_btn_dat_PM1_add_clicked(self):
        file_names, file_type = QFileDialog.getOpenFileNames(self, 'Files select', self.cwd, 'All Type Files(*)')
        if len(file_names) == 0:
            return
        for file_name in file_names:
            flag = True
            for i in range(self.list_dat_PM1.count()):
                if (self.list_dat_PM1.item(i).text() == file_name):
                    QMessageBox.information(self, 'warning', '该文件路径已存在', QMessageBox.Yes)
                    flag = False
                    break
            if flag:
                self.list_dat_PM1.addItem(file_name)

    @pyqtSlot()
    def on_btn_dat_PM1_delete_clicked(self):
        select_items = list(self.list_dat_PM1.selectedItems())
        if len(select_items) == 0:
            return
        else:
            for i in select_items:
                item_no = self.list_dat_PM1.row(i)
                self.list_dat_PM1.takeItem(item_no)

    @pyqtSlot()
    def on_btn_dat_PM1_clear_clicked(self):
        self.list_dat_PM1.clear()

    @pyqtSlot()
    def on_btn_dat_PM2_add_clicked(self):
        file_names, file_type = QFileDialog.getOpenFileNames(self, 'Files select', self.cwd, 'All Type Files(*)')
        if len(file_names) == 0:
            return
        for file_name in file_names:
            flag = True
            for i in range(self.list_dat_PM2.count()):
                if (self.list_dat_PM2.item(i).text() == file_name):
                    QMessageBox.information(self, 'warning', '该文件路径已存在', QMessageBox.Yes)
                    flag = False
                    break
            if flag:
                self.list_dat_PM2.addItem(file_name)

    @pyqtSlot()
    def on_btn_dat_PM2_delete_clicked(self):
        select_items = list(self.list_dat_PM2.selectedItems())
        if len(select_items) == 0:
            return
        else:
            for i in select_items:
                item_no = self.list_dat_PM2.row(i)
                self.list_dat_PM2.takeItem(item_no)

    @pyqtSlot()
    def on_btn_dat_PM2_clear_clicked(self):
        self.list_dat_PM2.clear()

    @pyqtSlot()
    def on_btn_idr_PIR_add_clicked(self):
        file_names, file_type = QFileDialog.getOpenFileNames(self, 'Files select', self.cwd, 'All Type Files(*)')
        if len(file_names) == 0:
            return
        else:
            for file_name in file_names:
                flag = True
                for i in range(self.list_idr_PIR.count()):
                    if (self.list_idr_PIR.item(i).text() == file_name):
                        QMessageBox.information(self, 'warning', '该文件路径已存在', QMessageBox.Yes)
                        flag = False
                        break
                if flag:
                    self.list_idr_PIR.addItem(file_name)

    @pyqtSlot()
    def on_btn_idr_PIR_delete_clicked(self):
        select_items = list(self.list_idr_PIR.selectedItems())
        if len(select_items) == 0:
            return
        else:
            for i in select_items:
                item_no = self.list_idr_PIR.row(i)
                self.list_idr_PIR.takeItem(item_no)

    @pyqtSlot()
    def on_btn_idr_PIR_clear_clicked(self):
        self.list_idr_PIR.clear()

