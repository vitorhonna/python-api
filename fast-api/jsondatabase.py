import json

print()


def add_user(name, email, score, user_id):
    newUser = {
        "name": name,
        "email": email,
        "score": score,
        "user_id": user_id,
        "link": f"http://www.example.com/{user_id}"
    }
    with open('data.json', 'r+') as handle:
        text_content = handle.read()
        if len(text_content) == 0:
            data = {
                "users": []
            }
        else:
            data = json.loads(text_content)
        users = data['users']
        users.append(newUser)
        data['users'] = users
        new_text_content = json.dumps(data)
        handle.seek(0)
        handle.truncate()
        handle.write(new_text_content)


def all_users():
    with open('data.json', 'r') as handle:
        text_content = handle.read()
        if len(text_content) == 0:
            data = {
                "users": []
            }
        else:
            data = json.loads(text_content)
        return data


def get_user(user_id):
    with open('data.json', 'r+') as handle:
        text_content = handle.read()
        if len(text_content) == 0:
            data = {
                "users": []
            }
        else:
            data = json.loads(text_content)
        users = data['users']
        for user in users:
            if user['user_id'] == user_id:
                return user
        return None
