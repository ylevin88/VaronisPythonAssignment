import json
from sanic import Sanic
from sanic import response
from sanic_jwt import exceptions, protected
from sanic_jwt import initialize

users_dict = {}
app = Sanic("Normalizer App")


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user_password = users_dict.get(username, None)
    if user_password is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user_password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return {'user': username}


@app.route("/", methods=['POST'])
@protected()
def normilize_data(request):
    data = request.json
    res = {}
    for d in data:
        name = d['name']
        for key in d.keys():
            if 'val' in key.lower():
                value = d[key]
                break
        res[name] = value
    # normalized = normilize_data(j)
    return response.json(res)


if __name__ == '__main__':
    with open('users.json', 'r')as users_file:
        users = json.load(users_file)
    users_dict = {user['user']: user['password'] for user in users}

    initialize(app, authenticate=authenticate)
    app.run(host="0.0.0.0", port=8000, debug=True)
