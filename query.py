from datetime import datetime

import sqlite3

# conn = sqlite3.connect('Employees.db')

# INSERT INTO EMPLOYEE VALUES("332288342","Yoni","Henner","JLM","Hatzerot","1","12.05.02","0527695444","0524000035")"""

def get(request_num , id):
    request_query=["FIRST_NAME || ' ' ||LAST_NAME" , "ADDR_ST || ' ' || ADDR_ST_NUM || ' , ' || ADDR_CITY","DOB","PHONE || ' , ' ||CELL_PHONE"]#continue
    conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
    c = conn.cursor()
    try:
        c.execute("select "+request_query[request_num]+" from EMPLOYEE WHERE ID= ?",(id,) ) #do try catch in case...
        rows=c.fetchall()
        if rows==[]:
            print("404")
        else: print(rows,"200")
    except Exception as e:
        print("500")
    c.close()
    conn.close()


def getCovidVacs(id):
    conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
    c = conn.cursor()
    try:
        c.execute("select VAC_NUM , DATE_VAC, VAC_MAN from COVIDVAC WHERE employee_ID= ?  ORDER BY VAC_NUM ASC",(id,) ) #do try catch ,add in order(order by) of vac num
        rows=c.fetchall()
        if rows==[]:
            print("404")
        else: print(rows,"200")
    except Exception as e:
        print("500")
    c.close()
    conn.close()
        
    return (rows)

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
    
def getAll(code):
    if code=='0000':
        conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
        c = conn.cursor()
        try:
            c.execute("""select DOB,  FIRST_NAME || ' ' ||LAST_NAME , ADDR_ST || ' ' || ADDR_ST_NUM || ' , ' || ADDR_CITY , DOB , PHONE || ' , ' || CELL_PHONE ,DATE_POSITIVE ,DATE_RECOVERY,DATE_VAC,VAC_MAN,VAC_NUM 
                        from EMPLOYEE 
                        INNER JOIN COVIDVAC on  COVIDVAC.EMPLOYEE_ID= EMPLOYEE.ID 
                        ORDER BY LAST_NAME ASC,VAC_NUM ASC """) 
            rows=c.fetchall()
            if rows==[]:
                print("404")
            else: print(rows,"200")
        except Exception as e:
            print("500")
        c.close()
        conn.close()
    else:  print("400","incorrect code")   



#tester
get(0,"332288372") #success
get(1,"332288323") #success
get(2,"332288372") #success
get(3,"332288331") #success

getCovidVacs("332288372")
getAll("2")
getAll("0000")


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

#post new worker


# app.route('/data',methods=['POST'])
# def postNew():
#     data=request.json
#     conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO EMPLOYEES VALUES(?,?,?,?,?)",(data["id"],data["firstname"],data["lastname"],data["city"],data["street"],data["streetnum"],data["DOB"],data["phone"],data["cellsphone"]))
#     rows=c.fetchall()
#     c.close()
#     conn.close()
#     return "data added to database"

#post new shot
# app.route('/data',methods=['POST'])
# def postShot():
#     data=request.json
#     conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
#     c = conn.cursor()
#     c.execute("select MAX(VAC_NUM)  from COVIDVAC WHERE EMPLOYEE_ID = ?",(id,)) #do try catch ,add in order of vac num
#     num=c.fetchone()[0] #number of vac update it
#     c.execute("INSERT INTO COVID_VAC VALUES(?,?,?,?)",[data["id"],str(datetime.now())[:19],data["vacman"],num+1])
#     rows=c.fetchall()
#     c.close()
#     conn.close()
#     return "data added to database"

def chaya():
    conn = sqlite3.connect(r'C:\Users\This_user\Desktop\hadassim_project\question_2\server.db')
    c = conn.cursor()
    
   # c.execute("select MAX(VAC_NUM)  from COVIDVAC WHERE EMPLOYEE_ID = '332288372'") #do try catch ,add in order of vac num
    id="332288372"
    c.execute("select MAX(VAC_NUM)  from COVIDVAC WHERE EMPLOYEE_ID = ?",(id,)) #do try catch ,add in order of vac num
    num=c.fetchone()[0]
    
    #rows=c.fetchall() #number of vac update it
    print(num)
    #print(rows)
    #c.execute("INSERT INTO COVID_VAC VALUES(?,?,?,?)",[data["id"],str(datetime.now())[:19],data["vacman"],data["vacnum"]])
    rows=c.fetchall()
    c.close()
    conn.close()

chaya()
