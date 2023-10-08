import pymysql

class SQL:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Root',
                             database='dbtest',
                             cursorclass=pymysql.cursors.DictCursor)
    
    def SaveToDb(self):
        with self.connection.cursor() as cursor:
            
            sql = "SELECT * from users;"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
if __name__ == '__main__':
    DB = SQL()
    DB.SaveToDb()

