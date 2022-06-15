import pandas as pd
class Interface:
    __TABLE = 'BNB_DATA'

    sql_code = {
    'GET_LOC_DATA': """ 
    SELECT ID AS ID, 
    COUNTY AS COUNTY, 
    NEIGHBOURHOOD AS NEIGHBOURHOOD, 
    LATITUDE AS LATITUDE, 
    LONGITUDE AS LONGITUDE,  
    PRICE AS PRICE, 
    RATING AS RATING,
    RATING_LOC AS RATING_LOC,
    REVIEWS AS REVIEWS

    FROM """ + __TABLE,

    'GET_COUNT': """ 
    SELECT COUNT(*) AS TOTAL  
    FROM """ + __TABLE
}

    def __init__(self,runQuery):
        self.__runQuery = runQuery

    def getQueryResult(self, query):
        current_query = self.sql_code[query]
        result = self.__runQuery(current_query)
        output = pd.DataFrame(result[0],columns = result[1])
        output.columns = result[1]
        return output
    def changeDataSet(self,newSet):
        self.__TABLE = newSet
        

        
        

    