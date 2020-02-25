from PyQt5 import QtWidgets, uic
from functions import *


def get_user_info():
    rfid = dlg.lineEdit.text()
    data = get_user(str(rfid))

    if data is not None:
        dlg.label_5.setText(data[1])
        dlg.label_6.setText(data[2])
        dlg.label_4.setText("Authorized Personel!")
    else:
        dlg.label_4.setText("Unauthorized!")

app = QtWidgets.QApplication([])
dlg = uic.loadUi("rfid.ui")

dlg.lineEdit.returnPressed.connect(get_user_info)

dlg.show()
app.exec()