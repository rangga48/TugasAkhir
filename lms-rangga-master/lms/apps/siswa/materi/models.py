from models.mainModel import mainModel, paramsGenerator
column = ["id_guru", "nama","jenis_kelamin","tanggal_lahir"]
class Model(mainModel):
    def getMateri(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_materi, id_agenda, konten, attachment from materi where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def getAllMateri(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_materi, id_agenda, konten, attachment from materi where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def getAllMateriByJadwal(self, id_jadwal=""):
        try:
            self.cursor.execute("SELECT id_materi, id_agenda, konten, attachment from materi where id_agenda in ((select id_agenda from agenda where id_jadwal = '"+id_jadwal+"')) ")
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
   
    
    def postMateri(self, data):
        try:
            col, param, val = (
                list(data.keys()), 
                ["%s" for x in range(len(data.items()))],
                list(data.values())
            )
            self.cursor.execute("INSERT INTO materi ("+",".join(col)+") VALUES("+",".join(param)+")", val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"insert"
            }
            return  self
        except Exception as e:
            print(e)
    
    def patchMateri(self, data, where):
        try:
            params_up, val_up = paramsGenerator(data)
            params_wh, val_wh = paramsGenerator(where)
            val = val_up + val_wh
            self.cursor.execute("UPDATE materi set "+params_up.replace("and",",")+" WHERE "+params_wh, val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"update"
            }
            return self.result
        except Exception as e:
            print(e)

    def deleteMateri(self, data):
        try:
            params, val = paramsGenerator(data)
            self.cursor.execute("DELETE FROM materi where "+params, val)
            self.client.commit()
            return True
        except Exception as e:
            print(e)