from flask import Flask , request,jsonify
from datetime import datetime
import json 
import sqlite3
DB_PATH=r'C:\Users\This_user\Desktop\hadassim_project\question_2_update\server.db'

app = Flask(__name__)
# app.config["DEBUG"]=True

#good        
@app.route('/covid_vacs/<id>')
def getCovidVacs(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("select VAC_NUM , DATE_VAC, VAC_MAN from COVIDVAC WHERE employee_ID= ?  ORDER BY VAC_NUM ASC",(id,) ) 
        vacs=[
            dict(vac_num=row[0],date_vac=row[1],vac_man=row[2])
            for row in c.fetchall()
        ]
        if vacs !=[]:
            return jsonify(vacs), 200
        else: 
            c.execute("select DATE_POSITIVE || ' - ' || DATE_RECOVERY from EMPLOYEE WHERE ID= ?", (id,) ) 
            rows=c.fetchall()
            if rows==[]:
                return "error. there is no worker with that id" ,404 
            else:  return "this employee did not get any vacs" ,200
        
    except Exception as e:
       return "internal server error" ,500 
    c.close()
    conn.close() 

#good
@app.route('/covid_dates/<id>')
def getCovidDates(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("select DATE_POSITIVE || ' - ' || DATE_RECOVERY from EMPLOYEE WHERE ID= ?", (id,) ) 
        rows=c.fetchall()
        if rows==[]:
            return "error. there is no worker with that id" ,404 
        else:
             return jsonify(rows[0][0]) ,200 
    except Exception as e:
        c.close()
        conn.close()
        return "internal server error" ,500      

@app.route('/get_column/<id>/<request_num>')
def get(id,request_num):
    # return "hii",200
    request_query=["FIRST_NAME || ' ' ||LAST_NAME" , "ADDR_ST || ' ' || ADDR_ST_NUM || ' , ' || ADDR_CITY","DOB","PHONE || ' , ' ||CELL_PHONE"]#continue
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if(str(request_num)>3):
        return "error. invalid coulmn" ,404 
    try:
        c.execute("select "+request_query[int(request_num)]+" from EMPLOYEE WHERE ID=?",(str(id),) )#,(request_query[request_num],))#str(id),) ) #do try catch in case...
        rows=c.fetchall()
        c.close()
        conn.close()
        if rows==[]:
            return "error. there is no worker with that id" ,404 
        else: return jsonify(rows[0][0]) ,200 
    except Exception as e:
         c.close()
         conn.close()
         return "internal server error" ,500   
     
       
  
#good.fix should give all  
@app.route('/all/<code>')          
def getAll(code):
    if code=='8068':
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        try:
            c.execute("""select   FIRST_NAME || ' ' ||LAST_NAME , ADDR_ST || ' ' || ADDR_ST_NUM || ' , ' || ADDR_CITY , DOB , PHONE || ' , ' || CELL_PHONE ,DATE_POSITIVE ,DATE_RECOVERY,DATE_VAC,VAC_MAN,VAC_NUM 
                        from EMPLOYEE 
                        INNER JOIN COVIDVAC on  COVIDVAC.EMPLOYEE_ID= EMPLOYEE.ID 
                        ORDER BY LAST_NAME ASC,VAC_NUM ASC """) 
            
            employees = [
                dict(name=row[0],address=row[1],dob=row[2],phonenumbers=row[3],datepositive=row[4],daterecovery=row[5],datevac=row[6],vacman=row[7],vacnum=row[8])
                for row in c.fetchall()
            ]
            if employees is not None:
                return jsonify(employees), 200 #fix should return all ppl not just one

        except Exception as e:
            return "internal server error" ,500 
        c.close()
        conn.close()
    else:  
        return jsonify("wrong code") ,400  


@app.route('/new_employee', methods=['POST'])
def post_data_2_2():

    
    ID = request.args['ID']
    FIRST_NAME = request.args['FIRST_NAME']
    LAST_NAME = request.args['LAST_NAME']
    ADDR_CITY = request.args['ADDR_CITY']
    ADDR_ST_NUM = request.args['ADDR_ST_NUM']
    ADDR_ST = request.args['ADDR_ST']
    DOB= request.args['DOB']
    PHONE = request.args['PHONE']
    CELL_PHONE = request.args['CELL_PHONE']
    # DATE_POSITIVE = request.args['DATE_POSITIVE']
    # DATE_RECOVERY = request.args['DATE_RECOVERY']
    
   
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
         if check_values(ID,FIRST_NAME,LAST_NAME,ADDR_CITY,ADDR_ST, ADDR_ST_NUM,DOB,PHONE,CELL_PHONE):
            c.execute("INSERT INTO EMPLOYEE (id, first_name,last_name,ADDR_CITY,ADDR_ST,ADDR_ST_NUM,DOB,PHONE,CELL_PHONE) VALUES (?,?,?,?,?,?,?,?,?)", (str(id), first_name,LAST_NAME,ADDR_CITY,ADDR_ST,ADDR_ST_NUM,DOB,PHONE,CELL_PHONE))
    except Exception as e:
            conn.commit()
            conn.close()
            return "internal server error" ,500 

    conn.commit()
    conn.close()
    return "all good iyH" ,200       



    
#id,firstname,lastname,city,street,streetnum,DOB,phone,cellphone    
    
#check values r ok
def check_values(id,firstname,lastname,city,street,streetnum,DOB,phone,cellphone ):
    correct=True
    if len(id)>9 or id.isnumeric()==False or phone.isnumeric()==False or streetnum.isnumeric()==False or id.isnumeric()==False :#,c or dob incorrect
        correct=False
    return correct

@app.route('/chaya', methods=['POST'])
def post_data():
    data = request.get_json()  # get the JSON data from the request
    # do something with the data, e.g. save to a database
    return jsonify({'message': 'Data received successfully!'})

#good post
@app.route('/new_vac', methods=['POST'])
def post_data_2():
    # data = {}
    # for key, value in request.args.items():
    #     data[key] = value

    id = request.args['id']
    vacman = request.args['vacman']
    print(request)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("select MAX(VAC_NUM)  from COVIDVAC WHERE EMPLOYEE_ID = ?",(str(id),)) 
    #c.execute("select MAX(VAC_NUM)  from COVIDVAC WHERE EMPLOYEE_ID = ?",(str(data["id"]),)) 

    num=int(c.fetchone()[0]) #number of vac update it
    c.execute("INSERT INTO COVIDVAC VALUES(?,?,?,?)",(str(id),str(datetime.now())[:10],vacman,num+1,))
    #c.execute("INSERT INTO COVIDVAC VALUES(?,?,?,?)",(data["id"],str(datetime.now())[:10],data["vacman"],num+1,))
    conn.commit()
    conn.close()
    return "all good iyH" ,200  


if __name__ == "__main__":
    app.run(debug=True)        


