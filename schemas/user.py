def userEntity(item) -> dict:
    return {
        # # 'id': item['id'],
        # 'id': str(item['_id']),
        'id': str(item['_id']) if type(item['_id']) != str else item['_id'],
        'name': item['name'],
        'email': item['email'],
        'password': item['password']
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def userNotPasswordEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'email': item['email'],
    }