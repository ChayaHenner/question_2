from flask import Flask , request,jsonify
from datetime import datetime
import json 
import sqlite3


app = Flask(__name__)

def get(request_num , id):
    request_query=["FIRST_NAME ,LAST_NAME","ADDR_CITY,ADDR_ST,ADDR_ST_NUM","DOB","PHONE, CELL_PHONE"]#continue
    conn = sqlite3.connect('Employees.db')
    c = conn.cursor()
    c.execute("select ? from EMPLOYEES WHERE ID= ?",[request_query[ request_num ], id]) #do try catch in case...
    rows=c.fetchall()
    c.close()
    conn.close()
    return jsonify(rows)

# #will get values by given id

@app.route('/data/<int:id>',methods=['GET'])
def getName(id):
    return get(0,id)

@app.route('/data/<int:id>',methods=['GET'])
def getAdrress(id):
    return get(1,id)

@app.route('/data/<int:id>',methods=['GET'])
def getDOB(id):
    return get(3,id)

@app.route('/data/<int:id>',methods=['GET'])
def getPhoneNumber():
    return get(4,id)

@app.route('/data/<int:id>',methods=['GET'])
def getCovidDates(id):
    conn = sqlite3.connect('Employees.db')
    c = conn.cursor()
    c.execute("select VAC_NUM , DATE_VAC, VAC_MAN from COVID_VAC WHERE ID= ?",(id,) ) #do try catch ,add in order of vac num
    rows=c.fetchall()
    c.close()
    conn.close()
    return jsonify(rows)

@app.route('/data/<int:id>',methods=['GET'])
def getCovidVacs(id):
    conn = sqlite3.connect('Employees.db')
    c = conn.cursor()
    c.execute("select DATE_POSITIVE ,DATE_RECOVERY from COVID_EMPLOYEE WHERE ID= ?", (id,) ) #do try catch ,also if values null return "no date"
    rows=c.fetchall()
    c.close()
    conn.close()
    return jsonify(rows)
    




# @app.route('/data',methods=['POST'])
# def post():
#     data=request.json
#     conn = sqlite3.connect('Employees.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO EMPLOYEES VALUES(?,?)",(data["name"],data["phonenumber"]))
#     rows=c.fetchall()
#     c.close()
#     conn.close()
#     return "data added to database"

# #post new worker
# app.route('/data',methods=['POST'])
# def postNew():
#     data=request.json
#     conn = sqlite3.connect('Employees.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO EMPLOYEES VALUES(?,?,?,?,?)",(data["id"],data["firstname"],data["lastname"],data["city"],data["street"],data["streetnum"],data["DOB"],data["phone"],data["cellsphone"]))
#     rows=c.fetchall()
#     c.close()
#     conn.close()
#     return "data added to database"

# #post new shot
# app.route('/data',methods=['POST'])
# def postShot():
#     data=request.json
#     conn = sqlite3.connect('Employees.db')
#     c = conn.cursor()
#     c.execute("select MAX(VAC_NUM)  from COVID_VAC WHERE ID= ?",id) #do try catch ,add in order of vac num
#     rows=c.fetchall() #number of vac update it

#     c.execute("INSERT INTO COVID_VAC VALUES(?,?,?,?)",[data["id"],str(datetime.now())[:19],data["vacman"],data["vacnum"]])
#     rows=c.fetchall()
#     c.close()
#     conn.close()
#     return "data added to database"

if __name__=='__main__':
    app.run()