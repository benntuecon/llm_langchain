from langchain.callbacks.base import BaseCallbackHandler


class StreamLLMCallbackHandler(BaseCallbackHandler):
    def __init__(self, ref_to_st_text_manager):
        self.text_manager = ref_to_st_text_manager

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text_manager.insert(token)
