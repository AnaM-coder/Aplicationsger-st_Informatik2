import streamlit as st

# Berechnung des Idealgewichts - Devine Formel
def berechne_idealgewicht(geschlecht, groesse):
    if groesse < 152:
        return "Die Körpergröße sollte mindestens 152 cm betragen."

    if geschlecht.lower() == "männlich":
        idealgewicht = 50 + 2.3 * (groesse - 152) / 2.54  # Umrechnung von cm in Zoll
    elif geschlecht.lower() == "weiblich":
        idealgewicht = 45.5 + 2.3 * (groesse - 152) / 2.54  # Umrechnung von cm in Zoll
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
        st.write("Die Körpergröße sollte mindestens 152 cm betragen.")
    else:
        idealgewicht = berechne_idealgewicht(geschlecht, groesse)
        st.write(f"Dein ideales Körpergewicht liegt bei: {idealgewicht} kg.")
import streamlit as st

if st.button("Start"):
    st.switch_page("IWC.py")