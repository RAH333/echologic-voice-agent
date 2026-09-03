import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
from app.tools import handle_tool_execution

app = FastAPI(
    title="EchoLogic AI - Tools & Fulfillment Hook",
    description="Fulfillment API endpoint for AssemblyAI Voice Agent Tool Calling"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ToolCallPayload(BaseModel):
    tool_name: str
    arguments: Dict[str, Any]

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "echologic-backend"}

@app.post("/api/webhook/tools", status_code=status.HTTP_200_OK)
async def external_tool_webhook(payload: ToolCallPayload):
    """
    Fulfillment webhook targeted by AssemblyAI's JSON-Schema tool call routing.
    """
    try:
        result = await handle_tool_execution(payload.tool_name, payload.arguments)
        return {"success": True, "data": result}
    except ValueError as val_err:
        raise HTTPException(status_code=400, detail=str(val_err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Internal fulfillment execution error: {str(err)}")

if __name__ == "__main__":
    uvicorn.run("main.py", host="0.0.0.0", port=8000, reload=True)
  
