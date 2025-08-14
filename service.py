from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_profiles(db: Session):

    query = db.query(models.Profiles)

    profiles_all = query.all()
    profiles_all = (
        [new_data.to_dict() for new_data in profiles_all]
        if profiles_all
        else profiles_all
    )
    res = {
        "profiles_all": profiles_all,
    }
    return res


async def get_profiles_id(db: Session, id: int):

    query = db.query(models.Profiles)
    query = query.filter(and_(models.Profiles.id == id))

    profiles_one = query.first()

    profiles_one = (
        (
            profiles_one.to_dict()
            if hasattr(profiles_one, "to_dict")
            else vars(profiles_one)
        )
        if profiles_one
        else profiles_one
    )

    res = {
        "profiles_one": profiles_one,
    }
    return res


async def post_profiles(db: Session, raw_data: schemas.PostProfiles):
    id: int = raw_data.id
    name: str = raw_data.name
    contact: str = raw_data.contact

    record_to_be_added = {"id": id, "name": name, "contact": contact}
    new_profiles = models.Profiles(**record_to_be_added)
    db.add(new_profiles)
    db.commit()
    db.refresh(new_profiles)
    profiles_inserted_record = new_profiles.to_dict()

    res = {
        "profiles_inserted_record": profiles_inserted_record,
    }
    return res


async def put_profiles_id(db: Session, id: int, name: str, contact: str):

    query = db.query(models.Profiles)
    query = query.filter(and_(models.Profiles.id == id))
    profiles_edited_record = query.first()

    if profiles_edited_record:
        for key, value in {"id": id, "name": name, "contact": contact}.items():
            setattr(profiles_edited_record, key, value)

        db.commit()
        db.refresh(profiles_edited_record)

        profiles_edited_record = (
            profiles_edited_record.to_dict()
            if hasattr(profiles_edited_record, "to_dict")
            else vars(profiles_edited_record)
        )
    res = {
        "profiles_edited_record": profiles_edited_record,
    }
    return res


async def delete_profiles_id(db: Session, id: int):

    query = db.query(models.Profiles)
    query = query.filter(and_(models.Profiles.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        profiles_deleted = record_to_delete.to_dict()
    else:
        profiles_deleted = record_to_delete
    res = {
        "profiles_deleted": profiles_deleted,
    }
    return res
