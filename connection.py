import cx_Oracle
class Connection:
    def __init__(self,conn_string):
        try:
            self.conn_string = conn_string
            self.__conn = cx_Oracle.connect(conn_string)
            print(self.__conn.version)
            self.__curr = self.__conn.cursor()
        except:
            print("CONNECTION ERROR!")

    def runQuery(self, sql_query):
        self.__curr.execute(sql_query)
        result =  self.__curr.fetchall()
        col_names = [result[0] for result in self.__curr.description]
        return result, col_names

