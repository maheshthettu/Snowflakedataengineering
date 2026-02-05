import snowflake.connector
snowflake.connector.paramstyle = "qmark"

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from snowflake_connection.snowflake_con import get_connection
from snowflake_connection.validators import is_valid_email, email_exists

st.title("📥 Load Data into Snowflake")

name = st.text_input("Name")
email = st.text_input("Email")
age = st.number_input("Age", min_value=1, max_value=100, step=1)

if st.button("Load into Snowflake"):

    if not name or not email:
        st.warning("⚠️ Please fill all fields")

    elif not is_valid_email(email):
        st.error("❌ Invalid email format")

    else:
        try:
            conn = get_connection()

            if email_exists(conn, email):
                st.error("⚠️ Email already exists in database")
            else:
                cur = conn.cursor()
                cur.execute(
                    """
                    INSERT INTO COLLEGE.BRANCH.USERS (NAME, EMAIL, AGE)
                    VALUES (?, ?, ?)
                    """,
                    (name, email, int(age))
                )
                conn.commit()
                st.success("✅ Data loaded successfully into Snowflake")

        except Exception as e:
            st.error(f"❌ Error loading data: {e}")

        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()
