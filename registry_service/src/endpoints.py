from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Body, Path, Response
from fastapi.exceptions import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import DBAPIError
from fastapi_cache.decorator import cache
from pydantic import UUID4

from database import get_async_session
from models import entrie
from schemas import EntryModel

