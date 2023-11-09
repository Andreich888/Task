import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Выберите файл..")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=",", encoding="ptcp154")
    # df = pd.read_csv("./Task.csv", sep=",")
    df = df[['Номер заявки', 'Входящий номер', 'Время открытия',
             'Предельный срок в Naumen SD', 'Краткое описание',
             'Исполнитель', 'Номер связанного обращения ПР.Наумен.Индекс местопроведения работ',
             'Номер связанного обращения Isc Rp Naumen Place Address',
             'Затронутый КЕ Название КЕ']]

    df = df.rename(columns={df.columns[6]: 'Индекс'})

    options = st.multiselect(
        'Индекс ОПС', list(df.Индекс), []
    )
    Executor = st.multiselect(
        'Исполнитель', list(df.Исполнитель), []
    )
    # st.write(type(options[0]))
    st.write(df[df.Индекс.isin(options) | df.Исполнитель.isin(Executor)])

else:
    st.write("Загрузите файл..")

