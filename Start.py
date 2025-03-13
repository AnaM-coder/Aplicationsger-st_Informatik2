import streamlit as st
from utils.data_manager import DataManager

st.title("Idealgewicht Rechner")

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Idealgewicht Rechner")

st.markdown("Willkommen beim Idealgewicht Rechner 🎉, deinem persönlichen Wegweiser zu einem gesunden Körpergewicht!")
st.markdown("Dieser Rechner verwendet die Devine-Formel zur Berechnung des Idealgewichts.")

st.info("""Deine persönliche Ergebnisse können variieren, basierend auf weiteren Gesundheitsfaktoren!""")
st.info("""Bitte beachte, dass dies nur eine Schätzung ist und keine professionelle medizinische Beratung ersetzt!""")
st.info("""Wenn du Fragen zu deinem Idealgewicht hast, wende dich bitte an einen Arzt oder eine Ernährungsberatung!""")

st.write("Diese App wurde von Ana Maria Andrade (andraana@students.zhaw.ch) im Rahmen der Moduls 'BMLD Informatik 2' an der ZHAW entwickelt.")