posts = []

def create_post(user: str, content: str):
    post = {
        "id": len(posts) + 1,
        "user": user,
        "content": content
    }
    posts.append(post)
    return post

def get_posts():
    return posts
