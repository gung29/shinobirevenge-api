# Shinobi Revenge API
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)

![Framework](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
### Prerequisites
Ensure you have Python version 3.8+ and pip installed on your system.

### Installation
1. **Clone this repository:**
   ```
   git clone https://github.com/gung29/shinobirevenge-api.git
   cd shinobirevenge-api
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```
   uvicorn app.main:app --reload
   ```

The server will run at `http://127.0.0.1:8000/`.

## API Routes

Below is a table listing the currently available routes in the API:

| Endpoint                    | Method | Description                              | Data Required                      |
|-----------------------------|--------|------------------------------------------|------------------------------------|
| `/login/check-version`      | POST   | Checks the version from the client       | `version`: string                  |
| `/login/login-user`         | POST   | Authenticates user                       | `username`: string, `password`: string |
| `/character/verify-files`   | POST   | Verifies user files                      | `session_key`: string, `talent_hash`: string |
| `/character/get-all-characters` | POST   | Retrieves all available characters       | `account_id`: string, `session_key`: string |
| `/utils/decode-amf`         | POST   | Decodes AMF data into JSON               | Raw AMF data stream                |

## Example Requests and Responses

### Get All Characters
**Request**
```json
{
  "session_key": "xxxxxxxxxxxxxxxxxxxxxxxx",
  "account_id": "xxxxx-xxxxx-xxxxx-xxxxx-xxxxx"
}
```

**Response**
```
raw AMF
```

Then send the raw AMF to the `/utils/decode-amf` route:

**Request**
```
raw AMF from above
```

**Response**
```json
{
  "status": 1,
  "error": 0,
  "account_type": 0,
  "tokens": 100,
  "total_characters": 1,
  "account_data": [{
    "char_id": 0000,
    "character_name": "gung",
    "character_level": 1,
    "character_xp": 0,
    "character_gender": 0,
    "character_rank": 1,
    "character_element_1": 1,
    "character_element_2": 0,
    "character_element_3": 0,
    "character_gold": 2500,
    "character_tp": 0,
    "character_class": "",
    "gender": "male"
  }]
}
```

## Contributions
Contributions are welcome, please fork this repository and submit your pull requests or open an issue for further discussion.

**Game** : https://playshinobirevenge.com/

**Software used to decompile the SWF files** : https://github.com/jindrapetrik/jpexs-decompiler

**Software used to capture game requests and responses** : https://www.charlesproxy.com/

**Discord** : gungg29
