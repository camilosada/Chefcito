from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

from router import item_router


app.include_router(item_router.router, prefix='/items')


@app.get('/', status_code=200)
def read_root():
    return {'Welcome':'Chefcito is all ready to go!'}








#--------------------------------------------------------------------------------------------------------
"""# Post model 
class Post(BaseModel):
    id: Optional[str]
    title: str
    author:str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool= False

@app.get('/')
def read_root():
    return {"Welcome":"Welcome to the Jungle"}

@app.get('/posts')
def get_post():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id=str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail='Post Not found')

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for i_post, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(i_post)
            return {"message": post_id + " has been deleted"}
    raise HTTPException(status_code=404, detail='Post Not found')

@app.put('/posts/{post_id}')
def updated_post(post_id: str, updated_post: Post):
    for i_post, post in enumerate(posts):
        if post["id"] == post_id:
            posts[i_post]["title"] = updated_post.title
            posts[i_post]["author"] = updated_post.author
            posts[i_post]["content"] = updated_post.content
            return {"message": post_id + " has been updated"}
    raise HTTPException(status_code=404, detail='Post Not found')"""