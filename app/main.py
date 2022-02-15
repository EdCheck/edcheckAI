import uvicorn
from fastapi import APIRouter, Depends, FastAPI
from starlette.middleware.cors import CORSMiddleware


from pydantic import BaseModel

from celery.result import AsyncResult

####################################################
class spelling_grammar_data:
    text : str
#####################################################

router = APIRouter()

def create_app() -> CORSMiddleware:
    """Create app wrapper to overcome middleware issues."""
    fastapi_app = FastAPI()
    fastapi_app.include_router(router)
    return CORSMiddleware(
        fastapi_app,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app = create_app()


@router.get('/')
async def root():
    return "Welcome to EdCheck Backend API"



from happytransformer import HappyTextToText, TTSettings
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
@router.post('/spelling-grammar/')
async def spelling_grammar(data: spelling_grammar_data):
    args = TTSettings(num_beams=5, min_length=1)
    result = happy_tt.generate_text("grammar: " + data.text, args=args)

    return result.text


