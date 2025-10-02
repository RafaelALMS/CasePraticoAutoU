from typing import List, Optional
from xml.etree.ElementTree import tostring
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import processamentoEmail as pe
app = FastAPI()



@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

# Class servem para parsar o email e ajustalo para o prompt
class EmailRequest(BaseModel):
    email_content: str

class EmailAnalysisResponse(BaseModel):
    summary: str
    bulletPoints: List[str]

class APIResponse(BaseModel):
    success: bool
    data: Optional[List[EmailAnalysisResponse]] = None
    error: Optional[str] = None


@app.post("/api/IsUsefulEmail/", response_model=APIResponse)
async def usefulEmail(request: EmailRequest):
    try:
        response = pe.promptResponse(request.email_content)
        
        serialized_response = []
        for item in response:
            serialized_response.append(
                EmailAnalysisResponse(
                    summary=item.summary,
                    bulletPoints=item.bulletPoints
                )
            )
        
        return APIResponse(
            success=True,
            data=serialized_response
        )
        
    except Exception as e:
        return APIResponse(
            success=False,
            error=f"Failed to process email: {str(e)}"
        )



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# This is important for Vercel
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)