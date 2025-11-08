import sys
import subprocess

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

install_and_import("PyQt5")
install_and_import("PyQt5.QtWidgets")
install_and_import("PyQt5.QtCore")
install_and_import("PyQt5.QtWebEngineWidgets")

from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MinimalBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genuis")
        self.resize(900, 600)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://genius.com/"))
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MinimalBrowser()
    window.show()
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        sys.exit(0)