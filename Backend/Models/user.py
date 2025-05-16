from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel):
    name: str
    address: str
    qualification: str
    interested_fields_require: List[str]
    interested_fields_seek: List[str]
    current_employed_facility: str
    experience: Optional[str] = None
    contact_info: str
    email: Optional[EmailStr] = None
    prev_works: Optional[List[str]] = None
    role: str  # "requirement", "seeker", or "investor"
    investment_required: Optional[bool] = False
    investment_amount: Optional[float] = None