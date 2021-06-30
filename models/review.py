#!/usr/bin/python3
"""Review Public Cass"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class to create Review objects"""
    place_id = ""
    user_id = ""
    text = ""
