import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))


def email_exists(conn, email: str) -> bool:
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT 1 FROM COLLEGE.BRANCH.USERS WHERE EMAIL = ?",
            (email,)
        )
        return cur.fetchone() is not None
    finally:
        cur.close()
