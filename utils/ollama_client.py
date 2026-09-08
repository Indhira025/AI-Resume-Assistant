import ollama

from config.settings import MODEL_NAME
from config.logging_config import setup_logger

logger = setup_logger()


def ask_ai(prompt: str):

    logger.info("Sending prompt to Ollama...")

    response = ollama.chat(

        model=MODEL_NAME,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        options={
            "temperature": 0,
            "num_predict": 1200
        }

    )

    logger.info("Response received.")

    return response["message"]["content"]