from flask import Flask , request,jsonify
from datetime import datetime
import json 
import sqlite3


app = Flask(__name__)

@app.route('/data/<int:id>',methods=['GET'])
def getCovidDates(id):
    conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
    c = conn.cursor()
    try:
        c.execute("select DATE_POSITIVE || ' - ' || DATE_RECOVERY from COVID_EMPLOYEE WHERE ID= ?", (id,) ) #do try catch ,also if values null return "no date"
        rows=c.fetchall()
        if rows==[]:
            print("404")
        else: print(rows,"200")
    except Exception as e:
        print("500")
    c.close()
    conn.close()
    return (rows)

@app.route('/data/<int:id>',methods=['GET'])
def getAll(code):
    if code=='0000':
        conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
        c = conn.cursor()
        try:
            c.execute("""select   FIRST_NAME || ' ' ||LAST_NAME , ADDR_ST || ' ' || ADDR_ST_NUM || ' , ' || ADDR_CITY , DOB , PHONE || ' , ' || CELL_PHONE ,DATE_POSITIVE ,DATE_RECOVERY,DATE_VAC,VAC_MAN,VAC_NUM 
                        from EMPLOYEE 
                        INNER JOIN COVIDVAC on  COVIDVAC.EMPLOYEE_ID= EMPLOYEE.ID 
                        ORDER BY LAST_NAME ASC,VAC_NUM ASC """) 
            # data=[
            #     dict(name=row[0],address=row[1],phone=row[2],DATE_POSITIVE=row[3] ,DATE_RECOVERY=row[4],DATE_VAC=row[5],VAC_MAN=row[6],VAC_NUM=row[7])
            #     for row in c.fetchall
            #     ]
            # if data is not None:
            #     return jsonify(data)
            rows=c.fetchall()
            if rows==[]:
                print("404")
            else: print(rows,"200")
        except Exception as e:
            print("500")
        c.close()
        conn.close()
    else:  print("400","incorrect code")   

    def get(request_num , id):
        request_query=["FIRST_NAME || ' ' ||LAST_NAME" , "ADDR_ST || ' ' || ADDR_ST_NUM || ' , ' || ADDR_CITY","DOB","PHONE || ' , ' ||CELL_PHONE"]#continue
        conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
        c = conn.cursor()
        try:
            c.execute("select "+request_query[request_num]+" from EMPLOYEE WHERE ID= ?",(id,) ) #do try catch in case...
            rows=c.fetchall()
            c.close()
            conn.close()#problem its here?
            if rows==[]:
                return "not found" ,404
            else: return jsonify(rows[0]),200
        except Exception as e:
            return "internal server error",500
        
        