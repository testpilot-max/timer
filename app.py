from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging
import uvicorn
import os
from math import sin, cos, tan
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Root page accessed")
    message = "Welcome! You can start, stop, and reset the timer."
    year_message = f"The current year is: {datetime.now().year}"
    log_message = f"Request received at: {datetime.now().strftime('%I:%M %p')}"
    logger.info(log_message)
    result = (1 + 2)
    return templates.TemplateResponse("index.html", {"request": request, "message": message, "year_message": year_message})

@app.get("/error")
async def error_page():
    try:
        value = 1 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        logger.error(f"An error occurred: {str(e)}")
        return {"error": "An error occurred", "details": str(e)}

@app.get('/test')
async def test_route( ):
    """This is a test route that intentionally violates PEP 8 rules"""
    x=5
    y= 10
    z =   15
    CONSTANT = 'This should be all caps'
    class badlyNamedClass:
        pass
    def Badly_Named_Function( args ):
        return None
    longVariableName = 'This variable name is quite long and violates PEP 8 guidelines for maximum line length, which is typically 79 characters for code.'
    
    return {'message':"This is a test route",
        'timestamp':datetime.now().isoformat(),
        'random_calculation':sin(.5)+cos(.3)-tan(.1),
        'environment':os.environ.get('FASTAPI_ENV','development'),
        'violations':[x,y,z,CONSTANT,badlyNamedClass,Badly_Named_Function,longVariableName]

            
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
