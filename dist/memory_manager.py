# memory_manager.py

import json
import os

MEMORY_FILE = "zizah_memory.json"

def load_memory():
    """Memuat data ingatan dari file JSON."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Jika file korup atau kosong, kembalikan state default
                return get_default_memory()
    else:
        return get_default_memory()

def save_memory(data):
    """Menyimpan data ingatan ke file JSON."""
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=5, ensure_ascii=False)

def get_default_memory():
    """Mengembalikan struktur data ingatan default."""
    return {
        "user_name": None,
        "user_hobby": None,
        "conversation_history": [],
        "learned_vocabulary": [], # Use list for JSON serialization
        "human_traits": [],
        "document_insights": []
    }
