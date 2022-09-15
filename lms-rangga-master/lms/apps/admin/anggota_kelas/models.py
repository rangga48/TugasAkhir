from models.mainModel import mainModel, paramsGenerator
column = ["id_guru", "nama","jenis_kelamin","tanggal_lahir"]
class Model(mainModel):
    def getAnggotaKelas(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT a.id_anggota_kelas, a.nis, b.nama as nama_siswa, c.nama as nama_kelas, a.id_kelas from anggota_kelas as a inner join siswa as b on a.nis = b.nis inner join kelas as c on a.id_kelas = c.id_kelas  where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def getAllAnggotaKelas(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT a.id_anggota_kelas, a.nis, b.nama as nama_siswa, c.nama as nama_kelas, a.id_kelas from anggota_kelas as a inner join siswa as b on a.nis = b.nis inner join kelas as c on a.id_kelas = c.id_kelas where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def getSiswa(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT nis, nama FROM siswa where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
    def postAnggotaKelas(self, data):
        try:
            col, param, val = (
                list(data.keys()), 
                ["%s" for x in range(len(data.items()))],
                list(data.values())
            )
            self.cursor.execute("INSERT INTO anggota_kelas ("+",".join(col)+") VALUES("+",".join(param)+")", val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"insert"
            }
            return  self
        except Exception as e:
            print(e)
    

    def deleteAnggotaKelas(self, data):
        try:
            params, val = paramsGenerator(data)
            self.cursor.execute("DELETE FROM anggota_kelas where "+params, val)
            self.client.commit()
            return True
        except Exception as e:
            print(e)