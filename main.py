import customtkinter as ctk
from datetime import datetime
import pytz
from config import fuseaux, display_names, abbrev_map
from utils import convert_time, get_diff_hours

# Fenêtre principale
app = ctk.CTk()
app.title("Horloge multi-fuseaux")
app.geometry("700x750")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Label pour UTC
utc_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
utc_label.pack(pady=10)

# Labels pour chaque fuseau
labels = {}
for tz in fuseaux.keys():
    lbl = ctk.CTkLabel(app, text="", font=("Arial", 16))
    lbl.pack(pady=5)
    labels[tz] = lbl

# Section conversion horaire
convert_frame = ctk.CTkFrame(app)
convert_frame.pack(pady=15)

ctk.CTkLabel(convert_frame, text="Conversion horaire :", font=("Arial", 16)).pack(pady=5)

tz_from_var = ctk.StringVar(value="America/New_York")
tz_to_var = ctk.StringVar(value="Europe/Paris")
hour_var = ctk.StringVar(value="08:00")

tz_from_menu = ctk.CTkOptionMenu(convert_frame, values=list(fuseaux.keys()), variable=tz_from_var)
tz_from_menu.pack(pady=3)
tz_to_menu = ctk.CTkOptionMenu(convert_frame, values=list(fuseaux.keys()), variable=tz_to_var)
tz_to_menu.pack(pady=3)

hour_entry = ctk.CTkEntry(convert_frame, textvariable=hour_var)
hour_entry.pack(pady=3)

convert_result_label = ctk.CTkLabel(convert_frame, text="", font=("Arial", 16))
convert_result_label.pack(pady=5)

def handle_conversion():
    result = convert_time(hour_var.get(), tz_from_var.get(), tz_to_var.get())
    convert_result_label.configure(
        text=f"{hour_var.get()} à {display_names[tz_from_var.get()]} → {result} à {display_names[tz_to_var.get()]}"
    )

convert_button = ctk.CTkButton(convert_frame, text="Convertir", command=handle_conversion)
convert_button.pack(pady=3)

# Section comparaison de fuseaux
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

# Fonction de mise à jour
def update_time():
    utc_now = datetime.now(pytz.utc)
    utc_label.configure(text=f"UTC : {utc_now.strftime('%H:%M:%S')}")

    for tz in fuseaux.keys():
        timezone = pytz.timezone(tz)
        now = datetime.now(timezone)
        abbrev = abbrev_map.get(tz, now.tzname() or now.strftime('%z'))
        formatted = now.strftime("%H:%M")
        labels[tz].configure(text=f"{display_names[tz]} : {formatted}")

    # Différence fuseaux
    diff_hours = get_diff_hours(tz1_var.get(), tz2_var.get())
    diff_label.configure(text=f"{display_names[tz1_var.get()]} → {display_names[tz2_var.get()]} : {diff_hours:+.1f} h")

    app.after(1000, update_time)

update_time()
app.mainloop()