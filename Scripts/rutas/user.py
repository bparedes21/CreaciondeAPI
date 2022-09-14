from fastapi import APIRouter

user=APIRouter()

@user.get("/")
def root():
    return {"message":"Hello i am API with router"}

    