from logging import Logger
from typing import Annotated
from http import HTTPStatus

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from schemas import ModelInput, ModelResponse, ModelPrediction

import json
import logging.config

with open('logging_config.json', 'r') as cf:
    logging_config = json.load(cf)

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

logger.info("Starting API Service")

app = FastAPI(title="Sentiment Analysis from text reviews")


@app.get(path="/", response_class=HTMLResponse)
def read_root_html_page():
    logging.info("Reading root page")
    
    html_page = """
    <html>
        <header>
            <title>Sentiment Analysis API</title>
        </header>
        <body>
            <h1>Sentiment Analysis API</h1>
            <p>Make your prediction here:<br></p>
            <form>
                <label for="review_text">Review Text:</label><br>
                <input type="text" id="review_text" name="review_text"><br><br>
                <input type="submit" value="Predict Sentiment">
            </form>

        </body>
    </html>
    """
    
    return html_page


@app.post(
    path="/prediction", 
    status_code=HTTPStatus.OK, 
    response_model=ModelResponse
)
def make_prediction(model_input: Annotated[ModelInput, Form()]):
    logging.info("Making prediction")
    
    result = ModelPrediction(
        input_text=model_input.text,
        value=1,
        category="cat 1",
        description="bla bla"
    )

    logging.info(
        msg="Prediction concluded", 
        extra={"input": model_input.text, "result": result.model_dump_json}
    )
    return result