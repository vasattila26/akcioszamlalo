import js

def szamold_ki(event):
    # Elemek elérése
    input_ar = js.document.getElementById("eredeti_ar")
    input_szazalek = js.document.getElementById("szazalek")
    kijelzo_szam = js.document.getElementById("eredmeny_szam")
    
    try:
        # Értékek beolvasása és számmá alakítása
        ar = float(input_ar.value)
        szazalek = float(input_szazalek.value)
        
        # A matek: Akciós ár = Eredeti * (1 - kedvezmény/100)
        vegosszeg = ar * (1 - szazalek / 100)
        
        # Megjelenítés (ezresek csoportosításával)
        formazott_osszeg = "{:,.0f}".format(vegosszeg).replace(",", " ")
        kijelzo_szam.innerHTML = f"{formazott_osszeg} Ft"
        
        # Siker esetén egy kis zöld villanás a kijelzőn
        js.document.getElementById("kijelzo").style.borderColor = "#34C759"
        
    except ValueError:
        # Ha nem számot írtál be, vagy üres valamelyik mező
        kijelzo_szam.innerHTML = "Hiba!"
        js.document.getElementById("kijelzo").style.borderColor = "#ff3b30"
