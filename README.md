# Legal AI
A chatbot to help you navigate through the complicated paths of the AI regulations inside EU

Technically it is a RAG system implementation, using:
- LLM - ChatGPT 4.o
- VectorDB - ChromaDB
- Embedding functions - OpenAI
- Agents - LangChain 

It demonstrates how efficient this type of system could be for big documents as a context and how smart the LLM is on understanding legal terms.

For the purpose of this demo, the context is The Artificial Intelligence Act, document adopted by EU Parliament on 13 March 2024. The system could be easily extended to many other legal papers. 

### Installing
After cloning the repository the OpenAI key needs to be added as an environmental variable with the name OPENAI_API_KEY.
```bash
export OPENAI_API_KEY=your_key_value_here
```
After that it should be all fine. To run it localy, in the app folder use:
```bash
streamlit run app.py
```

### Demo
https://huggingface.co/spaces/firica/legalai
