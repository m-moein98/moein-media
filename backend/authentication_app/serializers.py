def user_serilaizer(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "email": user["email"],
        "createdAt": user["createdAt"],
        "lastSeen": user["lastSeen"]
    }
