from db_connection.db_connecter import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE()")
print(cur.fetchone())

cur.close()
conn.close()

