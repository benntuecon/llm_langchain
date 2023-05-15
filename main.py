from db.set_up_db import setup_db
from streamlit_app import streamlit_app


def main():
    setup_db()
    streamlit_app()
