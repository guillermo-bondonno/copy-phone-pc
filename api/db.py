db = []

def save_to_db(unique_id):
    db.append({"unique_id": unique_id, "data": None})

def update_in_db(data, unique_id):
    for item in db:
        if item["unique_id"] == unique_id:
            item["data"] = data
            break
    else:
        raise Exception("We shouldn't be updating something that doesn't exist!")
    

def get_from_db(unique_id):
    for item in db:
        if item["unique_id"] == unique_id:
            return item
    else:
        return {"error": "Not found"}