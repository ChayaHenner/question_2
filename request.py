import struct
import sqlite3



class Request:
    def __init__(self,request):
        header=request[:18]
        self.emloyee_id, self.code,self.insertinfo = struct.unpack("16sH",header)
        request_query=["FIRST_NAME ,LAST_NAME","ADDR_CITY,ADDR_ST,ADDR_ST_NUM","DOB","PHONE","CELL_PHONE"]#continue

        if  self.code<=10: #retrieve address
            conn=sqlite3.connect('server.db')
            conn.text_factory=bytes
            cur=conn.cursor()
            cur.execute("select ? from EMPLOYEES WHERE ID= ?",[request_query[ self.code ], self.emloyee_id]) #do try catch in case...
            conn.commit()
            all=cur.fetchall()
            conn.close()

          