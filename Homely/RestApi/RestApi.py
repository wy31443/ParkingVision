from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import MySQLdb
import os
import json
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')
server_hostname = 'ParkingVision'

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# view the information of all the parking slots
@app.route("/viewall")

# view current parking suggestion
@app.route("/current")
def current():
    dc = databaseConnector()
    var = json.dumps(dc.getCurrentSuggestion())
    dc.close()
    return var

@app.route("/shorttime")
def findshorttime():
    dc = databaseConnector()
    var = json.dumps(dc.getParkingShortTimeSlots())
    dc.close()
    return var

@app.route("/2hr")
def find2hr():
    dc = databaseConnector()
    var = json.dumps(dc.getParking2HrSlots())
    dc.close()
    return var

@app.route("/3hr")
def find3hr():
    dc = databaseConnector()
    var = json.dumps(dc.getParking3HrSlots())
    dc.close()
    return var


@app.route("/")
def index():
    return "Welcome!"

#
# @app.route("/test", methods=['GET', 'POST'])
# def test():
#     dc = databaseConnector()
#     res = json.dumps(dc.getMarkers(0, 0))
#     dc.close()
#     if request.method == 'GET':
#         return res
#     elif request.method == 'POST':
#         return request.form['message']

def update():
    dc = databaseConnector()
    dc.updateSuggestion()
    dc.close()

class databaseConnector:
    # Define connection with MySQL database

    def __init__(self):
        self.mysql = MySQLdb.connect(user="admin", passwd="fred1",
                                     charset='utf8', db="parkingvision")

    def updateSuggestion(self):
        n = 34
        sqlstr = '''SELECT zid,primecontrol,control1,control2,control3 FROM parkingzones WHERE primecontrol like '%hr Parking%' or control1 like '%hr Parking%';'''
        cur = self.mysql.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sqlstr)
        R = cur.fetchall()

    def getParkingShortTimeSlots(self):
        sqlstr = '''SELECT * FROM parkingzones WHERE primecontrol like '%1 hr Parking%' or control1 like '%1 hr Parking%' or primecontrol like '%min Parking%' or control1 like '%min Parking%';'''
        cur = self.mysql.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sqlstr)
        return cur.fetchall()

    def getParking2HrSlots(self):
        sqlstr = '''SELECT * FROM parkingzones WHERE primecontrol like '%2 hr Parking%' or control1 like '%2 hr Parking%';'''
        cur = self.mysql.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sqlstr)
        return cur.fetchall()

    def getParking3HrSlots(self):
        sqlstr = '''SELECT * FROM parkingzones WHERE primecontrol like '%3 hr Parking%' or control1 like '%3 hr Parking%';'''
        cur = self.mysql.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sqlstr)
        return cur.fetchall()

    def getCurrentSuggestion(self):
        sqlstr = '''SELECT * FROM parkingzones WHERE primecontrol like '%hr Parking%' or control1 like '%hr Parking%';'''
        cur = self.mysql.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sqlstr)
        return cur.fetchall()


    def close(self):
        self.mysql.close()

if __name__ == "__main__":
    app.run()
    # Context = ssl._create_default_https_context()
    #app.run('0.0.0.0', port=5000, ssl_context='adhoc')