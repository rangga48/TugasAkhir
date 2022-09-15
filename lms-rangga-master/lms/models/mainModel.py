from os import environ
import mysql.connector as mysqli

def paramsGenerator(data):
    print(data)
    if len(data.items())>0:
        if type(data) is dict:
            params = []
            values = []
            for key,val in data.items():
                params.append(key+" = %s")
                values.append(val)
            return " and ".join(params), values
    else:
        return "1", []

class mainModel:
    def __init__(self):
        self.client = mysqli.connect(
            host=environ.get("HOST","localhost"),
            user=environ.get("USERNAME","root"),
            password=environ.get("PASSWORD",""),
            database=environ.get("DATABASE","lms"),
        )
        self.cursor = self.client.cursor()
    
    def getResult(self):
        # print(self.result)
        self.client.commit()
        if self.result['action']=="select":
            column = self.cursor.description
            if type(self.result['data']) is tuple:
                row = self.result['data']
                data = {column[x][0]:row[x] for x in range(len(column))}
            if type(self.result['data']) is list:
                print(self.result['data'])
                data = [
                    {column[x][0]:row[x] for x in range(len(column))} for row in self.result['data']
                ]
            if self.result['data'] == None:
                data = None
            return data
        else:
            return False