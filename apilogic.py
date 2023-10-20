import requests
import pandas  as pd
import csv
import showgraph


#       INTERNAL FUNCTIONS

def fetchDataFromAPI(topUrl):
    url=f"https://codeforces.com/api/{topUrl}"
    response= requests.get(url)

    # with open("data.csv", 'w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     header = response[0].keys()
    #     csv_writer.writerow(header)
    #     for entry in response:
    #         csv_writer.writerow(entry.values())

    data=response.json()   # .json() will convert the the json file to python dictionary
    return data





#       USER FUNCTIONS



def getHandleInfo(handles):
    data=fetchDataFromAPI(f"user.info?handles={handles}")

    f = open('data.csv','w')
    csv_file = csv.writer(f)
    csv_file.writerow(('handle', 'rating', 'rank', 'organization', 'country', 'maxRating', 'maxRank',))

    for item in data['result']:
        csv_file.writerow((item['handle'], item['rating'], item['rank'], item['organization'], item['country'], item['maxRating'], item['maxRank'],))

    f.close()

    # df=pd.read_csv("data.csv")   # dont need this any more as the main module will read the file itself
    # return df #return statement nahi dia hai 

def getRatingChangeInfo(handles):
    handleslist=handles.split(";")

    f = open('rc_data.csv','w')
    csv_file = csv.writer(f)
    csv_file.writerow(('handle','Time', 'newRating'))



    for handle in handleslist:
        data=fetchDataFromAPI(f'user.rating?handle={handle}')
        for item in data['result']:
            csv_file.writerow((item['handle'],item['ratingUpdateTimeSeconds'], item['newRating']))
    
    f.close()

    




##################################################################################################################################################################
#######    the following function are a designed to do some pre task to be performed before the plotting of the graphs
##################################################################################################################################################################


def graphUsers(handles):
    #do some data fetching for the graph module
    getHandleInfo(handles)
    # call the function to generate the graph
    showgraph.graphUsers()

def graphUsersRatingChange(handles):
    #do some data fetching for the graph module
    getRatingChangeInfo(handles)
    # call the function to generate the graph
    showgraph.plotRatingChangeForUsers(handles)   