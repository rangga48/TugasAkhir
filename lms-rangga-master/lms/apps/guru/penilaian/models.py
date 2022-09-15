from models.mainModel import mainModel, paramsGenerator
column = ["id_guru", "nama","jenis_kelamin","tanggal_lahir"]
class Model(mainModel):
    def getNilai(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT c.id_nilai_ujian_semester, c.id_jadwal, b.nis as nis, (select nama from siswa where nis=b.nis) as nama_siswa, c.nilai_uts, c.nilai_uas, CAST(c.nilai_keterampilan * (select (count(*)-(select count(*) from absensi where nis = c.nis))/count(*) from agenda where id_jadwal = c.id_jadwal) as INTEGER) as nilai_keterampilan, c.nilai_harian from jadwal a inner join anggota_kelas b on a.id_kelas = b.id_kelas left join nilai_ujian_semester c on a.id_jadwal = c.id_jadwal and b.nis = c.nis where "+params, values)
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
            self.cursor.execute("SELECT (select sum(if((select nilai from tugas_pengerjaan where nis = d.nis and id_tugas=tugas.id_tugas) is null,0,(select nilai from tugas_pengerjaan where nis = d.nis and id_tugas=tugas.id_tugas)))/count(*) from tugas where id_agenda in ((select id_agenda from agenda where id_jadwal = a.id_jadwal))) as nilai_harian_tugas,d.id_nilai_ujian_semester,a.id_mata_pelajaran,a.id_guru, a.id_jadwal, c.nis as nis, (select nama from siswa where nis=c.nis) as nama_siswa, d.nilai_uts, d.nilai_uas, CAST(d.nilai_keterampilan * (select (count(*)-(select count(*) from absensi where nis = d.nis))/count(*) from agenda where id_jadwal = d.id_jadwal) as INTEGER) as nilai_keterampilan, d.nilai_harian from jadwal a inner join kelas b on a.id_kelas = b.id_kelas inner join anggota_kelas c on b.id_kelas = c.id_kelas left join nilai_ujian_semester d on c.nis = d.nis and a.id_jadwal = d.id_jadwal where "+params, values)

            res = self.cursor.fetchall()
            
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)
    
    def getNilaiDetail(self, data={}):
        try:
            params, values = paramsGenerator(data)
            

            self.cursor.execute("SELECT c.id_nilai_ujian_semester,a.id_guru, (select sum(if((select nilai from tugas_pengerjaan where nis = b.nis and id_tugas=tugas.id_tugas) is null,0,(select nilai from tugas_pengerjaan where nis = b.nis and id_tugas=tugas.id_tugas)))/count(*) from tugas where id_agenda in ((select id_agenda from agenda where id_jadwal = c.id_jadwal)) ) as nilai_harian_tugas,(select nama from mata_pelajaran where id_mata_pelajaran = a.id_mata_pelajaran) nama_mata_pelajaran,c.id_jadwal, b.nis as nis, (select nama from siswa where nis=b.nis) as nama_siswa, c.nilai_uts, c.nilai_uas, CAST(c.nilai_keterampilan * (select (count(*)-(select count(*) from absensi where nis = c.nis))/count(*) from agenda where id_jadwal = c.id_jadwal) as INTEGER) as nilai_keterampilan, c.nilai_harian from jadwal a inner join anggota_kelas b on a.id_kelas = b.id_kelas left join nilai_ujian_semester c on a.id_jadwal = c.id_jadwal and b.nis = c.nis where "+params, values)

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
    def getNilaiRekap(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT b.id_jadwal,a.id_tugas,a.nis,avg(a.nilai) as nilai FROM `tugas_pengerjaan` a inner join tugas b on a.id_tugas = b.id_tugas where "+params+" group by id_jadwal, nis", values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    def patchNilaiUjianSemester(self, data, where):
        try:
            params_up, val_up = paramsGenerator(data)
            params_wh, val_wh = paramsGenerator(where)
            val = val_up + val_wh
            self.cursor.execute("UPDATE nilai_ujian_semester set "+params_up.replace("and",",")+" WHERE "+params_wh, val)
            self.client.commit()
            self.result = {
                "response":True,
                "action":"update"
            }
            return self.result
        except Exception as e:
            print(e)
            
    def postNilaiUjianSemester(self, data):
        try:
            col, param, val = (
                list(data.keys()), 
                ["%s" for x in range(len(data.items()))],
                list(data.values())
            )
            self.cursor.execute("INSERT INTO nilai_ujian_semester ("+",".join(col)+") VALUES("+",".join(param)+")", val)
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