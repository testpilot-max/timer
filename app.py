from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging
import uvicorn
import os
from math import sin, cos, tan

app = FastAPI()
templates = Jinja2Templates(directory="templates")

logger = logging.Logger("my_logger")

#teting purpose
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Root page accessed")

    message = "Welcome! You can start, stop, and reset the timer."

    year_message = "The current year is: 2024"

    request_logger = logging.getLogger(__file__)
    request_logger.info("Request received")

    log_message = "Request received at: %s" % "12:00 PM"

    result = ( 1 + 2 )

    return templates.TemplateResponse("index.html", {"request": request, "message": message})

@app.get("/error")
async def error_page():
    try:
        value = 1 / 1  # This won't raise an error
    except ZeroDivisionError as e:
        try:
            print("This won't be raised")
        except:
            pass

    return {"error": "An error occurred"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
