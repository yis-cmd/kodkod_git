import requests
import fastapi

def exe_1():
    result = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = result.json()
    print(
        f"Name: {data.get('name')}\nEmail: {data.get('email')}\nCity: {data.get('address').get("city")}"
    )

    posts = requests.get("https://jsonplaceholder.typicode.com/posts")
    amount = len(posts.json())
    print(amount)

    user2_posts = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
    for post in user2_posts.json():
        print(post.get("title"))


def safe_get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    raise Exception(response.status_code)

app = fastapi.FastAPI()
@app.get("/greet")
def greet(name:str = "world"):
    return {"message": f"Hello, {name}!"}


def exe_4():
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    for post in posts:
        for user in users:
            if post.get("userId") == user.get("id"):
                post["name"] = user.get("name")
    for post in posts:
        print(f"{post.get("title")} by {post.get("name")}")


def exe_4_v2():
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    id_users = {user.get("id"):user for user in users}
    for post in posts:
        post["name"] = id_users.get(post.get("userId")).get("name") #type: ignore
    for post in posts:
        print(f"{post.get("title")} by {post.get("name")}")



#exe 5
    """
    1. get "/" to get the using instructions
    2. post "/add_task" adding a task
    3. get "/get_tasks" getting tasks by param filters
    4. patch "/update_task/task_name" updating task by name
    5. delete "/delete_task/task_name" delete task by name
    """
