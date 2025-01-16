import streamlit as st


rho_api_key = st.secrets.get("rho_api_key")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("rho_api_key: {}".format(rho_api_key))
st.write("asdasd")

