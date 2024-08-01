from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from ..utilities import amf_utils

router = APIRouter()

@router.post("/decode-amf", response_class=JSONResponse)
async def decode_amf(request: Request):
    try:
        raw_amf_data = await request.body()
        decoded_data = amf_utils.decode_amf_request(raw_amf_data)
        return JSONResponse(content=decoded_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))