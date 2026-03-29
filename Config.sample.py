import os

# --- TELEGRAM CONFIGURATION ---
# This pulls your token and ID from your GitHub "Secrets"
telegram_active = True
telegram_bot_token = os.environ.get('TELEGRAM_TOKEN')
telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')

# --- NOTIFICATION SETTINGS (Leave as is) ---
smtp_active = False
slack_active = False

# --- THE "FLIP HUNTER" QUERIES ---
# catalog_ids '1256' = Video Games
queries = [
    # 1. BUNDLE HUNTER (£3 - £10)
    {
        'page': '1', 'per_page': '96',
        'search_text': 'job lot games bundle',
        'catalog_ids': '1256',
        'price_min': '3', 'price_max': '10',
        'order': 'newest_first',
    },
    {
        'page': '1', 'per_page': '96',
        'search_text': 'collection clearing out',
        'catalog_ids': '1256',
        'price_max': '10',
        'order': 'newest_first',
    },
    # 2. UNDERPRICED SINGLES (Up to £5)
    {
        'page': '1', 'per_page': '96',
        'search_text': 'nintendo zelda mario',
        'catalog_ids': '1256',
        'price_max': '5',
        'order': 'newest_first',
    },
    {
        'page': '1', 'per_page': '96',
        'search_text': 'pokemon gamecube ds 3ds',
        'catalog_ids': '1256',
        'price_max': '5',
        'order': 'newest_first',
    },
    # 3. PARENT/CLEAROUT TRAPS
    {
        'page': '1', 'per_page': '96',
        'search_text': 'son moved out games',
        'catalog_ids': '1256',
        'price_max': '15',
        'order': 'newest_first',
    },
    {
        'page': '1', 'per_page': '96',
        'search_text': 'kids games bundle',
        'catalog_ids': '1256',
        'price_max': '8',
        'order': 'newest_first',
    },
    # 4. MISSPELLED TRAPS
    {
        'page': '1', 'per_page': '96',
        'search_text': 'pokeman nintedo playstation',
        'catalog_ids': '1256',
        'price_max': '5',
        'order': 'newest_first',
    },
    # 5. GENERAL CATEGORY SNIPER
    # Catches anything new in Video Games under £4
    {
        'page': '1', 'per_page': '96',
        'search_text': ' ', 
        'catalog_ids': '1256',
        'price_max': '4',
        'order': 'newest_first',
    }
]

# --- WASTE FILTER ---
# Prevents notifications for low-value stock
exclude_keywords = [
    'fifa', 'pes', 'skylanders', 'disney infinity', 
    'singstar', 'wii fit', 'fortnite', 'destiny'
]
