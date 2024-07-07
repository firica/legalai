import streamlit as ST
import agent as Agent
import utils as Utils
import embed
import os as OS

def create_chat(id: str):
    chat = ST.container()

    # Initialize chat history
    if "messages" not in ST.session_state:
        ST.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in ST.session_state.messages:
        if message['id'] == id:
            chat.chat_message(message['role']).write(message['content'])
    
    ST.session_state.newschat = Agent.NewsChat(id)
 
    # Accept user input
    if prompt := ST.chat_input(placeholder = "Ask me about AI legal stuff in the EU", key = id):

        chat.chat_message("user").write(prompt)
        with ST.spinner('Wait for it...'):
            assistant_response = ST.session_state.newschat.ask(prompt)
            chat.chat_message("assistant").write(f"{assistant_response}")

        ST.session_state.messages.append({"id": id, "role": "user", "content": prompt})
        ST.session_state.messages.append({"id": id, "role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    if not OS.path.exists(Utils.DB_FOLDER):
        document_name = "Artificial Intelligence Act"
        document_description = "Artificial Intelligence Act"
        text = embed.pdf_to_text(Utils.EUROPEAN_ACT_URL)
        embed.embed_text_in_chromadb(text, document_name, document_description)

    create_chat("chat1")
