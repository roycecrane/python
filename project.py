
from sqlite3 import DatabaseError
import connection as cn             # connect to sql server
import dataIndex as dat             # my data classes   
import interface as inter           # convert sql to pandas data 
import gl_program as gls
import pandas as pd
import os  

def main():
    # init connection to server with connection class with connection str for oracle 
    CONN = cn.Connection('system/bac0N123@192.168.0.34:1521/xe')
    INERF = inter.Interface(CONN.runQuery) 
    DATA = dat.dataIndex(INERF)
    
    # county_names = DATA.data['COUNTY'].unique()
    # max = 0
    # hood_names  = DATA.data['NEIGHBOURHOOD'].unique() 
    # for ind in DATA.data.index:
    #     col = 0.0
    #     for hood in hood_names:
        
    #         col += 5.0
    #         if DATA.data['NEIGHBOURHOOD'][ind] == hood:
    #             DATA.data.at[ind,'REVIEWS'] = col
    #             if col > max: max = col
    # print(max)
                

    # DATA.data.to_csv(index=False)
    # DATA.data.to_csv('out.csv') 

    # countys = []
    # for c in county_names:
    #     county_data = DATA.data[DATA.data['COUNTY'] == c]
    #     countys.append(dat.countyData(c,county_data))
    # DATA.data.concat(DATA.data,df)
    glDat = DATA.data[['LATITUDE', 'LONGITUDE','REVIEWS']].to_numpy()
    # print(em)
    gls.start(glDat,0)
if __name__ == "__main__":
    main()



