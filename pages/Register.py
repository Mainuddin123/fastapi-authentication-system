import streamlit as st
import requests

st.set_page_config(
    page_title="Register",
    page_icon="📝",
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

# ---------------------------------------------------- #

left, center, right = st.columns([1,2,1])

with center:

    st.title("📝 Create Account")

    st.markdown("---")

    st.write("Please fill the details below")

    with st.form("register_form"):

        username = st.text_input(
            "Username",
            placeholder="Enter Username"
        )

        email = st.text_input(
            "Email",
            placeholder="Enter Email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter Password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Confirm Password"
        )

        register = st.form_submit_button(
            "Register",
            use_container_width=True
        )

    if register:

        if username == "" or email == "" or password == "":

            st.warning("All fields are required.")

        elif password != confirm_password:

            st.error("Passwords do not match.")

        else:

            data = {
                "username": username,
                "email": email,
                "password": password
            }

            response = requests.post(
                f"{API_URL}/register",
                json=data
            )

            if response.status_code == 200:

                st.success("🎉 Registration Successful!")

                st.balloons()

                st.info("Please login with your credentials.")

                if st.button(
                    "Go To Login",
                    use_container_width=True
                ):
                    st.switch_page("pages/Login.py")

            else:

                try:
                    st.error(response.json()["detail"])
                except:
                    st.error("Registration Failed.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏠 Home",
            use_container_width=True
        ):
            st.switch_page("app.py")

    with col2:

        if st.button(
            "🔑 Login",
            use_container_width=True
        ):
            st.switch_page("pages/Login.py")