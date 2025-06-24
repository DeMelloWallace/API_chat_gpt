import streamlit as st
import os
import openai

# Aqui utilizaremos a key de API openAi
openai.api_key = 'Insira chave API ChatGPT'

#Função para interagir com chat gpt(from gpt import professor_virtual1)
def professor_virtual1(prompt):
    try:
        response = openai.ChatCompletion.create(
            model = 'gpt - 3.5 - turbo',
            messages = [
                {'role': 'system', 'content:': 'You are an English teacher.'},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens = 150,
            temperature = 0.7,
        )
        return response.choices[0].message ['content'].strip()
    except Exception as e:
        st.error(f'Erro ao se comunicar com API: {e}')
        return 'Desculpe, houve um problema ao processar sua solicitação.'



st.set_page_config(layout = 'centered') #Centraliza o layout da página
st.title("Chat de inglês com Professor Virtual ")

user_input = st.text_input('You: ', '')

if user_input: 1
prompt = f'Aluno: {user_input}\n Professor de Inglês:'
response = professor_virtual1(prompt)
st.text_area('Professor: ', value = response, height = 200)

st.write('Digite sua pergunta ou frase em Inglês e pressione Enter para obter uma resposta do professor de Inglês virtual.')




