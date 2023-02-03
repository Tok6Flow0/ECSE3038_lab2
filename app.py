# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

#---------------------------------------
#LAB START
#---------------------------------------

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []

@app.get("/todos")
async def get_all_todos():
  return fake_database

@app.post("/todos")
async def create_todo(request: Request):
  todo = await request.json()
  fake_database.append(todo)
  return todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
  for index, todo in enumerate(fake_database):
    if todo.get("id") == todo_id:
      del fake_database[index]
      return {"message": "Todo deleted"}
  return {"message": "Todo not found"}

@app.patch("/todos/{todo_id}")
async def update_todo_by_id(todo_id: int, request: Request):
  todo_update = await request.json()
  for todo in fake_database:
    if todo.get("id") == todo_id:
      todo.update(todo_update)
      return {"message": "Todo updated"}
  return {"message": "Todo not found"}