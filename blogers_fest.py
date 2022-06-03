

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
        

checked_users = len(db.get_users_data())


for index, row in work_data_frame[checked_users:].iterrows():
    
    email = row['email']
    user = row['user_name']
    vote = row['vote']
    
    print("\nCHECKING ... Mail", email, "User", user, "Index:", index)
        
    validation_result = verifer.verify_email(email)  
    
    log_data = {
        "index": index, 
        "smtp_check": validation_result["smtp"] if validation_result else None, 
        "vote": vote, 
        "email": email, 
        "user": user, 
        "data": validation_result
    }
    
    
    print("--- LOGGING DATA")
    print(log_data)
    
    db.add_user(log_data)
    
    
    
    
    








