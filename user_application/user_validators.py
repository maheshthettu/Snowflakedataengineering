import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    """
    Phone must contain only digits.
    """
    return int(phone)


def email_validation(cur,email : str) :
    try:
        cur.execute(
            "SELECT 1 FROM FORMULA_RACE.MANAGE_SCHEMA.USERS WHERE EMAIL = %s",
            (email,)
        )
        if cur.fetchone() :
             return "❌ Email Already exist"
    except Exception as e:
                return(f"{e}")
        
def username_validation(cur, username: str) :
    try:
        cur.execute(
            "SELECT 1 FROM FORMULA_RACE.MANAGE_SCHEMA.USERS WHERE USERNAME = %s",
            (username,)
        )
        if cur.fetchone() :
             return "❌ Username Already exist"
    except Exception as e:
                return(f"{e}")


def phone_validation(cur, phone: str) :
    try:
        is_valid_phone(phone)
        cur.execute(
            "SELECT 1 FROM FORMULA_RACE.MANAGE_SCHEMA.USERS WHERE PHONE = %s",
            (phone,)
        )
        if cur.fetchone() :
             return "❌ Phone Already exist"
        
    except Exception as e:
                return(f"{e}")

def validate_user(conn, username: str, email: str, phone: str):
    """
    Performs:
    ✔ email format check
    ✔ phone numeric check
    ✔ duplicate email
    ✔ duplicate username
    ✔ duplicate phone

    Returns:
        error message (str) if failed
        None if success
    """

    # Format checks first (no DB hit)
    if not is_valid_email(email):
        return "❌ Invalid email format"
    
    cur = conn.cursor()
    if email_validation(cur,email):
         return email_validation(cur,email)
    if username_validation(cur,username):
        return username_validation(cur,username)
    if phone_validation(cur,username):
        return phone_validation(cur,phone)
    
    cur.close()



