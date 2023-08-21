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

opcoes = st.multiselect(
    'Itens da maleta:',
    ['Máquina', 'Carregador', 'Clivador', 'Decapador','Roleteador', 'V. de Alcool','Power Meter' ],
    )
st.write('Itens:', opcoes)


n_serie = st.text_input('Numero de série do item:')
st.write('Numero de série do item:', n_serie)

outros_itens = st.text_input('Outros itens:')
st.write('Outros itens:', outros_itens)

txt = st.text_area('Eventuais problemas:', ''' ''')
st.write('Eventuais problemas:', txt)


ramais = st.text_area('Ramal(s):', ''' ''')
st.write('Ramais:', ramais)

traco = '-'* 45

os = f'Quem entregou: {entregando}\n\nAss: {traco}\n\nAutorizado a pegar: {autorizado}\n\nAss: {traco}\n\nPosto de teste de atendimento: {posto_atendimento}\nPosto de teste da manutenção: {posto_manutencao}\nEventuais problemas: {txt}\nItens da maleta: {opcoes}\nOutros itens: {outros_itens}\nNumero de série do item: {n_serie}\nRamal(s): {ramais} '

st.download_button('Download',os, file_name = f'{entregando} {formatado}')

