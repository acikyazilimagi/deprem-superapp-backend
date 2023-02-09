from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class GetInfo(BaseModel):
    """
    This class is used to create a model for info data.
    """

    il: Optional[str] = ""
    ilce: Optional[str] = ""
    gereksinimler: Optional[List[str]] = []
    notlar: Optional[str] = ""
    baslangic_zaman: Optional[datetime] = ""
    bitis_zaman: Optional[datetime] = ""
    guncel_tarih: Optional[datetime] = ""
