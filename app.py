import streamlit as st

st.set_page_config(
    page_title="Authentication System",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- Hide Streamlit Default Menu ---------------- #

hide_style = """
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

</style>
"""

st.markdown(hide_style, unsafe_allow_html=True)

# ------------------------------------------------------------- #

col1, col2, col3 = st.columns([1,2,1])

with col2:

    # Optional Logo
    # st.image("assets/logo.png", width=150)

    st.title("🔐 Authentication System")

    st.markdown("---")

    st.subheader("Welcome")

    st.write(
        """
        This project demonstrates a complete Authentication System using

        ✅ FastAPI

        ✅ PostgreSQL

        ✅ SQLAlchemy

        ✅ Pydantic Validation

        ✅ Password Hashing

        ✅ Streamlit Frontend
        """
    )

    st.info(
        "Create a new account or login to continue."
    )

    st.markdown("### Choose an option")

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "📝 Register",
            use_container_width=True
        ):
            st.switch_page("pages/Register.py")

    with c2:

        if st.button(
            "🔑 Login",
            use_container_width=True
        ):
            st.switch_page("pages/Login.py")

    st.markdown("---")

    st.caption(
        "Developed using FastAPI • SQLAlchemy • PostgreSQL • Streamlit"
    )