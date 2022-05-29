from emailverifier import Client
from emailverifier import exceptions

client = Client('at_2yv4pTGtZLA0Jpqk05evdnKi02T9d')

test_mail = "wildproductionvideos@gmail.com"

def verify_email(mail):
        try:
            
            data = client.get(mail)
            
            print("----- FULL DATA")
            print(str(data))

            return {
                "email_adress": data.email_address,
                "format": data.format_check,
                "dns": data.dns_check,
                "smtp": data.smtp_check,
                "catch all": data.catch_all_check,
                "disposable": data.disposable_check,
                "free: ": data.free_check,
                # "last_audit_date": data.audit.audit_updated_date     
            }
            
        except exceptions.HttpException:
            # If you get here, it means service returned HTTP error code
            pass
        except exceptions.GeneralException:
            # If you get here, it means you cannot connect to the service
            pass
        except exceptions.UndefinedVariableException:
            # If you get here, it means you forgot to specify the API key
            pass
        except exceptions.InvalidArgumentException:
            # If you get here, it means you specified invalid argument
            # (options should be a dictionary)
            pass
        except:
            pass
            # Something else happened related. Maybe you hit CTRL-C
            # while the program was running, the kernel is killing your process, or
            # something else all together.
        
        
        
if __name__ == "__main__":
    
    # "anymailkjasdhfkshfjkashf@gmail.com"

    # validation_result = verify_email("anymailkjasdhfkshfjkashf@gmail.com")

    # print("-- VALIDATION RES")
    # print(validation_result)

    # if validation_result["dns"]:
    #     print("----- DNS VALID")
    
    f = open("votes_validation.json", "r")
    # print(f.read())
    
    # f_read = f.read()
    
    print(f)
    
    print("Index--------> ", f["index"])