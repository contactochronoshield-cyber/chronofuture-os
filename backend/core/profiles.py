profiles = {}

def create_profile(user_id: int, bio: str):
    profiles[user_id] = {
        "user_id": user_id,
        "bio": bio,
        "level": "Iniciado",
        "rank": "Chrono Citizen"
    }
    return profiles[user_id]

def get_profile(user_id: int):
    return profiles.get(user_id, "Perfil no existe")
