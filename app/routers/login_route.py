from fastapi import APIRouter
from ..utilities.responses import AMFResponse
from ..models.login_model import CheckVersion, LoginUser
from ..utilities import amf_utils

router = APIRouter()

@router.post("/check-version", response_class=AMFResponse)
async def check_version(data: CheckVersion):
    body = [data.version]
    response_data = amf_utils.encode_amf_response('SystemLogin.checkVersion', body)
    return AMFResponse(content=response_data)

@router.post("/login-user", response_class=AMFResponse)
async def login_user(data: LoginUser):
    body = [data.username, data.password]
    response_data = amf_utils.encode_amf_response('SystemLogin.loginUser', body)
    return AMFResponse(content=response_data)
