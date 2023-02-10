from datetime import datetime
from typing import Optional, Required

from pydantic import BaseModel, conlist


class SetInfo(BaseModel):
    """
    This class is used to create a model for info data.
    """

    il: Required[str]
    ilce: Required[str]
    adres: Required[str]
    isim: Optional[str] = ""
    gereksinimler: conlist(str, max_items=5) = []
    telefon: Optional[str] = ""
    lat: Required[float]
    lon: Required[float]
    notlar: Optional[str] = ""
    zaman: Required[datetime]
