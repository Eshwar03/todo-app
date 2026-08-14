from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import get_db
from typing import Annotated


app=FastAPI()

@app.get("/health")
async def health_check(db:Annotated[AsyncSession,Depends(get_db)]):
    try:
        await db.execute("SELECT 1")
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"detail":"Database unavailable"}
            ) from exc
    return {"status":"healthy"}
