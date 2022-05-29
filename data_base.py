import pymongo


client = pymongo.MongoClient("localhost", 27017)

db = client['python']

log_data = {"index": int, "smtp_check": bool, "vote": str, "data": {}}

blogers_data = db.blogers_data

def add_user(user_data: dict):
    try:

        res = blogers_data.insert_one(user_data)

        print('-------> checked, added')
        return res
    
    except ValueError as e:
        print(e)
        
        
def get_users_data():
    try:
        all_users  = list(blogers_data.find())

        return all_users
    
    except ValueError as e:
        print(e)
        
        
        
if __name__ == "__main__":
    
    
    users_data = get_users_data()

    print("----- Got", len(users_data), "accounts")
    
    unvalid_emails = list(filter(lambda x: ( not x['smtp_check'] ), users_data))
        
    print("----- UNVALID EMAILS:", len(unvalid_emails), "percents:", str((len(unvalid_emails)/len(users_data)) * 100 ) +"%" )
    
    # print("----- Unvalid %: ", ( (len(unvalid_emails)/len(users_data)) * 100 ))