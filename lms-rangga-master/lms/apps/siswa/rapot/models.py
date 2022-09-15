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

    def getAllNilai(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT c.id_nilai_ujian_semester,a.id_guru, (select sum(if((select nilai from tugas_pengerjaan where nis = b.nis and id_tugas=a.id_tugas) is null,0,(select nilai from tugas_pengerjaan where nis = b.nis and id_tugas=a.id_tugas)))/count(*) from tugas as a ) as nilai_harian_tugas,(select nama from mata_pelajaran where id_mata_pelajaran = a.id_mata_pelajaran) nama_mata_pelajaran,c.id_jadwal, b.nis as nis, (select nama from siswa where nis=b.nis) as nama_siswa, c.nilai_uts, c.nilai_uas, CAST(c.nilai_keterampilan * (select (count(*)-(select count(*) from absensi where nis = c.nis))/count(*) from agenda where id_jadwal = c.id_jadwal) as INTEGER) as nilai_keterampilan, c.nilai_harian from jadwal a inner join anggota_kelas b on a.id_kelas = b.id_kelas left join nilai_ujian_semester c on a.id_jadwal = c.id_jadwal and b.nis = c.nis where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
    def getNilai(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT c.id_nilai_ujian_semester,a.id_guru, (select sum(if((select nilai from tugas_pengerjaan where nis = b.nis and id_tugas=a.id_tugas) is null,0,(select nilai from tugas_pengerjaan where nis = b.nis and id_tugas=a.id_tugas)))/count(*) from tugas as a ) as nilai_harian_tugas,(select nama from mata_pelajaran where id_mata_pelajaran = a.id_mata_pelajaran) nama_mata_pelajaran,c.id_jadwal, b.nis as nis, (select nama from siswa where nis=b.nis) as nama_siswa, c.nilai_uts, c.nilai_uas, CAST(c.nilai_keterampilan * (select (count(*)-(select count(*) from absensi where nis = c.nis))/count(*) from agenda where id_jadwal = c.id_jadwal) as INTEGER) as nilai_keterampilan, c.nilai_harian from jadwal a inner join anggota_kelas b on a.id_kelas = b.id_kelas left join nilai_ujian_semester c on a.id_jadwal = c.id_jadwal and b.nis = c.nis where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    def getAllTugas(self, nis, id_jadwal):
        try:
            
            self.cursor.execute("SELECT a.id_tugas, a.id_agenda, a.attachment, a.title, a.konten, (select nilai from tugas_pengerjaan where nis = '"+nis+"' and id_tugas=a.id_tugas) from tugas as a where a.id_agenda in ((select id_agenda from agenda where id_jadwal = '"+id_jadwal+"'))")
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
            self.cursor.execute("select a.nis, a.id_kelas, c.nama as nama_kelas from anggota_kelas as a inner join kelas c on a.id_kelas = c.id_kelas where "+params, values)
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
            self.cursor.execute("SELECT id_tugas_pengerjaan, id_tugas, nis, konten, attachment, is_approved from tugas_pengerjaan where "+params, values)
            res = self.cursor.fetchall()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
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
    
    def postTugasPengerjaan(self, data):
        try:
            col, param, val = (
                list(data.keys()), 
                ["%s" for x in range(len(data.items()))],
                list(data.values())
            )
            self.cursor.execute("INSERT INTO tugas_pengerjaan ("+",".join(col)+") VALUES("+",".join(param)+")", val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"insert"
            }
            return  self
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