from fastapi import APIRouter
from ..utilities.responses import AMFResponse
from ..models.character_model import User
from ..utilities import amf_utils

router = APIRouter()

@router.post("/verify-files", response_class=AMFResponse)
async def verify_files(data: User):
    body = [data.session_key, data.talent_hash]
    response_data = amf_utils.encode_amf_response('AC.verifyFiles', body)
    return AMFResponse(content=response_data)

@router.post("/get-all-characters", response_class=AMFResponse)
async def get_all_characters(data: User):
    body = [data.account_id, data.session_key]
    response_data = amf_utils.encode_amf_response('SystemLogin.getAllCharacters', body)
    return AMFResponse(content=response_data)

