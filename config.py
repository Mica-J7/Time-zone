fuseaux = {
    "Europe/Paris": "Paris (France)",
    "Europe/Kiev": "Kiev (Ukraine)",
    "Europe/Moscow": "Moscou (Russie)",
    "Asia/Dubai": "Dubaï (Émirats)",
    "Asia/Kolkata": "New Delhi (Inde)",
    "Asia/Shanghai": "Pékin (Chine)",
    "Asia/Tokyo": "Tokyo (Japon)",
    "Australia/Sydney": "Sydney (Australie)",
    "America/Los_Angeles": "Los Angeles (USA)",
    "America/Denver": "Denver (USA)",
    "America/Chicago": "Chicago (USA)",
    "America/New_York": "New York (USA)",
    "America/Sao_Paulo": "São Paulo (Brésil)",
    "Europe/Lisbon": "Lisbonne (Portugal)"
}

abbrev_map = {
    
    "Europe/Paris": "CET",
    "Europe/Kiev": "EET",
    "Europe/Moscow": "MSK",
    "Asia/Dubai": "GST",
    "Asia/Kolkata": "IST",
    "Asia/Shanghai": "CST",
    "Asia/Tokyo": "JST",
    "Australia/Sydney": "AEST",
    "America/Los_Angeles": "PST",
    "America/Denver": "MST",
    "America/Chicago": "CST",
    "America/New_York": "EST",
    "America/Sao_Paulo": "BRT",
    "Europe/Lisbon": "WET",
}

display_names = {k: f"{v} ({abbrev_map[k]})" for k, v in fuseaux.items()}