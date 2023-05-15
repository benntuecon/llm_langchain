from dotenv import load_dotenv
from langchain.llms import OpenAI
from agent.callbacks import StreamLLMCallbackHandler
from agent.prompt_templates import final_prompt_test_jd_extraction
from db.vector_store import get_collection
from schema import JobDescriptionInput, RepoSummary
from chromadb.api.types import QueryResult


load_dotenv()


def test():

    llm = OpenAI(temperature=0.9, callbacks=[
        StreamLLMCallbackHandler()], max_tokens=1000, streaming=True, model_name="gpt-3.5-turbo",)


def match_repos_with_jd(jd: JobDescriptionInput) -> QueryResult:
    """ get the most relevant repos from the vector store
    return the un-summarized repos
    Args:
        jd (JobDescriptionInput): 
        the processed summary of the job description from user
        should be match the format of the schema define in the schema.py

    Returns:
        QueryResult: the direct result from the chromaDb vector store, should be a list of the document in the database

    """
    ...
