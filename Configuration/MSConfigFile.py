from Configuration.MSConfig import *
from Configuration.MSTool import *
import configparser


class CConfigFileOne():
    def config2file(self, path, config):
        c = AutoConfigParser()
        # [Ini files]
        c.add_section('Ini files')
        c.set('Ini files', 'INI_PATH_ELEMENT', str(config.INI_PATH_ELEMENT).replace("/", "\\"))
        c.set('Ini files', 'INI_PATH_AA', str(config.INI_PATH_AA).replace("/", "\\"))
        c.set('Ini files', 'INI_PATH_MOD', str(config.INI_PATH_MOD).replace("/", "\\"))
        c.set('Ini files', 'INI_PATH_GLYCO', str(config.INI_PATH_GLYCO).replace("/", "\\"))

        # [Data]
        c.add_section('Data')
        c.set('Data', 'PATH_MS1', '|'.join(config.PATH_MS1).replace("/", "\\"))
        c.set('Data', 'TYPE_MS1', str(config.TYPE_MS1))
        c.set('Data', 'PATH_MS2', '|'.join(config.PATH_MS2).replace("/", "\\"))
        c.set('Data', 'TYPE_MS2', str(config.TYPE_MS2))

        # [Identification results]
        c.add_section('Identification results')
        c.set('Identification results', 'PATH_IDENTIFICATION_RESULT', '|'.join(config.PATH_IDENTIFICATION_RESULT).replace("/", "\\"))
        c.set('Identification results', 'TYPE_IDENTIFICATION_RESULT', str(config.TYPE_IDENTIFICATION_RESULT))
        c.set('Identification results', 'THRESHOLD_FDR', str(config.THRESHOLD_FDR))

        # [Quantitation]
        c.add_section('Quantitation')
        c.set('Quantitation', 'TYPE_QUANT', str(config.TYPE_QUANT))
        c.set('Quantitation', 'RI_MASS_REPORT_ION', str(config.RI_MASS_REPORT_ION))
        c.set('Quantitation', 'RI_PPM_HALF_WIN_ACCURACY_PEAK', str(config.RI_PPM_HALF_WIN_ACCURACY_PEAK))
        c.set('Quantitation', 'DDALF_RT_HALF_WIN_IN_MIN', str(config.DDALF_RT_HALF_WIN_IN_MIN))
        c.set('Quantitation', 'DDALF_PPM_HALF_WIN_ACCURACY_PEAK', str(config.DDALF_PPM_HALF_WIN_ACCURACY_PEAK))
        c.set('Quantitation', 'DDALL_RT_HALF_WIN_IN_MIN', str(config.DDALL_RT_HALF_WIN_IN_MIN))
        c.set('Quantitation', 'DDALL_PPM_HALF_WIN_ACCURACY_PEAK', str(config.DDALL_PPM_HALF_WIN_ACCURACY_PEAK))
        c.set('Quantitation', 'DDALL_LABEL_INFO', str(config.DDALL_LABEL_INFO))
        c.set('Quantitation', 'DDALL_FLAG_CALIBRATION_18O', str(config.DDALL_FLAG_CALIBRATION_18O))

        # [Export]
        c.add_section('Export')
        c.set('Export', 'PATH_EXPORT', str(config.PATH_EXPORT).replace("/", "\\"))
        c.set('Export', 'TYPE_EXPORT', str(config.TYPE_EXPORT))
        c.set('Export', 'FLAG_CREATE_NEW_FOLDER', str(config.FLAG_CREATE_NEW_FOLDER))
        c.set('Export', 'FLAG_EXPORT_EVIDENCE', str(config.FLAG_EXPORT_EVIDENCE))

        with open(path, 'w+', encoding='utf-8') as f:
            c.write(f)
        with open(path, 'r') as f:
            context = f.read()
        f1 = open(path, 'w')
        print(context)
        f1.write(context.replace(" = ", "="))
        f1.close()

    def file2config(self, path, config):
        c = AutoConfigParser()
        c.read(path, encoding='utf-8')
        c.remove_note()

        # [Ini files]
        config.INI_PATH_ELEMENT = c.get('Ini files', 'INI_PATH_ELEMENT').replace("\\", "/")
        config.INI_PATH_AA = c.get('Ini files', 'INI_PATH_AA').replace("\\", "/")
        config.INI_PATH_MOD = c.get('Ini files', 'INI_PATH_MOD').replace("\\", "/")
        config.INI_PATH_GLYCO = c.get('Ini files', 'INI_PATH_GLYCO').replace("\\", "/")

        # [Data]
        config.PATH_MS1 = c.get('Data', 'PATH_MS1').replace("\\", "/").split('|')
        if config.PATH_MS1 == ['']:
            config.PATH_MS1 = []
        config.TYPE_MS1 = c.get('Data', 'TYPE_MS1')
        config.PATH_MS2 = c.get('Data', 'PATH_MS2').replace("\\", "/").split('|')
        if config.PATH_MS2 == ['']:
            config.PATH_MS2 = []
        config.TYPE_MS2 = c.get('Data', 'TYPE_MS2')

        # [Identification results]
        config.PATH_IDENTIFICATION_RESULT = c.get('Identification results', 'PATH_IDENTIFICATION_RESULT').replace("\\", "/").split('|')
        if config.PATH_IDENTIFICATION_RESULT == ['']:
            config.PATH_IDENTIFICATION_RESULT = []
        config.TYPE_IDENTIFICATION_RESULT = c.get('Identification results', 'TYPE_IDENTIFICATION_RESULT')
        config.THRESHOLD_FDR = c.get('Identification results', 'THRESHOLD_FDR')

        # [Quantitation]
        config.TYPE_QUANT = c.get('Quantitation', 'TYPE_QUANT')
        config.RI_MASS_REPORT_ION = c.get('Quantitation', 'RI_MASS_REPORT_ION')
        config.RI_PPM_HALF_WIN_ACCURACY_PEAK = c.get('Quantitation', 'RI_PPM_HALF_WIN_ACCURACY_PEAK')
        config.DDALF_RT_HALF_WIN_IN_MIN = c.get('Quantitation', 'DDALF_RT_HALF_WIN_IN_MIN')
        config.DDALF_PPM_HALF_WIN_ACCURACY_PEAK = c.get('Quantitation', 'DDALF_PPM_HALF_WIN_ACCURACY_PEAK')
        config.DDALL_RT_HALF_WIN_IN_MIN = c.get('Quantitation', 'DDALL_RT_HALF_WIN_IN_MIN')
        config.DDALL_PPM_HALF_WIN_ACCURACY_PEAK = c.get('Quantitation', 'DDALL_PPM_HALF_WIN_ACCURACY_PEAK')
        config.DDALL_LABEL_INFO = c.get('Quantitation', 'DDALL_LABEL_INFO')
        config.DDALL_FLAG_CALIBRATION_18O = c.get('Quantitation', 'DDALL_FLAG_CALIBRATION_18O')

        # [Export]
        config.PATH_EXPORT = c.get('Export', 'PATH_EXPORT').replace("\\", "/")
        config.TYPE_EXPORT = c.get('Export', 'TYPE_EXPORT')
        config.FLAG_CREATE_NEW_FOLDER = c.get('Export', 'FLAG_CREATE_NEW_FOLDER')
        config.FLAG_EXPORT_EVIDENCE = c.get('Export', 'FLAG_EXPORT_EVIDENCE')

        return config


