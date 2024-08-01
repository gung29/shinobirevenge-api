from typing import Any, List
from pyamf import remoting, AMF0, AMF3

def encode_amf_response(target: str, body: List[Any], use_amf3: bool = True) -> bytes:
    amf_version = AMF3 if use_amf3 else AMF0
    request = remoting.Request(target=target, body=[body])
    envelope = remoting.Envelope(amfVersion=amf_version)
    envelope["/1"] = request
    return remoting.encode(envelope).getvalue()

def decode_amf_request(data: bytes):
    decoded_data = remoting.decode(data).bodies[0][1].body
    return decoded_data
