# from huggingface_hub import hf_hub_download
# hf_hub_download(repo_id="TheBloke/Llama-2-7B-Chat-GGML", filename="llama-2-7b-chat.ggmlv3.q2_K.bin")

import streamlit as st
from langchain.llms import CTransformers

llm = CTransformers(
    model=".cache/huggingface/hub/models--TheBloke--Llama-2-7B-Chat-GGML/snapshots/76cd63c351ae389e1d4b91cab2cf470aab11864b/llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title('Gerador de poemas')

content = st.text_input('Escreva um poema com o tema')

if st.button('Solicite o poema'):
    with st.spinner('escrevendo ...'):
        result = llm.predict("Você é um escritor de poemas em português brasileiro. Escreva um poema com o tema " + content)
        st.write(result)