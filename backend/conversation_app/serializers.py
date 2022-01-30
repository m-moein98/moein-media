def conversation_serilaizer(conversation) -> dict:
    return {
        "_id": str(conversation["_id"]),
        "users": conversation["users"],
        "messages": conversation["messages"]
    }
