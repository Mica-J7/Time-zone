fuseaux = {
    "Europe/Lisbon": "Lisbonne",
    "Europe/Paris": "Paris",
    "Europe/Moscow": "Moscou",
    "Asia/Dubai": "Dubaï",
    "Asia/Kolkata": "New Delhi",
    "Asia/Shanghai": "Pékin",
    "Asia/Tokyo": "Tokyo",
    "Australia/Sydney": "Sydney",
    "America/New_York": "New York",
    "America/Chicago": "Chicago",
    "America/Denver": "Denver",
    "America/Los_Angeles": "Los Angeles",
    "America/Sao_Paulo": "São Paulo",
    "Africa/Johannesburg": "Johannesburg"
}

abbrev_map = {
    "Europe/Lisbon": "WET",
    "Europe/Paris": "CET",
    "Europe/Moscow": "MSK",
    "Asia/Dubai": "GST",
    "Asia/Kolkata": "IST",
    "Asia/Shanghai": "CST",
    "Asia/Tokyo": "JST",
    "Australia/Sydney": "AEST",
    "America/New_York": "EST",
    "America/Chicago": "CST",
    "America/Denver": "MST",
    "America/Los_Angeles": "PST",
    "America/Sao_Paulo": "BRT",
    "Africa/Johannesburg": "SAST"
}

display_names = {k: f"{v} ({abbrev_map[k]})" for k, v in fuseaux.items()}