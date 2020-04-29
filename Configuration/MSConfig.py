class CConfigOne(object):
    # [Ini files]
    INI_PATH_ELEMENT = ''
    INI_PATH_AA = ''
    INI_PATH_MOD = ''
    INI_PATH_GLYCO = ''

    # [Data]
    PATH_MS1 = []
    TYPE_MS1_LIST = ['0', '1', '2']
    TYPE_MS1 = '0'
    PATH_MS2 = []
    TYPE_MS2_LIST = ['0', '1', '2']
    TYPE_MS2 = '0'

    # [Identification results]
    PATH_IDENTIFICATION_RESULT = []
    TYPE_IDENTIFICATION_RESULT_LIST = ['0', '1', '2']
    TYPE_IDENTIFICATION_RESULT = '1'
    THRESHOLD_FDR = '0.01'

    # [Quantitation]
    TYPE_QUANT_LIST = ['0', '1', '2']
    TYPE_QUANT = '0'
    RI_MASS_REPORT_ION = "\'127.11\', \'130.11\'"
    RI_PPM_HALF_WIN_ACCURACY_PEAK = '1000'
    DDALF_RT_HALF_WIN_IN_MIN = '2'
    DDALF_PPM_HALF_WIN_ACCURACY_PEAK = '20'
    DDALL_RT_HALF_WIN_IN_MIN = '2'
    DDALL_PPM_HALF_WIN_ACCURACY_PEAK = '20'
    DDALL_LABEL_INFO = "2 | NONE | AA:R: N:15N & AA: R:C: 13C & AA: K:C: 13C & AA: K:N: 15N |"
    DDALL_FLAG_CALIBRATION_18O_LIST = ['0', '1', '2']
    DDALL_FLAG_CALIBRATION_18O = '0'

    # [Export]
    PATH_EXPORT = 'D:\\test\\'
    TYPE_EXPORT_LIST = ['0', '1', '2']
    TYPE_EXPORT = '1'
    FLAG_CREATE_NEW_FOLDER_LIST = ['0', '1', '2']
    FLAG_CREATE_NEW_FOLDER = '0'
    FLAG_EXPORT_EVIDENCE_LIST = ['0', '1', '2']
    FLAG_EXPORT_EVIDENCE = '0'
