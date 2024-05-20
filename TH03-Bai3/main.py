from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    username: str
    password: str

class Student(BaseModel):
    id: int
    name: str
    age: int
    address: str
    phone: str
    email: str
    class_name: str

students = [
    {"id": 1, "name": "Nguyen Van A", "age": 19, "address": "122 Hoang Quoc Viet", "phone": "0123-456-789", "email": "adeptrai@gmail.com", "class_name": "CC01"},
    {"id": 2, "name": "Nguyen Van B", "age": 20, "address": "456 Nguyen Trai-Ha Dong", "phone": "0987-654-321", "email": "bbuonba@gmail.com", "class_name": "CC02"},
    # Add more students as needed
]

@app.post("/login")
def login(login_request: LoginRequest):
    if login_request.username == "admin" and login_request.password == "admin":
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/students")
def get_students():
    return students

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
