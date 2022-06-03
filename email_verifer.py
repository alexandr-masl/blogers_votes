from emailverifier import Client
from emailverifier import exceptions

client = Client('API_KEY')

test_mail = "wildproductionvideos@gmail.com"

def verify_email(mail):
        try:
            
            data = client.get(mail)
            
            print("----- FULL DATA")
            print(str(data))
            
            return {
                
                "email_adress": data.email_address if data.email_address else None,
                "format": data.format_check if data.format_check else None,
                "dns": data.dns_check if data.dns_check else None,
                "smtp": data.smtp_check if data.smtp_check else None,
                "catch all": data.catch_all_check if data.catch_all_check else None,
                "disposable": data.disposable_check if data.disposable_check else None,
                "free: ": data.free_check if data.free_check else None,
                "last_audit_date": data.audit.audit_updated_date if data.audit.audit_updated_date else None
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
        
        