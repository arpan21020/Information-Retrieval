<h1>Instructions to run the Chatbot</h1>
<li> Install the django using command "pip install django"
<li>Change the directory to chatbotui and start the server using the command "python3 manage.py runserver"  

<h1>Youtube link</h1>
<a href="https://youtu.be/5A3tYNWGA64">https://youtu.be/5A3tYNWGA64</a>

<h1>Comparison with baselines and the system's performance on existing data and SOTA on different evaluation metrics + how the system performs on new data / handles different cases.</h1>
<p>The model prompt template helps in assigning the LLM a role and refining its responses. We have given LangChain and Llama a prompt template explaining that the input file is a CSV with sentiment analysed social media posts and information about government schemes. It is then instructed to refer this document first. If it can't find relevant information in the document, it should generate it itself. If it still can't understand the user input, it will output an apology and ask to input again with an understandable prompt. This helps in completeness of the output. It also safeguards against fake data creeping in.</p>


