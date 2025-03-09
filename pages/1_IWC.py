import streamlit as st
import numpy as np
import pandas as pd

# Berechnung des Idealgewichts - Devine Formel
def berechne_idealgewicht(geschlecht, groesse):
    if groesse < 152:
        return "Die Körpergröße sollte mindestens 152 cm betragen."

    if geschlecht.lower() == "männlich":
        idealgewicht = 50 + 0.905 * (groesse - 152)
    elif geschlecht.lower() == "weiblich":
        idealgewicht = 45.5 + 0.905 * (groesse - 152)  
    else:
        return "Ungültiges Geschlecht"

    return round(idealgewicht, 2)

st.title("Idealgewicht Rechner")

st.markdown("Dieser Rechner verwendet die Devine-Formel zur Berechnung des Idealgewichts.")

# Formular erstellen
with st.form(key="idealgewicht_form"):
    # Benutzeroberfläche innerhalb des Formulars
    geschlecht = st.selectbox("Wähle dein Geschlecht", ["männlich", "weiblich"])
    groesse = st.number_input("Gib deine Körpergröße in cm ein:", min_value=152, max_value=300)

# Berechnungsbutton innerhalb des Formulars
    submit_button = st.form_submit_button("Berechnen")

# Wenn das Formular abgesendet wird
if submit_button:
    if groesse < 152:
        st.error("Die Körpergröße sollte mindestens 152 cm betragen.")
    else:
        idealgewicht = berechne_idealgewicht(geschlecht, groesse)
        st.success(f"Dein ideales Körpergewicht liegt bei: {idealgewicht} kg.")

# Diagramm für das Idealgewicht basierend auf der Körpergröße und Geschlecht
        groessen = np.arange(152, 201, 1)  # Größenspanne von 152 bis 200 cm
        gewicht_mann = 50 + 0.905 * (groessen - 152)  # Berechnung für Männer
        gewicht_frau = 45.5 + 0.905 * (groessen - 152)  # Berechnung für Frauen

# Umwandlung der Daten in ein DataFrame für die Nutzung mit Streamlit

df = pd.DataFrame({
            'Körpergröße (cm)': groessen,
            'Männlich Idealgewicht (kg)': gewicht_mann,
            'Weiblich Idealgewicht (kg)': gewicht_frau
        })
# Zeigen der Liniendiagramms basierend auf der Körpergröße
st.subheader("Idealgewicht basierend auf Körpergröße")
st.line_chart(df.set_index('Körpergröße (cm)'))