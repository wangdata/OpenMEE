################
#              #
# George Dietz #
# CEBM@Brown   #
#              #
################

import sys
import time

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from PyQt4.QtGui import QPixmap, QSplashScreen

import python_to_R
import main_form
import icons_rc

SPLASH_DISPLAY_TIME = 0

def load_R_libraries(app, splash=None):
    ''' Loads the R libraries while updating the splash screen'''
    
    rloader = python_to_R.RlibLoader()

    splash.showMessage("Loading metafor\n....")
    app.processEvents()
    rloader.load_metafor()
    
    splash.showMessage("Loading openmetar\n........")
    app.processEvents()
    rloader.load_openmetar()
    
    splash.showMessage("Loading igraph\n............")
    app.processEvents()
    rloader.load_igraph()
    
    splash.showMessage("Loading grid\n................")
    app.processEvents()
    rloader.load_grid()
    
def start(open_file_path=None):
    app = QtGui.QApplication(sys.argv)
    
    splash_pixmap = QPixmap(":/splash/splash.png")
    splash = QSplashScreen(splash_pixmap)
    #splash = QSplashScreen( QPixmap(300, 200) )
    splash.show()
    app.processEvents()
    
    time.sleep(1)
    
    splash_starttime = time.time()
    load_R_libraries(app, splash)
    
    # Show splash screen for at least SPLASH_DISPLAY_TIME seconds
    time_elapsed  = time.time() - splash_starttime
    print("It took %s seconds to load the R libraries" % str(time_elapsed))
    if time_elapsed < SPLASH_DISPLAY_TIME: # seconds
        print("Going to sleep for %f seconds" % float(SPLASH_DISPLAY_TIME-time_elapsed))
        QThread.sleep(int(SPLASH_DISPLAY_TIME-time_elapsed))
        print("woke up")

    # create and show the main window
    form = main_form.MainForm()
    form.show()
    form.raise_()
    if open_file_path:
        form.open(open_file_path)
        
    # Close the splash screen
    splash.finish(form)
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        if sys.argv[1][-3:len(sys.argv[1])]=="ome":
            start(open_file_path=sys.argv[1])
    except IndexError:
        pass
    start()