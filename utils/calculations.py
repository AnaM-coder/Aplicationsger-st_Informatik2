from utils.helpers import ch_now

def berechne_idealgewicht(geschlecht, groesse):
    if groesse < 152:
        return "Die Körpergröße sollte mindestens 152 cm betragen."

    if geschlecht.lower() == "männlich":
        idealgewicht = 50 + 0.905 * (groesse - 152)
    elif geschlecht.lower() == "weiblich":
        idealgewicht = 45.5 + 0.905 * (groesse - 152)  
    else:
        return "Ungültiges Geschlecht"
    
    result = {
        "timestamp": ch_now(),
        "geschlecht": geschlecht,   
        "groesse": groesse,
        "idealgewicht": round(idealgewicht, 2)
    }

    return result
