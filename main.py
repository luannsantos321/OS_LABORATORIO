import streamlit as st
from datetime import datetime, timedelta

agora = datetime.now() - timedelta(hours=3)
formatado = agora.strftime('%H:%M:%S')

st.title('O.S de máquinas Laboratório')

entregando = st.text_input('Quem entregou:')
st.write('Quem entregou:', entregando)

autorizado = st.text_input('Autorizado a pegar:')
st.write('Autorizado a buscar:', autorizado)

posto_atendimento = st.radio('Posto de teste de atendimento:', options= ['1','2','3','4','5','6'])

posto_manutencao = st.radio('Posto de teste da manutenção:', options= ['1','2','3','4','5','6'])


txt = st.text_area('Eventuais problemas:', ''' ''')
st.write('Eventuais problemas:', txt)


ramais = st.text_area('Ramal(s):', ''' ''', placeholder='Usuário - ramal')
st.write('Ramais:', ramais)

traco = '-'* 45

os = f'Quem entregou: {entregando}\n\nAss: {traco}\n\nAutorizado a pegar: {autorizado}\n\nAss: {traco}\n\nPosto de teste de atendimento: {posto_atendimento}\nPosto de teste da manutenção: {posto_manutencao}\nEventuais problemas: {txt}\nRamal(s): {ramais} '
st.download_button('Download',os, file_name = formatado)

