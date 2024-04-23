# myapp/views.py
from django.shortcuts import render
# from transformers import PreTrainedTokenizerFast, GPT1LMHeadModel, GPT2TokenizerFast, GPT2Tokenizer
import os
from langchain.chains import create_retrieval_chain
import pickle
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def my_view(request):
    output_str = ''
    if request.method == 'POST':
        input_str = request.POST.get('input_str', '')
        output_str = generate_text(input_str)
    return render(request, 'index.html', {'output_str': output_str})

def generate_text(user_query):
    
    with open("/home/najiya/Desktop/Arpan/IR_Project/compress_file_chatbot/myapp/static/vector", "rb") as f:
        vector = pickle.load(f)

    retriever = vector.as_retriever()

    # retriever = vector.as_retriever()

    # First we need a prompt that we can pass into an LLM to generate this search query

    prompt = ChatPromptTemplate.from_template(""" 
        A document is provided for some schemes
                                            by the states of Delhi, UP, Haryana, Rajasthan, Maharashtra
                                            and some schemes by the Central Government. 
                                            Take information from the document and answer
                                            people's questions. Search the document first.
                                            If you can't find relevant data, look it up.
        We have sentiment analysed social media posts in the document too.
        A post's rating of 0 means negative, 1 means neutral and 2 means positive sentiments.
        You have to perform data analysis on the documents using these as requested. Give a brief
        view about people's opinions on a scheme if asked. If there are profane words, ignore those
        posts.
        Given a user conversation, search the document first to
        get information relevant to the conversation. If nothing is found, look it up.

    <context>
    {context}
    </context>

    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    # retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    retrieval_chain = create_retrieval_chain(retriever, document_chain)


    response = retrieval_chain.invoke({"input": """" {user_query}"""})
    print(response['answer'])

    return response['answer']