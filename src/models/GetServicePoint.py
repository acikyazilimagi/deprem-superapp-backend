from typing import List, Optional

from pydantic import BaseModel


class GetServicePoint(BaseModel):
    """
    This class is used to create a model for info data.
    """

    il: Optional[str] = ""
    ilce: Optional[str] = ""
    servis: Optional[List[str]] = []
    notlar: Optional[str] = ""
