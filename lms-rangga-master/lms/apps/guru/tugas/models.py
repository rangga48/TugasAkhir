from models.mainModel import mainModel, paramsGenerator
column = ["id_guru", "nama","jenis_kelamin","tanggal_lahir"]
class Model(mainModel):
    def getTugas(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_tugas, id_agenda, attachment, title, konten from tugas where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def getAllTugas(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_tugas, id_agenda, attachment, title, konten, created_date from tugas where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
   
    def getAllTugasPengerjaan(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_tugas_pengerjaan, id_tugas, nis, konten,created_date, last_update, attachment, (select nama from siswa where nis=tugas_pengerjaan.nis) as nama_siswa, is_approved from tugas_pengerjaan where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def patchTugasPengerjaan(self, data, where):
        try:
            params_up, val_up = paramsGenerator(data)
            params_wh, val_wh = paramsGenerator(where)
            val = val_up + val_wh
            self.cursor.execute("UPDATE tugas_pengerjaan set "+params_up.replace("and",",")+" WHERE "+params_wh, val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"update"
            }
            return self.result
        except Exception as e:
            print(e)
            
    def postTugas(self, data):
        try:
            col, param, val = (
                list(data.keys()), 
                ["%s" for x in range(len(data.items()))],
                list(data.values())
            )
            self.cursor.execute("INSERT INTO tugas ("+",".join(col)+") VALUES("+",".join(param)+")", val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"insert"
            }
            return  self
        except Exception as e:
            print(e)
    
    def patchTugas(self, data, where):
        try:
            params_up, val_up = paramsGenerator(data)
            params_wh, val_wh = paramsGenerator(where)
            val = val_up + val_wh
            self.cursor.execute("UPDATE tugas set "+params_up.replace("and",",")+" WHERE "+params_wh, val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"update"
            }
            return self.result
        except Exception as e:
            print(e)

    def deleteTugas(self, data):
        try:
            params, val = paramsGenerator(data)
            self.cursor.execute("DELETE FROM tugas where "+params, val)
            self.client.commit()
            return True
        except Exception as e:
            print(e)