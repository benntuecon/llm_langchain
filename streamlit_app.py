import streamlit as st
from agent.callbacks import StreamLLMCallbackHandler
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from agent.prompt_templates import final_prompt_test_jd_extraction, jd_extract_template
from config import logger
import dotenv
import json

from langchain.schema import (
    HumanMessage,
    SystemMessage
)

dotenv.load_dotenv()


class StTextManager:
    '''
    singleton class to manage text in streamlit
    '''

    def __init__(self, st=st):
        self.text = ""
        self.st = st

    def insert(self, text: str):
        self.text += text
        self.st.write(self.text, unsafe_allow_html=True,)

    def get_text(self):
        print(self.text)
        return self.text

    def clear(self):
        self.text = ""


# set up singleton text manager
st.session_state['text_manager'] = st.session_state.get(
    'text_manager') or StTextManager()
# text_manager = st.session_state['text_manager']


def streamlit_app():

    # llm = ChatOpenAI(temperature=0.9, callbacks=[
    #     stream_handler], max_tokens=400, model_name="gpt-3.5-turbo",)

    with st.sidebar:
        st.markdown("""
        # About 
        This app is designed for **`Recruiters`** to see how Ben fit the job description, with the help of `Generative AI`.
        
        """)
        st.markdown("""
        # How does it work
        The underlying works flow is as follows:
          1. Used prompt engineering + map-reduce embedding strategy to summarized the JD.
          2. Used summarized JD to fetch the most relevant parts of resume and github repos.
          3. System prompting on the summarized resume and github repos to llm, send it into a langchain agent.
          4. Ready to receive questions from recruiters, see how Ben fit the job 🤓.
        > Though some tool we use are overkill, the main idea is to explore how generative ai can provide value the conceptual matching process like candidate sourcing.

        """)
        st.markdown("""
        # Tech stack
          * Vector Database for llm : vector store`ChromaDB`
          * Manager of llm : `langchain agent` `langchain summarizer` 
          * Models : `gpt-3.5-turbo` `all-mpnet-base-v2`
          * Frontend : `Streamlit`

        """)

    st.markdown("""
    # CandidateGPT by Ben Chen
    """)
    job_description = st.text_input(
        "Put job description below", disabled=False, placeholder="""Software Engineer II, llm ... What we are looking for ... Good to have ...""", help="put job description here, and ")

    placeholder = st.empty()

    st.button(label="test label", on_click=on_click_generate,
              args=[placeholder, job_description, st])

    if 'json' in st.session_state:
        st.write("json summery for the input")
        st.write(st.session_state['json'])
    # st.write(st.session_state['text_manager'].text, unsafe_allow_html=True,)


def generate_data(text_manager):
    # This is just an exa}\n')
    text_manager.insert(" test")


def on_click_generate(placeholder, prompt, st):
    if len(prompt) < 50:
        st.warning("Please put more text, at least 50 characters")
        return

    prompt = jd_extract_template.format(text=prompt)
    msg = [
        SystemMessage(
            content="you are the best job description extractor, receiving JD and returning perfect pure json output for the job description"),
        HumanMessage(content=prompt),
    ]
    with placeholder:
        st.session_state['text_manager'] = StTextManager(st)
        text_manager = st.session_state['text_manager']
        stream_handler = StreamLLMCallbackHandler(text_manager)
        extractor_llm = ChatOpenAI(temperature=0, callbacks=[
            stream_handler], max_tokens=400, streaming=True, model_name="gpt-3.5-turbo",)
        extractor_llm(msg)
        st.session_state['json'] = text_manager.get_text()
    try:
        if 'json' in st.session_state:
            json_output = json.dumps(st.session_state.json)
            st.write(json_output,)
    except Exception as e:
        logger.WARN(f"error in json.dumps: {e}")
        # json_output = json.dumps(text_manager.get_text())


if __name__ == "__main__":
    streamlit_app()
