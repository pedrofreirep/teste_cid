import pandas as pd
import numpy as np
import zipfile
import streamlit as st
import altair as alt
from PIL import Image
from io import BytesIO
import webbrowser
import streamlit
import re
import time
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image


from streamlit import caching


zf_2 = zipfile.ZipFile('sep2.zip') 

@st.cache(allow_output_mutation=True) #Ler base de procedimentos por beneficiários
def get_data():
	return pd.read_csv(zf_2.open("sep.csv"))
df = get_data()


df['id_pessoa'].replace({'2b617ace585e62a590d2f322a02429da':'Indivíduo 1', 'ad5791c1e122deb7829724030c539e5b':'Indivíduo 2', '68e91bae36bfc73aad2bbf5288c65131':'Indivíduo 3', 'def81392db738417e2a3ffa815901b3a':'Indivíduo 4', 'e71160773d49cf47c791505e535a13f8':'Indivíduo 5', '35efaae352a35224a86b0afac09c58c6':'Indivíduo 6'}, inplace=True)

lista_pessoa = ['-']
for x in df['id_pessoa'].unique():
    lista_pessoa.append(x)

lista_pessoa.sort()
pessoa = st.selectbox('Avaliar o histórico de:', lista_pessoa, index=0, format_func=str, key=None)

if pessoa != '-':
	df_aux = df[df['id_pessoa'] == pessoa]

	visual = st.selectbox('Visualizar:', ['Subgrupos', 'Procedimentos', 'Histórico'], index=0, format_func=str, key=None)
	
	if visual == 'Subgrupos':
		st.subheader('Subgrupos únicos:')
		st.table(df_aux['Subgrupo'].unique())
	elif visual == 'Procedimentos':
		st.subheader('Procedimentos únicos:')
		st.table(df_aux['DescricaoProcedimentoFinal'].unique())
	elif visual == 'Histórico':
		st.subheader('Histórico completo:')
		st.table(df_aux[['sexo', 'idade_cat', 'dt_utilizacao', 'DescricaoProcedimentoFinal', 'Subgrupo']].sort_values('dt_utilizacao', ascending = False))

else:
	st.title('Para começar o teste escolha um indivíduo')


# if st.button('Salvar resposta'):
# 	st.balloons()
# 	st.success('Resposta salva!')



