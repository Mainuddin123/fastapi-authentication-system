import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide"
)

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

# User must login first
if "logged_in" not in st.session_state or not st.session_state.logged_in:

    st.error("❌ Please Login First")
    st.stop()

# ----------------------------------------------------- #

st.title("🏠 User Dashboard")

st.markdown("---")

st.success(f"Welcome, **{st.session_state.username}** 👋")

# ---------------- User Details ---------------- #

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        label="User ID",
        value=st.session_state.user_id
    )

with col2:

    st.metric(
        label="Username",
        value=st.session_state.username
    )

with col3:

    st.metric(
        label="Status",
        value="Active"
    )

st.markdown("---")

# ---------------- Profile Card ---------------- #

st.subheader("👤 Profile Information")

st.info(
f"""
**Username :** {st.session_state.username}

**User ID :** {st.session_state.user_id}

**Login Status :** Logged In ✅
"""
)

st.markdown("---")

# ---------------- Navigation ---------------- #

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "✏ Update Profile",
        use_container_width=True
    ):

        st.switch_page("pages/Update_Profile.py")

with col2:

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.switch_page("pages/Logout.py")

st.markdown("---")

# ---------------- Project Information ---------------- #

with st.expander("📘 Project Information"):

    st.write("""
This Authentication System demonstrates:

- FastAPI Backend
- PostgreSQL Database
- SQLAlchemy ORM
- Pydantic Validation
- Password Hashing
- Login Authentication
- Streamlit Frontend
""")

st.markdown("---")

st.caption(
    "Authentication System | FastAPI • SQLAlchemy • PostgreSQL • Streamlit"
)