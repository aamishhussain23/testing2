from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    name: str
    email: str

@app.post("/submit/")
async def capture_post_details(request: Request, form_data: FormData):
    # Access form-values (JSON body)
    body = form_data.dict()

    # Access query-string
    query_string = str(request.query_params)

    # Access raw-content (as JSON)
    raw_content = await request.json()

    # Access headers
    headers = request.headers
    host = headers.get('host')
    user_agent = headers.get('user-agent')
    date = headers.get('date')  # Note: 'date' might not be present in headers

    return {
        "host": host,
        "date": date,
        "user-agent": user_agent,
        "query-string": query_string,
        "form-values": body,
        "raw-content": raw_content
    }
