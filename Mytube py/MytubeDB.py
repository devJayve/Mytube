import sqlite3

class DbInit:

    def __init__(self):
        self.connection = sqlite3.connect("Mytubedb.db")
        self.cursor = self.connection.cursor()

    def initUserTable(self):
        self.cursor.execute("CREATE TABLE user (id VARCHAR(20),password VARCHAR(20),phonenumber TINYINT(11),date DATE);")

    def initPlaylistTable(self):
        self.cursor.execute("CREATE TABLE playlist (id VARCHAR(20), listname CHAR(20));")

    def initVideoTable(self):
        self.cursor.execute("CREATE TABLE video (id VARCHAR(20),listname CHAR(20), url CHAR(100));")

    def dropAllTable(self):
        #self.cursor.execute("DROP TABLE user;")
        #self.cursor.execute("DROP TABLE playlist;")
        self.cursor.execute("DROP TABLE video;")

    def testId(self):
        connection = sqlite3.connect("Mytubedb.db") 
        cursor = connection.cursor()

        #cursor.execute("INSERT INTO user VALUES('123','123','01012345678','2020-10-10');")
        cursor.execute("DELETE FROM playlist WHERE id='123';")
        connection.commit()
        connection.close()

        
if __name__ == "__main__":
    db = DbInit()
    #db.initUserTable()
    #db.initPlaylistTable()
    #db.dropAllTable()
    #db.testId()
    db.initVideoTable()