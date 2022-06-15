import pandas as pd

class dataIndex:
    total_entries = None
    data = None

    def __init__(self, inerf):
        self.data = inerf.getQueryResult('GET_LOC_DATA')
        self.total_entries = self.data.shape[0]
class entry:
    value = 0.0
    def __init__(self, id,lat,long,hood):
        self.id = id
        self.hood = hood 
        self.lat = lat
        self.long = long

    def setValue(self,value):
        self.value = value

        
# class countyData:
#     total_entries = None
#     county = None
#     data = None
#     def __init__(self, county, data):
#         self.county = county
#         self.data = data[(data['COUNTY'] == county)]
#         self.total_entries = self.data.shape[0]

# class neighborhoodData:
#     total_entries = None
#     county = None
#     neighborhood = None
#     data = None 
#     def __init__(self, county, data):
#         pass







    


