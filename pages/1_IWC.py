import streamlit as st

st.title("Idealgewicht Rechner")

# Berechnung des Idealgewichts -  Devine Formel
def berechne_idealgewicht(geschlecht, groesse):
    if geschlecht.lower() == "männlich":
        idealgewicht = 50 + 2.3 * (groesse - 152) / 2.54  # Umrechnung von cm in Zoll
    elif geschlecht.lower() == "weiblich":
        idealgewicht = 45.5 + 2.3 * (groesse - 152) / 2.54  # Umrechnung von cm in Zoll
    else:
        return "Ungültiges Geschlecht"

    return round(idealgewicht, 2)

# titel
st.title("Idealgewicht Rechner")

# Benutzeroberfläche
geschlecht = st.selectbox("Wähle dein Geschlecht", ["männlich", "weiblich"])
groesse = st.number_input("Gib deine Körpergröße in cm ein:", min_value=50, max_value=300)

# Berechnungsbutton
if st.button("Berechnen"):
    idealgewicht = berechne_idealgewicht(geschlecht, groesse)
    st.write(f"Dein ideales Körpergewicht liegt bei: {idealgewicht} kg.")

