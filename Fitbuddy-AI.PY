import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "FitBuddy AI")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./fitbuddy.db"
    )

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    GEMINI_WORKOUT_MODEL = os.getenv(
        "GEMINI_WORKOUT_MODEL",
        "gemini-1.5-pro"
    )

    GEMINI_TIP_MODEL = os.getenv(
        "GEMINI_TIP_MODEL",
        "gemini-1.5-flash"
    )

    ADMIN_TOKEN = os.getenv(
        "ADMIN_TOKEN",
        "fitbuddy-admin"
    )


settings = Settings()