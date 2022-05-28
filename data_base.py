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
    # print("----- USERS DATA -------")
    # print(users_data)