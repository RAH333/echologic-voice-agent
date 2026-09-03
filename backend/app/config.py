import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Core API configuration variables 
    PROJECT_NAME: str = "EchoLogic AI Backend"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # AssemblyAI Webhook Validation Secret (Optional for validation)
    ASSEMBLYAI_WEBHOOK_SECRET: str = os.getenv("ASSEMBLYAI_WEBHOOK_SECRET", "default_secret_key")
    
    # Environment Tracking
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Load environment variables cleanly from local configurations if available
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")

settings = Settings()
