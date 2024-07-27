from fastapi import APIRouter, Request, Response, Query, Depends, HTTPException
from fastapi.responses import JSONResponse

from . import models, services, schemas


router = APIRouter(
    prefix = '/auth',
    tags = ['Auth']
)


@router.post('/create/user')
async def create_user(
    userdata: schemas.UserSchemas
):
    response = services.UserServices.create_user(userdata)
    if response:
        return JSONResponse(
            status_code = 201,
            content = {
                'detail': 'User created'
            }
        )
    
    else:
        return JSONResponse(
            status_code = 422,
            content = {
                'detail': 'The user has not been created. You entered incorrect data'
            }
        )