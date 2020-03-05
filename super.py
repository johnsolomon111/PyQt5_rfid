from PyQt5 import QtWidgets, uic
import sqlite3

app = QtWidgets.QApplication([])
dlg = uic.loadUi("super.ui")
conn = sqlite3.connect('rfid.db')
cur = conn.cursor()

def addUser():
	new_name = dlg.lineEdit.text()
	new_idno = dlg.lineEdit_3.text()
	new_rfid = dlg.lineEdit_2.text()
	val = (str(new_name),str(new_idno),str(new_rfid),int(0))
	sql = "INSERT into users (name,idno,rfid,points) VALUES (?,?,?,?)"
	cur.execute(sql,val)
	conn.commit()
	dlg.lineEdit.setText("")
	dlg.lineEdit_2.setText("")
	dlg.lineEdit_3.setText("")
	dlg.label.setText("User Added")
	loadData()
	

def addPoints():
	rfid = dlg.lineEdit_5.text()
	query = "SELECT * FROM users WHERE rfid='"+rfid+"'"
	cur.execute(query)
	data = cur.fetchone()
	if data is not None:
		points = (int(data[4]) + int(dlg.lineEdit_4.text()),)
		sql = "UPDATE users SET points=? WHERE rfid='"+rfid+"'"
		cur.execute(sql,points)
		conn.commit()
		dlg.label_4.setText("Points Added")
		dlg.lineEdit_5.setText("")
		dlg.lineEdit_4.setText("")
		loadData()

	else:
		dlg.label_4.setText("User Not Found")
		dlg.lineEdit_5.setText("")
		dlg.lineEdit_4.setText("")

def loadData():

	query = "SELECT * FROM users"
	result = conn.execute(query)
	dlg.tableWidget.setRowCount(0)
	for row_number, row_data in enumerate(result):
		dlg.tableWidget.insertRow(row_number)
		for column_number, data in enumerate(row_data):
			dlg.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
loadData()

dlg.lineEdit_2.returnPressed.connect(addUser)
dlg.lineEdit_5.returnPressed.connect(addPoints)

dlg.show()
app.exec()