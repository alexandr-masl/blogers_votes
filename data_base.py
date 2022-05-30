import pymongo


client = pymongo.MongoClient("localhost", 27017)

db = client['python']

log_data = {"index": int, "smtp_check": bool, "vote": str, "email": str, "user": str, "data": {}}

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

    print("----- TOTAL VERIFED EMAILS:", len(users_data))
    
    unvalid_emails = list(filter(lambda x: ( not x['smtp_check'] ), users_data))
    
    valid_emails_amount = len(users_data) - len(unvalid_emails)
        
    print("----- UNVALID EMAILS:", len(unvalid_emails), "|", str((len(unvalid_emails)/len(users_data)) * 100 ) +"%", "\n\n")
    
    bloggers = ["CHRISTIAN BETZMANN", "AZUL MISTICO", "PROJECT WAHBA", "LOS FAMILUKIS", "TEAM MARVE", "MAN VS BABY", "BOB THISSEN", "DABBLE AND TRAVEL", "GIRL VS GLOBE", "BACKPACKER STEVE"]
    
    for name in bloggers:
        
        blogger = list(filter(lambda x: (name in x['vote']), users_data))
        blogger_unvalid_mails = list(filter(lambda x: ( not x['smtp_check'] ), blogger))
        blogger_valid_votes = len(blogger) - len(blogger_unvalid_mails)
        blogger_valid_result = (blogger_valid_votes / valid_emails_amount) * 100

        print(name, "--total votes:", len(blogger), "--unvalid votes:", len(blogger_unvalid_mails), "--valid votes:", blogger_valid_votes)
        print("--- VALID RESULT:", str(blogger_valid_result)+"%")
        print("\n")
        
        
    

    
    