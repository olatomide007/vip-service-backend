from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from .schemas import APIKey, Signup, SignupResponse, ChangePassword

router = APIRouter()


@router.post("/signup", response_model=SignupResponse)
async def create_user(signup: Signup):
    return signup


@router.get("/key")
async def get_user_api_key():
    # Check Database if User id exist
    # Depends on session user id

    # If user exist get user APIkey
    userAPIKey = APIKey(
        key="3fa85f64-5740-2262-b3fc-2c963f36afa1",
        user="3fa85f64-5740-2262-b3fc-2c963f36afa1",
    )

    # Send key string
    return userAPIKey


@router.patch("/", response_model=ChangePassword)
async def change_password(
    change_password: ChangePassword
):
    # check old and new password must not be the same
    if change_password.current_password == change_password.new_password:
        raise HTTPException (status_code=404, detail= "Please choose a different password")

    

    # check new and confirm password are the same
    if change_password.new_password != change_password.confirmed_password:
        raise HTTPException (status_code=404, detail= "Confirmed password and new password must match")

    return change_password 
    