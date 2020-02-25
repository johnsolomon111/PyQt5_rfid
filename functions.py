import sqlite3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

conn = sqlite3.connect('rfid.db') # connecting to database

 # creating cursor to control the database

def get_user(rfid):
    c = conn.cursor()
    sql = "SELECT * FROM users WHERE rfid=?"
    task = (str(rfid),)
    c.execute(sql,task)
    row = c.fetchone()

    return row