from models.mainModel import mainModel, paramsGenerator
column = ["id_guru", "nama","jenis_kelamin","tanggal_lahir"]
class Model(mainModel):
    def getUser(self, data={}):
        try:
            params, values = paramsGenerator(data)
            self.cursor.execute("SELECT id_user, username, password, role, user_role_id FROM user where "+params, values)
            res = self.cursor.fetchone()
            self.result = {
                "data":res,
                "action":"select"
            }
            return self
        except Exception as e:
            print(e)

    