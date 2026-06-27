import streamlit as st
import requests

st.set_page_config(
    page_title="Login",
    page_icon="🔑",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# ---------------- Hide Streamlit Menu ---------------- #

hide_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

st.markdown(hide_style, unsafe_allow_html=True)

# Initialize Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------------------------------------------ #

left, center, right = st.columns([1,2,1])

with center:

    st.title("🔑 Login")

    st.markdown("---")

    st.write("Enter your credentials")

    with st.form("login_form"):

        username = st.text_input(
            "Username",
            placeholder="Enter Username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter Password"
        )

        login = st.form_submit_button(
            "Login",
            use_container_width=True
        )

    if login:

        if username == "" or password == "":

            st.warning("Please enter Username and Password.")

        else:

            data = {
                "username": username,
                "password": password
            }

            response = requests.post(
                f"{API_URL}/login",
                json=data
            )

            if response.status_code == 200:

                user = response.json()

                st.session_state.logged_in = True
                st.session_state.user_id = user["user_id"]
                st.session_state.username = user["username"]

                st.success("✅ Login Successful")

                st.balloons()

                st.switch_page("pages/Dashboard.py")

            else:

                try:
                    st.error(response.json()["detail"])
                except:
                    st.error("Invalid Username or Password")

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "🏠 Home",
            use_container_width=True
        ):
            st.switch_page("app.py")

    with c2:

        if st.button(
            "📝 Register",
            use_container_width=True
        ):
            st.switch_page("pages/Register.py")

st.markdown("---")

st.caption(
    "Authentication System | FastAPI • PostgreSQL • SQLAlchemy • Streamlit"
)