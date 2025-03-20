# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === BMI Grafik ===
import streamlit as st

st.title('📊Idealgewicht Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine IWC Daten vorhanden. Berechnen Sie Ihren IWC auf der Startseite.')
    st.stop()

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['groesse'],
                use_container_width=True)
st.caption('Größe über Zeit (m)')

# IWC over time
st.line_chart(data=data_df.set_index('timestamp')['idealgewicht'],
                use_container_width=True)
st.caption('IWC über Zeit')
