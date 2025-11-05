import customtkinter as ctk
from datetime import datetime
import pytz

# Fenêtre principale
app = ctk.CTk()
app.title("Horloge multi-fuseaux")
app.geometry("500x300")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Liste des fuseaux horaire à afficher
fuseaux = {
    "Europe/Lisbon": "Lisbonne (Portugal)",
    "Europe/Paris": "Paris (France)",
    "Europe/Moscow": "Moscou (Russie)",
    "Asia/Dubai": "Dubaï (Émirats)",
    "Asia/Kolkata": "New Delhi (Inde)",
    "Asia/Shanghai": "Pékin (Chine)",
    "Asia/Tokyo": "Tokyo (Japon)",
    "Australia/Sydney": "Sydney (Australie)",
    "America/New_York": "New York (USA)",
    "America/Chicago": "Chicago (USA)",
    "America/Denver": "Denver (USA)",
    "America/Los_Angeles": "Los Angeles (USA)",
    "America/Sao_Paulo": "São Paulo (Brésil)",
    "Africa/Johannesburg": "Johannesburg (Afrique du Sud)"
}

# Label pour UTC
utc_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
utc_label.pack(pady=10)

# Labels dynamiques pour chaque fuseau
labels = {}
for tz, name in fuseaux.items():
    lbl = ctk.CTkLabel(app, text="", font=("Arial", 18), text_color="white")
    lbl.pack(pady=5)
    labels[tz] = lbl

# Section pour comparer deux fuseaux
compare_frame = ctk.CTkFrame(app)
compare_frame.pack(pady=20)

tz1_var = ctk.StringVar(value=list(fuseaux.keys())[0])
tz2_var = ctk.StringVar(value=list(fuseaux.keys())[1])

tz1_menu = ctk.CTkOptionMenu(compare_frame, values=list(fuseaux.keys()), variable=tz1_var)
tz1_menu.pack(side="left", padx=5)

tz2_menu = ctk.CTkOptionMenu(compare_frame, values=list(fuseaux.keys()), variable=tz2_var)
tz2_menu.pack(side="left", padx=5)

diff_label = ctk.CTkLabel(compare_frame, text="", font=("Arial", 16))
diff_label.pack(side="left", padx=10)

# Fonction pour mettre à jour l'heure
def update_time():
    utc_now = datetime.now(pytz.utc)
    utc_label.configure(text=f"UTC : {utc_now.strftime('%H:%M:%S')}")

    for tz, name in fuseaux.items():
        timezone = pytz.timezone(tz)
        now = datetime.now(timezone)
        abbrev = now.tzname() # Abreviation des fuseaux horaire
        formatted = now.strftime("%H:%M:%S")
        labels[tz].configure(text=f"{name} ({abbrev}) : {formatted}")

    # Calcul de la différence entre tz1 et tz2
    tz1_key = tz1_var.get()
    tz2_key = tz2_var.get()
    now1 = datetime.now(pytz.timezone(tz1_key))
    now2 = datetime.now(pytz.timezone(tz2_key))
    diff_hours = (now1 - now2).total_seconds() / 3600
    diff_label.configure(text=f"{fuseaux[tz1_key]} → {fuseaux[tz2_key]} : {diff_hours:+.1f} h")

    app.after(1000, update_time) # Mise à jour chaque seconde

update_time()
app.mainloop()