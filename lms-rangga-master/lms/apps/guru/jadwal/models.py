from models.mainModel import mainModel, paramsGenerator
column = ["id_guru", "nama","jenis_kelamin","tanggal_lahir"]
class Model(mainModel):
    def getJadwal(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("select b.nama as nama_guru, c.nama as nama_mata_pelajaran, d.nama as nama_kelas, a.id_jadwal, a.id_guru, a.id_kelas, a.id_mata_pelajaran, a.waktu, a.hari from jadwal as a inner join guru as b on a.id_guru = b.id_guru inner join mata_pelajaran as c on a.id_mata_pelajaran = c.id_mata_pelajaran inner join kelas as d on a.id_kelas = d.id_kelas where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def getAllJadwal(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("select b.nama as nama_guru, c.nama as nama_mata_pelajaran, d.nama as nama_kelas, a.id_jadwal, a.id_guru, a.id_kelas, a.id_mata_pelajaran, a.waktu, a.hari from jadwal as a inner join guru as b on a.id_guru = b.id_guru inner join mata_pelajaran as c on a.id_mata_pelajaran = c.id_mata_pelajaran inner join kelas as d on a.id_kelas = d.id_kelas where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
    def getAllAgenda(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("select * from agenda where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def getAllGuru(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_guru, nama, jenis_kelamin, tanggal_lahir FROM guru where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
    def getAllKelas(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_kelas, nama, wali_kelas FROM kelas where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
    def getAllMataPelajaran(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_mata_pelajaran, nama FROM mata_pelajaran where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
    def postJadwal(self, data):
        try:
            col, param, val = (
                list(data.keys()), 
                ["%s" for x in range(len(data.items()))],
                list(data.values())
            )
            self.cursor.execute("INSERT INTO jadwal ("+",".join(col)+") VALUES("+",".join(param)+")", val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"insert"
            }
            return  self
        except Exception as e:
            print(e)
    
    def postAgenda(self, data):
        try:
            col, param, val = (
                list(data.keys()), 
                ["%s" for x in range(len(data.items()))],
                list(data.values())
            )
            self.cursor.execute("INSERT INTO agenda ("+",".join(col)+") VALUES("+",".join(param)+")", val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"insert"
            }
            return  self
        except Exception as e:
            print(e)
    
    def patchJadwal(self, data, where):
        try:
            params_up, val_up = paramsGenerator(data)
            params_wh, val_wh = paramsGenerator(where)
            val = val_up + val_wh
            self.cursor.execute("UPDATE jadwal set "+params_up.replace("and",",")+" WHERE "+params_wh, val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"update"
            }
            return self.result
        except Exception as e:
            print(e)

    def deleteJadwal(self, data):
        try:
            params, val = paramsGenerator(data)
            self.cursor.execute("DELETE FROM jadwal where "+params, val)
            self.client.commit()
            return True
        except Exception as e:
            print(e)