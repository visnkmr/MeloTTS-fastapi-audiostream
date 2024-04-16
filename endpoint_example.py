import uvicorn
from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel
from fastapi.responses import FileResponse
from melo.api import TTS
import tempfile
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods
    allow_headers=["*"], # Allow all headers
)
class QueryData(BaseModel):
    text: str
    comments:str
from melo.api import TTS

# Speed is adjustable
speed = 0.8

# CPU is sufficient for real-time inference.
# You can set it manually to 'cpu' or 'cuda' or 'cuda:0' or 'mps'
device = 'auto' # Will automatically use GPU if available

# English 
model = TTS(language='EN_V2', device=device)
# print(model)
speaker_ids = model.hps.data.spk2id

@app.post("/tts")
async def tts(query: QueryData):
    print(query.text)

    # American accent
    # output_path = 'en-us.wav'
    # model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)

    # British accent
    model.tts_to_sound(query.text, speaker_ids['EN-BR'], speed=speed)

    return {"response":"text recieved"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8963)