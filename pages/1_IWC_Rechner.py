# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st
from ideal_weight_calculator import calculate_iwc

st.title('IWC Rechner')

with st.form("IWC Eingabeformular"):
    # User input geschlecht und Körpergröße
    geschlecht = st.selectbox("Wähle dein Geschlecht", ["männlich", "weiblich"])
    groesse = st.number_input("Gib deine Körpergröße in cm ein:", min_value=152, max_value=300)

    # submit button.
    submitted = st.form_submit_button("Submit")
    
if submitted:
    result = calculate_bmi(height, weight)
    st.write(f'Ihr IWC ist: {result["iwc"]}')
    st.write(f'Berechnet am: {result["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')
    st.write(f'Kategorie: {result["category"]}')
        
    # --- IWC data speichern---
    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)  # update data in session state and storage

