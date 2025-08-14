from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/profiles/')
async def get_profiles(db: Session = Depends(get_db)):
    try:
        return await service.get_profiles(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/profiles/id')
async def get_profiles_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_profiles_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profiles/')
async def post_profiles(raw_data: schemas.PostProfiles, db: Session = Depends(get_db)):
    try:
        return await service.post_profiles(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/profiles/id/')
async def put_profiles_id(id: int, name: Annotated[str, Query(max_length=100)], contact: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_profiles_id(db, id, name, contact)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/profiles/id')
async def delete_profiles_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_profiles_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

