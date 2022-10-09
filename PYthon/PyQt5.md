1. anaconda.com접속 후 다운로드
2. anaconda cmd에서 designer 친다
3. python에서 코드를 친다

#code
```
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = "untitled.ui"
form_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
```
