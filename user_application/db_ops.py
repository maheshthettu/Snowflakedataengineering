from db_connection.db_connecter import get_connection

def create_user(username, email, phone,password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO FORMULA_RACE.MANAGE_SCHEMA.USERS (USERNAME, EMAIL, PHONE, PASSWORD) VALUES (%s,%s,%s,%s)",
                    (username, email, phone, password))
        conn.commit()
    finally:
        cur.close()
        conn.close()
