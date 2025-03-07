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



# Benutzeroberfläche
geschlecht = st.selectbox("Wähle dein Geschlecht", ["männlich", "weiblich"])
groesse = st.number_input("Gib deine Körpergröße in cm ein:", min_value=50, max_value=300)

# Berechnungsbutton
if st.button("Berechnen"):
    idealgewicht = berechne_idealgewicht(geschlecht, groesse)
    st.write(f"Dein ideales Körpergewicht liegt bei: {idealgewicht} kg.")

st.markdown("Wilkommen beim Idealgewicht Rechner 🎉 deinem persönlichen Wegweiser zu einem gesunden Körpergewicht!")
st.markdown("🏃 Diese Rechner vewendet die ältesten und bekanntesten Methode zur Berechnung des Idealgewichts. Diese bewärte Formel, gibt dir eine einfache und schnelle Einschätzung deines Idealgewichts basierend auf deiner Körpergröße und deinem Geschlecht. 🏃")
        
# Add some health advice
st.info("""Deine persönliche Ergebnisse können variieren, basierend auf weiteren Gesundheitsfaktoren!""")
st.info("""Bitte beachte, dass dies nur eine Schätzung ist und keine professionelle medizinische Beratung ersetzt!""")
st.info("""Wenn du Fragen zu deinem Idealgewicht hast, wende dich bitte an deinen Arzt oder Ernährungsberatung!""")

