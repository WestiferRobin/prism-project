"""
- Company: Family
  - Leader: User("Wes Webb", 00000000-0000-0000-0000-000000000000)
  - Vice: Drone("Mr Goose")
  - Director: Drone("John Red")
  - Director: Drone("Mei Blue")
"""
from pydantic import BaseModel

from src.utils.configs.company_config import CompanyConfig


class Company(BaseModel):
    config: CompanyConfig

