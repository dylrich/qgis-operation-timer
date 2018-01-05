from PyQt4.QtCore import QSettings

class timePlugin:
    def __init__(self, iface):
        self.iface = iface
    def initGui(self):
        import os 
        path = os.path.dirname(os.path.realpath(__file__))
        settings = QSettings()
        settings.setValue("Processing/Configuration/POST_EXECUTION_SCRIPT", path + "\scripts\end.py")
        settings.setValue("Processing/Configuration/PRE_EXECUTION_SCRIPT", path + "\scripts\start.py")
    def unload(self):
        settings = QSettings()
        settings.setValue("Processing/Configuration/POST_EXECUTION_SCRIPT", "")
        settings.setValue("Processing/Configuration/PRE_EXECUTION_SCRIPT", "")
