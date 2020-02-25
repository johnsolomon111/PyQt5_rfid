from PyQt5 import QtWidgets, uic


def get_user_info():
	dlg.label_5.setText("John Benedict Solomon")
	dlg.label_6.setText("2015-1227")

app = QtWidgets.QApplication([])
dlg = uic.loadUi("rfid.ui")

dlg.lineEdit.returnPressed.connect(get_user_info)

dlg.show()
app.exec()