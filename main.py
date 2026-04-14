from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client["taskdb"]

SECRET = "secret123"
pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(pw):
    return pwd_context.hash(pw)

def verify_password(pw, hashed):
    return pwd_context.verify(pw, hashed)

def create_token(data):
    return jwt.encode(data, SECRET, algorithm="HS256")

def get_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/api/v1/auth/register")
def register(user: dict):
    user["password"] = hash_password(user["password"])
    db.users.insert_one(user)
    return {"msg": "User created"}

@app.post("/api/v1/auth/login")
def login(user: dict):
    db_user = db.users.find_one({"email": user["email"]})
    if not db_user or not verify_password(user["password"], db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_token({"id": str(db_user["_id"]), "role": db_user.get("role","user")})
    return {"access_token": token}

@app.get("/api/v1/tasks")
def get_tasks(user=Depends(get_user)):
    tasks = list(db.tasks.find({"user": user["id"]}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks

@app.post("/api/v1/tasks")
def create_task(task: dict, user=Depends(get_user)):
    task["user"] = user["id"]
    db.tasks.insert_one(task)
    return {"msg": "Task created"}

@app.put("/api/v1/tasks/{task_id}")
def update_task(task_id: str, data: dict, user=Depends(get_user)):
    db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data})
    return {"msg": "Updated"}

@app.delete("/api/v1/tasks/{task_id}")
def delete_task(task_id: str, user=Depends(get_user)):
    db.tasks.delete_one({"_id": ObjectId(task_id)})
    return {"msg": "Deleted"}
