from typing import Any, Generator
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apis.main import app
from apis import models
from apis.db import get_db



DATABASE_URL = 'sqlite:///:memory:'

engine = create_engine(DATABASE_URL, connect_args={
  "check_same_thread":False
},
poolclass=StaticPool)

TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


models.Base.metadata.create_all(bind=engine)

def override_get_db():
  db = TestingSessionLocal()
  try:
    yield db

  finally:
    db.close()
 
app.dependency_overrides[get_db] = override_get_db



@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


