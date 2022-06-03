import pandas as pd
from pandas import  DataFrame
import email_verifer as verifer
import data_base as db
import json

dfs = pd.read_excel("blog_fest_votes.xlsx", sheet_name=None)

votes_data = dfs["Final with bots-YOP-Poll-Export"]

framed_data = DataFrame.from_dict(votes_data)

print("----> FULL DATA ")
print(framed_data)
print("-----------")

work_data_frame = DataFrame()
work_data_frame['user_name'] = framed_data.iloc[:, 0]
work_data_frame['email'] =framed_data.iloc[:, 1]
work_data_frame['date'] =framed_data.iloc[:, 5]
work_data_frame['date'] =framed_data.iloc[:, 5]
work_data_frame['vote'] =framed_data.iloc[:, 7]
work_data_frame['ip'] =framed_data.iloc[:, 4]


work_data_frame.reset_index()

print("----> WORK DATA ")
print(work_data_frame)
print("-----------")

WAHBA = []
BETZMANN = []
MISTICO = []
FAMILUKIS = []

bloggers = ["CHRISTIAN BETZMANN", "AZUL MISTICO", "PROJECT WAHBA", "LOS FAMILUKIS", "TEAM MARVE", "MAN VS BABY", "BOB THISSEN", "DABBLE AND TRAVEL", "GIRL VS GLOBE", "BACKPACKER STEVE"]


for index, row in work_data_frame.iterrows():
    vote = row['vote']
    ip = row["ip"]
    
    if "PROJECT WAHBA" in vote:
        WAHBA.append({"vote": vote, "ip": str(ip)})
    elif "CHRISTIAN BETZMANN" in vote:
        BETZMANN.append({"vote": vote, "ip": str(ip)})
    elif "AZUL MISTICO" in vote:
        MISTICO.append({"vote": vote, "ip": str(ip)})
    elif "LOS FAMILUKIS" in vote:
        FAMILUKIS.append({vote: vote, ip: str(ip)})
    

betzman_clean_ip = []     

for item in BETZMANN:
    
    current_ip = item["ip"]
    got_this_ip = list(filter(lambda x: (x["ip"] == current_ip), BETZMANN))
    
    if len(got_this_ip) <= 10:
        betzman_clean_ip.append(item)
        
        
print("----- CHRISTIAN BETZMANN - total votes:", len(BETZMANN), "- unvalid IP", len(BETZMANN) - len(betzman_clean_ip), "- valid IP:", len(betzman_clean_ip))


mastico_clean_ip = []     

for item in MISTICO:
    
    current_ip = item["ip"]
    got_this_ip = list(filter(lambda x: (x["ip"] == current_ip), MISTICO))
    
    if len(got_this_ip) <= 10:
        mastico_clean_ip.append(item)
        
        
print("----- AZUL MISTICO  - total votes:", len(MISTICO), "- unvalid IP", len(MISTICO) - len(mastico_clean_ip), "- valid IP:", len(mastico_clean_ip))

wahba_clean_ip = []     

        
for item in WAHBA:
    
    current_ip = item["ip"]
    got_this_ip = list(filter(lambda x: (x["ip"] == current_ip), WAHBA))
    
    if len(got_this_ip) <= 10:
        wahba_clean_ip.append(item)
        
        
print("----- PROJECT WAHBA  - total votes:", len(WAHBA), "- unvalid IP", len(WAHBA) - len(wahba_clean_ip), "- valid IP:", len(wahba_clean_ip))

familikus_clean_ip = []     

for item in FAMILUKIS:
    
    current_ip = item["ip"]
    got_this_ip = list(filter(lambda x: (x["ip"] == current_ip), FAMILUKIS))
    
    if len(got_this_ip) <= 10:
        familikus_clean_ip.append(item)
        
        
print("----- PROJECT WAHBA  - total votes:", len(FAMILUKIS), "- unvalid IP", len(FAMILUKIS) - len(familikus_clean_ip), "- valid IP:", len(familikus_clean_ip))