from PyQt5 import QtWidgets, uic
import sqlite3
conn = sqlite3.connect('rfid.db')
cur = conn.cursor()

def get_user_info():
	rfid = dlg.lineEdit.text()
	query = "SELECT * FROM users WHERE rfid='"+rfid+"'"
	cur.execute(query)
	data = cur.fetchone()
	if data is not None:
		if data[4] > 0:
			bal = int(data[4]) - 1
			val = (bal,)
			dlg.label_5.setText(data[1])
			dlg.label_6.setText(data[2])
			dlg.label_8.setText(str(bal))
			sql = "UPDATE users SET points=? WHERE rfid='"+rfid+"'"
			cur.execute(sql,val)
			conn.commit()
			dlg.lineEdit.setText("")
			dlg.label_9.setText("Authorized")
		else:
			dlg.label_5.setText(data[1])
			dlg.label_6.setText(data[2])
			dlg.label_8.setText("0")
			dlg.label_9.setText("Insufficient points")
			dlg.lineEdit.setText("")
	else:
		dlg.label_5.setText("None")
		dlg.label_6.setText("None")
		dlg.label_9.setText("Unauthorized Personnel")
		dlg.lineEdit.setText("")



app = QtWidgets.QApplication([])
dlg = uic.loadUi("rfid.ui")

dlg.lineEdit.returnPressed.connect(get_user_info)

dlg.show()
app.exec()