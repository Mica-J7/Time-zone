import customtkinter as ctk
from datetime import datetime
import pytz
from config import fuseaux, display_names, abbrev_map
from utils import convert_time, get_diff_hours

# --- Fenêtre principale ---
app = ctk.CTk()
app.title("Horloge multi-fuseaux")
app.geometry("700x750")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Scrollable frame globale ---
main_frame = ctk.CTkScrollableFrame(app, width=700, height=750)
main_frame.pack(fill="both", expand=True)

# --- UTC ---
utc_label = ctk.CTkLabel(main_frame, text="", font=("Arial", 16))
utc_label.pack(pady=10)

# --- Frame pour bouton + checkboxes ---
checkbox_container = ctk.CTkFrame(main_frame)
checkbox_container.pack(pady=10, fill="x")

# Frame contenant réellement les checkboxes
select_frame = ctk.CTkFrame(checkbox_container)
select_frame.pack(pady=5, fill="x")

ctk.CTkLabel(select_frame, text="Fuseaux horaires :", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0,5))

# --- Création des checkboxes multi-colonnes ---
selected_tz = {}
col_count = 3  # nombre de colonnes
for i, tz in enumerate(fuseaux.keys()):
    var = ctk.BooleanVar(value=True)
    cb = ctk.CTkCheckBox(select_frame, text=display_names[tz], variable=var)
    row = (i // col_count) + 1  # +1 pour le label
    col = i % col_count
    cb.grid(row=row, column=col, sticky="w", padx=10, pady=2)
    selected_tz[tz] = var

# Bouton toggle
toggle_button = ctk.CTkButton(checkbox_container, text="Masquer les fuseaux")
toggle_button.pack(pady=5)

# Fonction toggle
def toggle_checkboxes():
    if select_frame.winfo_ismapped():
        select_frame.pack_forget()
        toggle_button.configure(text="Afficher les fuseaux")
    else:
        select_frame.pack(pady=5, fill="x", before=toggle_button)
        toggle_button.configure(text="Masquer les fuseaux")

toggle_button.configure(command=toggle_checkboxes)


# --- Frame pour les labels dynamiques ---
labels_frame = ctk.CTkFrame(main_frame)
labels_frame.pack(pady=10, fill="x")

labels = {}
for tz in fuseaux.keys():
    lbl = ctk.CTkLabel(labels_frame, text="", font=("Arial", 16))
    lbl.pack_forget()
    labels[tz] = lbl

# --- Conversion ---
convert_frame = ctk.CTkFrame(main_frame)
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

convert_button = ctk.CTkButton(
    convert_frame,
    text="Convertir",
    command=lambda: convert_result_label.configure(
        text=f"{hour_var.get()} à {display_names[tz_from_var.get()]} → "
             f"{convert_time(hour_var.get(), tz_from_var.get(), tz_to_var.get())} "
             f"à {display_names[tz_to_var.get()]}"
    )
)
convert_button.pack(pady=3)

# --- Comparaison ---
compare_frame = ctk.CTkFrame(main_frame)
compare_frame.pack(pady=20)

tz1_var = ctk.StringVar(value=list(fuseaux.keys())[0])
tz2_var = ctk.StringVar(value=list(fuseaux.keys())[1])

tz1_menu = ctk.CTkOptionMenu(compare_frame, values=list(fuseaux.keys()), variable=tz1_var)
tz1_menu.pack(side="left", padx=5)
tz2_menu = ctk.CTkOptionMenu(compare_frame, values=list(fuseaux.keys()), variable=tz2_var)
tz2_menu.pack(side="left", padx=5)

diff_label = ctk.CTkLabel(compare_frame, text="", font=("Arial", 16))
diff_label.pack(side="left", padx=10)

# --- Mise à jour ---
def update_time():
    utc_now = datetime.now(pytz.utc)
    utc_label.configure(text=f"UTC : {utc_now.strftime('%H:%M:%S')}")

    for lbl in labels.values():
        lbl.pack_forget()

    for tz in fuseaux.keys():
        if selected_tz[tz].get():
            timezone = pytz.timezone(tz)
            now = datetime.now(timezone)
            formatted = now.strftime("%H:%M")
            labels[tz].configure(text=f"{display_names[tz]} : {formatted}")
            labels[tz].pack(pady=5)

    diff_hours = get_diff_hours(tz1_var.get(), tz2_var.get())
    diff_label.configure(
        text=f"{display_names[tz1_var.get()]} → {display_names[tz2_var.get()]} : {diff_hours:+.1f} h"
    )

    app.after(1000, update_time)

update_time()
app.mainloop()