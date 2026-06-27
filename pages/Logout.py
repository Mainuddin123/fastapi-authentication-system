import streamlit as st
import time

st.set_page_config(
    page_title="Logout",
    page_icon="🚪",
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

st.title("🚪 Logout")

st.markdown("---")

if "logged_in" in st.session_state and st.session_state.logged_in:

    st.success(f"Goodbye, {st.session_state.username} 👋")

    st.info("Logging you out...")

    time.sleep(2)

    st.session_state.clear()

    st.success("✅ Logged Out Successfully")

    time.sleep(1)

    st.switch_page("app.py")

else:

    st.warning("You are already logged out.")

    if st.button("🏠 Go to Home", use_container_width=True):
        st.switch_page("app.py")