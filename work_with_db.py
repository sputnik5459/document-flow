import pymysql
import datetime

class connection(object):
    def __init__(self):
        try:
            self.connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='1234',
                                         db='electronaladka',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        except:
            print("Connection failed!")
    def SelectCommand(self, text):
        self.text = text
        try:
            with self.connection.cursor() as self.cursor:
                # SQL
                self.sql = self.text
                print(self.sql)
                # Выполнить команду запроса (Execute Query).
                self.cursor.execute(self.sql)
                retrow = []
                for row in self.cursor:
                    retrow.append(row)
                return (retrow)
        except:
            print("Command Error!")
            
    def CloseConnection(self):
        self.connection.close()

    def InsertCommand(self, text):
        self.text = text
        try:
            with self.connection.cursor() as self.cursor:
                # SQL
                self.sql = self.text
                print(self.sql)
                # Выполнить команду запроса (Execute Query).
                self.cursor.execute(self.sql)
                self.connection.commit()
        except:
            print("Command Error!")
    def CloseConnection(self):
        self.connection.close()

class database(object):
    def __init__(self):
        self.db = connection()

    def db_log(self, log = None, pwd = None):
        return self.db.SelectCommand("SELECT login FROM employee WHERE (login = \""+log+"\" and password = \""+pwd+"\");")

    def close_connection(self):
        self.db.CloseConnection()

    def load_docs(self):
        return self.db.SelectCommand("SELECT * FROM document")

    def load_agreement(self):
        return self.db.SelectCommand("SELECT * FROM agreement")

    def delete_doc(self, id_doc):

        check = self.db.SelectCommand("SELECT doc_name FROM document WHERE id_doc = %s" % id_doc)

        if(check):

            now = datetime.datetime.now()

            if now.month < 10: 
                month = "0" + str(now.month)
            else:
                month = str(now.month)
            if now.day < 10: 
                day = "0" + str(now.day)
            else:
                day = str(now.day)

            self.db.InsertCommand("DELETE FROM document WHERE id_doc = %s" % id_doc)
            self.db.InsertCommand("DELETE FROM agreement WHERE document_id_doc = %s" % id_doc)
            with open("log.txt", "a") as f:
                f.write("Удален документ: '%s' (%s-%s-%s)\n" % (check[0]["doc_name"], str(now.year), month, day))
            return "Удаление прошло успешно"

        else:
            return "Документа с таким номером не существует"

    def create_doc(self, name = None, type_ = None, path_ = None, level_ = "0"):
        
        now = datetime.datetime.now()

        if now.month < 10: 
            month = "0" + str(now.month)
        else:
            month = str(now.month)

        if now.day < 10: 
            day = "0" + str(now.day)
        else:
            day = str(now.day)

        self.db.InsertCommand("INSERT INTO document VALUES(DEFAULT, %s, '%s', '%s', null, '%s-%s-%s', 0, '%s')" % (level_, name, type_, str(now.year), month, day, path_.replace("\\", "\\\\")))

        with open("log.txt", "a") as f:
                f.write("Создан документ: '%s' (%s-%s-%s)\n" % (name, str(now.year), month, day))

        return "Документ успешно создан"

    def commit_doc(self, id_doc):

        check = self.db.SelectCommand("SELECT * FROM agreement WHERE document_id_doc = %s" % id_doc)

        if(check):
            return "Данный документ уже подтвержден"
        else:
            now = datetime.datetime.now()

            if now.month < 10: 
                month = "0" + str(now.month)
            else:
                month = str(now.month)

            if now.day < 10: 
                day = "0" + str(now.day)
            else:
                day = str(now.day)

            kek = self.db.SelectCommand("SELECT max(agreement) FROM agreement")
            if kek[0]["max(agreement)"] == None:
                self.db.InsertCommand("INSERT INTO agreement VALUES (1,'%s-%s-%s', %s, 1)" % (str(now.year), month, day, id_doc))
            else:
                self.db.InsertCommand("INSERT INTO agreement VALUES (%s,'%s-%s-%s', %s, 1)" % (str(kek[0]["max(agreement)"] + 1), str(now.year), month, day, id_doc))

            self.db.InsertCommand("UPDATE document SET is_confirmed = 1, agreement_date = '%s-%s-%s' WHERE id_doc = %s" % (str(now.year), month, day, id_doc))
            
            with open("log.txt", "a") as f:
                f.write("Подтвержден документ с id: %s (%s-%s-%s)\n" % (id_doc, str(now.year), month, day))
            
            return ("Вы успешно подтвердили документ: %s" % id_doc)

db = database()