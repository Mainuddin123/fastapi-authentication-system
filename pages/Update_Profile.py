import streamlit as st
import requests

st.set_page_config(
    page_title="Update Profile",
    page_icon="✏️",
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

# ----------------------------------------------------- #

# Check Login

if "logged_in" not in st.session_state or not st.session_state.logged_in:

    st.error("❌ Please Login First")
    st.stop()

# ----------------------------------------------------- #

st.title("✏️ Update Profile")

st.markdown("---")

st.info(f"Logged in as **{st.session_state.username}**")

# ---------------- Form ---------------- #

with st.form("update_form"):

    username = st.text_input(
        "New Username",
        value=st.session_state.username
    )

    email = st.text_input(
        "New Email"
    )

    password = st.text_input(
        "New Password",
        type="password"
    )

    update = st.form_submit_button(
        "Update Profile",
        use_container_width=True
    )

# ---------------- Update ---------------- #

if update:

    if username == "" or email == "" or password == "":

        st.warning("Please fill all fields.")

    else:

        data = {
            "username": username,
            "email": email,
            "password": password
        }

        response = requests.put(
            f"{API_URL}/update/{st.session_state.user_id}",
            json=data
        )

        if response.status_code == 200:

            st.success("✅ Profile Updated Successfully")

            # Update session with new username
            st.session_state.username = username

            st.balloons()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error("Unable to update profile.")

st.markdown("---")

# ---------------- Navigation ---------------- #

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🏠 Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/Dashboard.py")

with col2:

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):
        st.switch_page("pages/Logout.py")

st.markdown("---")

st.caption(
    "Authentication System | FastAPI • SQLAlchemy • PostgreSQL • Streamlit"
)