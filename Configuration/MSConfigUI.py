from .MainWindow import *
from .MSConfig import *
from decimal import Decimal
class CConfigUiOne:
    def config2ui(self, ui, config):
        # [Ini files]
        ui.ledt_ini_PA.setText(config.INI_PATH_AA)
        ui.ledt_ini_PE.setText(config.INI_PATH_ELEMENT)
        ui.ledt_ini_PM.setText(config.INI_PATH_MOD)
        ui.ledt_ini_PG.setText(config.INI_PATH_GLYCO)

        # [Data]
        ui.list_dat_PM1.clear()
        ui.list_dat_PM1.addItems(config.PATH_MS1)
        ui.cbox_dat_TM1.setCurrentIndex(config.TYPE_MS1_LIST.index(config.TYPE_MS1))
        ui.list_dat_PM2.clear()
        ui.list_dat_PM2.addItems(config.PATH_MS2)
        ui.cbox_dat_TM2.setCurrentIndex(config.TYPE_MS2_LIST.index(config.TYPE_MS2))

        # [Identification results]
        ui.list_idr_PIR.clear()
        ui.list_idr_PIR.addItems(config.PATH_IDENTIFICATION_RESULT)
        ui.cbox_idr_TIR.setCurrentIndex(config.TYPE_IDENTIFICATION_RESULT_LIST.index(config.TYPE_IDENTIFICATION_RESULT))
        ui.sbox_idr_TF.setValue(Decimal(config.THRESHOLD_FDR if config.THRESHOLD_FDR!='' else '0'))

        # [Quatitation]
        ui.ledt_qua_RMRI.setText(config.RI_MASS_REPORT_ION)
        ui.sbox_qua_RPHWAP.setValue(Decimal(config.RI_PPM_HALF_WIN_ACCURACY_PEAK if config.RI_PPM_HALF_WIN_ACCURACY_PEAK!='' else '0'))
        ui.sbox_qua_DFRHWIM.setValue(Decimal(config.DDALF_RT_HALF_WIN_IN_MIN if config.DDALF_RT_HALF_WIN_IN_MIN!='' else '0'))
        ui.sbox_qua_DFPHWAP.setValue(Decimal(config.DDALF_PPM_HALF_WIN_ACCURACY_PEAK if config.DDALF_PPM_HALF_WIN_ACCURACY_PEAK!='' else '0'))
        ui.sbox_qua_DLRHWIM.setValue(Decimal(config.DDALL_RT_HALF_WIN_IN_MIN if config.DDALL_RT_HALF_WIN_IN_MIN!='' else '0'))
        ui.sbox_qua_DLPHWAP.setValue(Decimal(config.DDALL_PPM_HALF_WIN_ACCURACY_PEAK if config.DDALL_PPM_HALF_WIN_ACCURACY_PEAK!='' else '0'))
        ui.ledt_qua_DLLI.setText(config.DDALL_LABEL_INFO)
        ui.cbox_qua_DFC.setCurrentIndex(config.DDALL_FLAG_CALIBRATION_18O_LIST.index(config.DDALL_FLAG_CALIBRATION_18O))

        # [Export]
        ui.ledt_exp_PE.setText(config.PATH_EXPORT)
        ui.cbox_exp_TE.setCurrentIndex(config.TYPE_EXPORT_LIST.index(config.TYPE_EXPORT))
        ui.cbox_exp_FCNF.setCurrentIndex(config.FLAG_CREATE_NEW_FOLDER_LIST.index(config.FLAG_CREATE_NEW_FOLDER))
        ui.cbox_exp_FEE.setCurrentIndex(config.FLAG_EXPORT_EVIDENCE_LIST.index(config.FLAG_EXPORT_EVIDENCE))

        return ui

    def ui2config(self, ui, config):
        # [Ini files]
        config.INI_PATH_AA = ui.ledt_ini_PA.text()
        config.INI_PATH_ELEMENT = ui.ledt_ini_PE.text()
        config.INI_PATH_MOD = ui.ledt_ini_PM.text()
        config.INI_PATH_GLYCO = ui.ledt_ini_PG.text()
        # item_num = ui.list_ini_PE_2.count()
        # config.INI_PATH_ELEMENT = [ui.list_ini_PE_2.item(i).text() for i in range(item_num)]
        # item_num = ui.list_ini_PM_2.count()
        # config.INI_PATH_MOD = [ui.list_ini_PM_2.item(i).text() for i in range(item_num)]
        # item_num = ui.list_ini_PG_2.count()
        # config.INI_PATH_GLYCO = [ui.list_ini_PG_2.item(i).text() for i in range(item_num)]
        # item_num = ui.list_ini_PL_2.count()
        # config.INI_PATH_LINKER = [ui.list_ini_PL_2.item(i).text() for i in range(item_num)]

        # [Data]
        item_num = ui.list_dat_PM1.count()
        config.PATH_MS1 = [ui.list_dat_PM1.item(i).text() for i in range(item_num)]
        config.TYPE_MS1 = ui.cbox_dat_TM1.currentText()
        item_num = ui.list_dat_PM2.count()
        config.PATH_MS2 = [ui.list_dat_PM2.item(i).text() for i in range(item_num)]
        config.TYPE_MS2 = ui.cbox_dat_TM2.currentText()

        # [Identification results]
        item_num = ui.list_idr_PIR.count()
        config.PATH_IDENTIFICATION_RESULT = [ui.list_idr_PIR.item(i).text() for i in range(item_num)]
        config.TYPE_IDENTIFICATION_RESULT = ui.cbox_idr_TIR.currentText()
        config.THRESHOLD_FDR = ui.sbox_idr_TF.text()

        # [Quantitation]
        config.TYPE_QUANT = ui.cbox_qua_TQ.currentText()
        config.RI_MASS_REPORT_ION = ui.ledt_qua_RMRI.text()
        config.RI_PPM_HALF_WIN_ACCURACY_PEAK = ui.sbox_qua_RPHWAP.text()
        config.DDALF_RT_HALF_WIN_IN_MIN = ui.sbox_qua_DFRHWIM.text()
        config.DDALF_PPM_HALF_WIN_ACCURACY_PEAK = ui.sbox_qua_DFPHWAP.text()
        config.DDALL_RT_HALF_WIN_IN_MIN = ui.sbox_qua_DLRHWIM.text()
        config.DDALL_PPM_HALF_WIN_ACCURACY_PEAK = ui.sbox_qua_DLPHWAP.text()
        config.DDALL_LABEL_INFO = ui.ledt_qua_DLLI.text()
        config.DDALL_FLAG_CALIBRATION_18O = ui.cbox_qua_DFC.currentText()

        # [Export]
        config.PATH_EXPORT = ui.ledt_exp_PE.text()
        config.TYPE_EXPORT = ui.cbox_exp_TE.currentText()
        config.FLAG_CREATE_NEW_FOLDER = ui.cbox_exp_FCNF.currentText()
        config.FLAG_EXPORT_EVIDENCE = ui.cbox_exp_FEE.currentText()


        return config
