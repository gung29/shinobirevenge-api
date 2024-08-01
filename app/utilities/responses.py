from fastapi.responses import Response

class AMFResponse(Response):
    media_type = "application/x-amf"
