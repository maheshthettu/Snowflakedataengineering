import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
from user_application.user_validators import is_valid_email, email_exists
from db_ops import create_user
from db_connection.db_connecter import get_connection

st.title("📥 Load Data into Snowflake")

name = st.text_input("Name")
email = st.text_input("Email")
age = st.number_input("Age", min_value=1, max_value=100)

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
                create_user(name, email, int(age))
                st.success("✅ Data loaded successfully")

        except Exception as e:
            st.error(f"❌ Error loading data: {e}")

        finally:
            if 'conn' in locals():
                conn.close()
