# OStwitterbot.py
# MICHAEL SCOTT
# 4 October 2021


# solve for multiple users

import tweepy
import requests
import time

from tweepy.api import API

# Authenticate to Twitter
auth = tweepy.OAuthHandler("blank for github")
auth.set_access_token("blank for github", 
    "blank for github")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

w_C = 'friend1'
w_M = 'friend2'
w_K = 'friend3'
w_D = 'friend4'
 
### START ###
url = "https://api.opensea.io/api/v1/collections"
querystring = {"asset_owner":"friend1 address","offset":"0","limit":"20"}
response = requests.request("GET", url, params=querystring)
collec_data = response.json()

#NFT OWNERS
recipient_idM = "twitter id1"
recipient_idC = "twitter id2"
recipient_idK = "twitter id3"
recipient_idD = "twitter id4"

i = 0
j = 0
nameList = []
floorList = []
resultsDict = dict()
resultsW = 'Update:'

while i < len(collec_data):
    nameList.append(collec_data[i]['name'])
    i += 1

while j < len(collec_data):
    floorList.append(collec_data[j]['stats']['floor_price'])
    j += 1

zip_iterator = zip(nameList, floorList)

dataDict = dict(zip_iterator)
print(dataDict)

#CREATE COPY
dataDict1 = dataDict

def return_key(val):
    for key, value in dataDict1.items():
        if value == val:
            return key
        continue


# LOOP 
print("running...")
time.sleep(5)
while True:
    try:
    # initiate values
        response = requests.request("GET", url, params=querystring)
        collec_data = response.json()
        i = 0
        j = 0
        nameList2 = []
        floorList2 = []
        dictCheck = dict()


        while i < len(collec_data):
            nameList2.append(collec_data[i]['name'])
            i += 1

        while j < len(collec_data):
            floorList2.append(collec_data[j]['stats']['floor_price'])
            j += 1
    
        zip_iterator = zip(nameList2, floorList2)
        dataDict = dict(zip_iterator)

        time.sleep(5)

    # retrieve new values
        j = 0

    # check for difference
        for key in dataDict:
            if (key in dataDict1 and dataDict[key] != dataDict1[key]):
                if (key in dataDict1 and dataDict[key] <= (dataDict1[key] - .1)):
                    resultsDict[key] = dataDict[key]
                    j += 1
                elif(key in dataDict1 and dataDict[key] >= (dataDict1[key] + .1)):
                    resultsDict[key] = dataDict[key]
                    dictCheck = dataDict1[key]
                    resultsW = resultsW + '\n' + return_key(dataDict1[key]) + ' ' + str(dataDict1[key]) + ' -> ' + str(dataDict[key])
                    j += 1
                else:
                    j += 1
                    continue
            else:
                j += 1
                #SENDING TO TWITTER DM
                if ((j == (len(dataDict) - 1)) & (dictCheck != {})):
                    api.send_direct_message(recipient_idM, text=resultsW)
                    continue
                continue
        else:
            p += 1
            if (p == 0):
                querystring = {"asset_owner":"Friend1 Address","offset":"0","limit":"20"}
            elif (p == 1):
                querystring = {"asset_owner":"My Address","offset":"0","limit":"20"}
            elif (p == 2):
                querystring = {"asset_owner":"Friend2 Address","offset":"0","limit":"20"}
            else:
                querystring = {"asset_owner":"Friend3 Address","offset":"0","limit":"20"}
                p = 0
            print("Floor hasn't notably changed")
            time.sleep(5)
            continue

    except Exception as e:
        print("error")
