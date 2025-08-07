from fastapi import APIRouter


router = APIRouter(prefix="/users")


@router.get("")
async def endpoint():
    return {"message": "Hello World"}
