from pydantic import BaseModel
from sympy import Eq

"""
Notes: Design for Equation and Expression.

Idea:
- We need to use sympy for performance and time
- Expression just means algerbra

"""
class Expression(BaseModel):
    value: str
