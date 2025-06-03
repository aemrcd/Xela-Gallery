import hashlib
import hmac
import os
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("SECRET_SALT")  

def hash_email(email: str) -> str:
    
    return hmac.new(secret, email.lower().strip().encode(), hashlib.sha256).hexdigest()  #  .lower.strip to prevent issue 
    # with Large letters and spaces in email address