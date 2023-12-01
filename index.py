import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = self.connect()

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_query(self, query, values=None):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()

class Application(Connection):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.conn = self.connect()
    
    def connect(self):
        return mysql.connector.connect(host = self.host, user = self.user, password = self.password, database = self.database)
    
    def execute_query(self, query, values=None):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()

    def create_record(self, nama, email, alamat):
        query = "INSERT INTO tb_mahasiswa (nama, email, alamat) VALUES (%s, %s, %s)"
        values = (nama, email, alamat)
        self.execute_query(query, values)

    def read_records(self):
        query = "SELECT * FROM tb_mahasiswa"
        cursor = self.conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        
        for i in results:
            print(i)

    def update_record(self, record_id, new_name):
        query = "UPDATE tb_mahasiswa SET nama = %s WHERE id = %s"
        values = (new_name, record_id)
        self.execute_query(query, values)

    def delete_record(self, record_id):
        query = "DELETE FROM tb_mahasiswa WHERE id = %s"
        values = (record_id,)
        self.execute_query(query, values)

    def close_connection(self):
        self.conn.close()


connection = Application("localhost", "root", "pw", "db_mahasiswa")
# connection.create_record("Yogawan", "yogawan@gmail.com", "klaten")
connection.read_records()