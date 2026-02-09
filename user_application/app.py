import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
from user_application.user_validators import is_valid_email,validate_user
from db_connection.db_connecter import get_connection
from db_ops import create_user



st.set_page_config(layout="wide")

left, center, right = st.columns([1, 2, 1])
with center:
    st.title("🏎️ Formula 1 Race Portal")


if "page" not in st.session_state:
    st.session_state.page = "main"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ==============================
# MAIN PAGE
# ==============================
def main_page():
    st.markdown("<h1 style='text-align:center;'>🔐 User Login</h1>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Login", use_container_width=True):
                st.session_state.page = "login"
                st.rerun()

        with col2:
            if st.button("Register", use_container_width=True):
                st.session_state.page = "register"
                st.rerun()


# ==============================
# REGISTER PAGE
# ==============================
def register_page():
    st.title("📝 Register")

    username = st.text_input("Username")
    email = st.text_input("Gmail")
    phone = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")

    if st.button("Submit"):

        if not username or not email or not phone or not password:
            st.warning("⚠️ Please fill all fields")

        elif not is_valid_email(email):
            st.error("❌ Invalid email format")

        else:
            try:
                conn = get_connection()
                validater = validate_user(conn, username, email, phone)
                if validater :
                    st.error(validater)
                else:
                    create_user(username, email, phone, password)
                    st.success("✅ Registered Successfully!")

                    st.session_state.page = "main"
                    conn.close()
                    # st.rerun()

            except Exception as e:
                st.error(f"❌ Error loading data: {e}")

    if st.button("⬅ Back to Login"):
        st.session_state.page = "main"
        st.rerun()


# ==============================
# LOGIN PAGE
# ==============================
def login_page():
    st.title("🔑 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login Now"):
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute(
                "SELECT COUNT(*) FROM FORMULA_RACE.MANAGE_SCHEMA.USERS WHERE USERNAME=%s AND PASSWORD=%s",
                (username, password),
            )

            result = cur.fetchone()[0]

            cur.close()
            conn.close()

            if result > 0:
                st.success("✅ Login Successful")
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.error("❌ Invalid credentials")

        except Exception as e:
            st.error(str(e))

    if st.button("⬅ Back"):
        st.session_state.page = "main"
        st.rerun()


# ==============================
# DASHBOARD PAGE
# ==============================
def dashboard_page():
    st.title("📊 Users Data")

    # protect route
    if not st.session_state.logged_in:
        st.warning("Please login first")
        st.session_state.page = "login"
        st.rerun()

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT USERNAME, EMAIL, PHONE FROM FORMULA_RACE.MANAGE_SCHEMA.USERS")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        st.table(rows)

    except Exception as e:
        st.error(str(e))

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "main"
        st.rerun()


# ==============================
# ROUTER
# ==============================
if st.session_state.page == "main":
    main_page()

elif st.session_state.page == "register":
    register_page()

elif st.session_state.page == "login":
    login_page()

elif st.session_state.page == "dashboard":
    dashboard_page()
