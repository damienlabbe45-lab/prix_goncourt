# -*- coding: utf-8 -*-

"""
Classe abstraite générique Dao[T], dont hérite les classes de DAO de chaque entité
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional
from UTILS.CustomAsyncsession import CustomAsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from os import environ
from dotenv import load_dotenv
from UTILS.logs import LogErreur


@dataclass
class Dao[T](ABC, LogErreur):
    load_dotenv()
    connection: sessionmaker[CustomAsyncSession] = sessionmaker(
        bind=create_async_engine(URL.create(drivername="mysql+asyncmy://",
                                            username=environ["USER"],
                                            password=environ["PASSWORD"],
                                            host=environ["IP"],
                                            database=environ["DATABASE"]),
                                 echo=False, poll_pre_ping=True),
        expire_on_commit=False,
        class_=CustomAsyncSession)


