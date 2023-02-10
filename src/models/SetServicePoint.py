from typing import Optional, Required

from pydantic import BaseModel, conlist


class SetServicePoint(BaseModel):
    """
    This class is used to create a model for info data.
    """

    il: Required[str]
    ilce: Required[str]
    adres: Required[str]
    mahalle: Optional[str]
    isim: Optional[str]
    servis: conlist(str, max_items=30)
    telefon: Optional[str]
    lat: Required[float]
    lon: Required[float]
    notlar: Optional[str]
