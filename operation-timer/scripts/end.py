from datetime import datetime
from qgis.gui import QgsMessageBar
from qgis.utils import *

algTimeEnd = datetime.now()
alg.end = algTimeEnd
totalTime = (alg.end-alg.start).total_seconds()
iface.messageBar().pushMessage("Time:", "Process took {0} seconds to complete".format(totalTime), level=QgsMessageBar.INFO)