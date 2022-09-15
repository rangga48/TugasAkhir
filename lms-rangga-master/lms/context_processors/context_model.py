from models.mainModel import mainModel, paramsGenerator
column = ["id_guru", "nama","jenis_kelamin","tanggal_lahir"]
class Model(mainModel):
    def getSiswa(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT nis, nama FROM siswa where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    def getGuru(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_guru, nama FROM guru where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    def getAllTugas(self, nis):
        try:
            
            self.cursor.execute("SELECT id_tugas, id_agenda, attachment, title, konten, (select count(*) from tugas_pengerjaan where id_tugas=tugas.id_tugas and nis='"+str(nis)+"') as status_pengerjaan from tugas where (select count(*) from tugas_pengerjaan where id_tugas=tugas.id_tugas and nis='"+str(nis)+"') = 0")
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)