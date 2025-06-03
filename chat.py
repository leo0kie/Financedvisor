import streamlit as st
import texts as tx
from enum import Enum
from openai import OpenAI

class HedgingPrompt(Enum):
    no_hedging = f"{tx.no_hedging}"
    first_person_hedging = f"{tx.first_person_hedging}"
    third_person_hedging = f"{tx.third_person_hedging}"

class Chat:
    def __init__(self, api_key, api_endpoint, model_name, chat_history = None, hedging_variant = None):
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.model_name = model_name
        self.chat_history = chat_history
        
        for hedging in HedgingPrompt:
            if hedging.name == hedging_variant:
                self.hedging_variant = hedging.value

    # Initiates the OpenAI API
    def buildClient(self):
        return OpenAI(api_key=self.api_key, base_url=self.api_endpoint)

    # Resets the chat history in st.session_state
    def reset_list(self):
        self.chat_history = []

    # Checks if the page has changed
    def check_page_change(self, url_path):
        current_page = url_path
        st.write(url_path, st.session_state.current_page)
        if current_page and current_page != st.session_state.current_page:
            #self.reset_list()
            st.session_state.current_page = current_page

    def create_baseline_answer(self):
        client = self.buildClient()
        answer = client.chat.completions.create(
            messages=[
                {"role": "system", "content": tx.baseline_prompt},]
            + [
                {"role": "user", "content": f"1) {tx.scenario_one} 2) {tx.scenario_two}"}],
            model=self.model_name,
            temperature=0.1,
            top_p=0.15
        )
        return answer

    # Initializes the prompt with current chat history and returns the chat stream    
    def generateStream(self, chat_history):
        client = self.buildClient()
        stream = client.chat.completions.create(
            messages=[
                {"role": "system", "content": f"{tx.chat_prompt} {st.session_state.baseline}. {self.hedging_variant}"},]
            + [
                {"role": current["role"], "content": current["content"]}
                for current in chat_history],
            model = self.model_name,
            stream = True
        )
        return stream