import js # Ez engedi, hogy a Python elérje a HTML elemeket
import datetime
import random

def gomb_kattintas(event):
    # Kiválasztjuk a HTML-ben lévő kijelzőt az ID-ja alapján
    kijelzo = js.document.getElementById("kijelzo")
    
    # Valamilyen Python logika (például egy véletlen szám és időpont)
    most = datetime.datetime.now().strftime("%H:%M:%S")
    veletlen_szam = random.randint(1, 100)
    
    # Frissítjük a kijelző tartalmát
    kijelzo.innerHTML = f"<b>Siker!</b><br>Idő: {most}<br>Szerencseszám: {veletlen_szam}"
    
    # Módosíthatunk stílust is Pythonból
    kijelzo.style.borderColor = "#34C759"
    kijelzo.style.borderStyle = "solid"
    kijelzo.style.borderWidth = "2px"

print("Python rendszer kész!")
