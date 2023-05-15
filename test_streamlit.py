import streamlit as st
import time

with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
    st.write("✔️ 1 minute over!")
    time.sleep(1)
    st.write("✔️ 2 minute over!")
    time.sleep(1)
    st.write("✔️ 3 minute over!")
    time.sleep(1)
    st.write("✔️ 4 minute over!")
    time.sleep(1)
    st.write("✔️ 5 minute over!")
    time.sleep(1)
    st.write("✔️ 6 minute over!")
    time.sleep(1)
    st.write("✔️ 7 minute over!")
    time.sleep(1)
