from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

from langchain.prompts import PromptTemplate
from langchain.document_loaders import YoutubeLoader
from langchain.chains import LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.chains.summarize import load_summary_chain

from argparse import ArgumentParser
from dotenv import load_dotenv
import os


load_dotenv()

# llm = OpenAI(temperature=0.9, callbacks=[
#              StreamingStdOutCallbackHandler()], max_tokens=100, streaming=True,)

intro_tech_prompt_template = PromptTemplate(
    input_variables=["tech"],
    template=(
        "請用小紅書的誇張語氣，把接下來的文字，改寫成更長的小作文，幾項注意事項，爭取同理心，爭取他人認同，用詞不宜。文字開始： {tech} "),
)

# chain = LLMChain(llm=llm, prompt=intro_tech_prompt_template)

# yt_loader = YoutubeLoader.from_youtube_url(
# 'https://www.youtube.com/watch?v=oF2hYNS9NqA&ab_channel=AaronKengAvar')


def main():
    chat = ChatOpenAI(streaming=True, callbacks=[
                      StreamingStdOutCallbackHandler()], temperature=0)
    resp = chat(
        [HumanMessage(content="Write me a song about sparkling water.")])
    # parser = ArgumentParser()
    # parser.add_argument(
    #     "-t", "--tech", dest="tech", help="The technology to introduce", required=True)
    # args = parser.parse_args()

    # print(llm(intro_tech_prompt_template.format(tech=args.tech)))


if __name__ == "__main__":
    main()
