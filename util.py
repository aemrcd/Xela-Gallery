import hashlib
import secrets

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def tokenize_email(email):
    user_id = secrets.randbelow(1000000)
    domain = email.split('@')[-1]
    email_token = f"User_{user_id}@{domain}"
    return email_token
