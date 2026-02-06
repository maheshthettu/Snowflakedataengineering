from db_connection.db_connecter import get_connection

def create_user(name, email, age):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("USE WAREHOUSE COMPUTE_WH")
        cur.execute(
            """
            INSERT INTO COLLEGE.BRANCH.USERS (NAME, EMAIL, AGE)
            VALUES (%s, %s, %s)
            """,
            (name, email, age)
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()
