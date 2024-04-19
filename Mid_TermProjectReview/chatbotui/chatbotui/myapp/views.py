# myapp/views.py
from django.shortcuts import render
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, GPT2TokenizerFast, GPT2Tokenizer
import os

def my_view(request):
    output_str = ''
    if request.method == 'POST':
        input_str = request.POST.get('input_str', '')
        output_str = generate_text(input_str, 200)
    return render(request, 'index.html', {'output_str': output_str})


def load_model(model_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return model


def load_tokenizer(tokenizer_path):
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer


def generate_text(sequence, max_length):
    model_path = "D:\IR_project\Information-Retrieval\model_output"
    print("Hello", os.path.exists(path= model_path))
    "chatbotui\myapp\views.py"
    model = load_model(model_path)
    tokenizer = load_tokenizer(model_path)
    ids = tokenizer.encode(f'{sequence}', return_tensors='pt')
    final_outputs = model.generate(
        ids,
        do_sample=True,
        max_length=max_length,
        pad_token_id=model.config.eos_token_id,
        top_k=50,
        top_p=0.95,
    )
    # print("Chatbot: ")
    # print(tokenizer.decode(final_outputs[0], skip_special_tokens=True))
    return tokenizer.decode(final_outputs[0], skip_special_tokens=True)


# sequence = input("User: ")
# max_len = 150
# generate_text(sequence, max_len)