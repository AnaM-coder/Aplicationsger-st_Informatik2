import streamlit as st

# Berechnung des Idealgewichts -  Devine Formel
def berechne_idealgewicht(geschlecht, groesse):
    if geschlecht.lower() == "männlich":
        idealgewicht = 50 + 2.3 * (groesse - 152) / 2.54  # Umrechnung von cm in Zoll
    elif geschlecht.lower() == "weiblich":
        idealgewicht = 45.5 + 2.3 * (groesse - 152) / 2.54  # Umrechnung von cm in Zoll
    else:
        return "Ungültiges Geschlecht"

    return round(idealgewicht, 2)

st.title("Idealgewicht Rechner")

st.markdown("Diese Rechner verwendet die älteste und bekannteste Methode zur Berechnung des Idealgewichts. Diese bewährte Formel gibt dir eine einfache und schnelle Einschätzung deines Idealgewichts basierend auf deiner Körpergröße und deinem Geschlecht.")

# Benutzeroberfläche
geschlecht = st.selectbox("Wähle dein Geschlecht", ["männlich", "weiblich"])
groesse = st.number_input("Gib deine Körpergröße in cm ein:", min_value=50, max_value=300)

# Berechnungsbutton
if st.button("Berechnen"):
    idealgewicht = berechne_idealgewicht(geschlecht, groesse)
    st.write(f"Dein ideales Körpergewicht liegt bei: {idealgewicht} kg.")