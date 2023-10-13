#setting
from pydantic import BaseModel
from enum import Enum
from cat.mad_hatter.decorators import tool,hook,plugin


class UnitSelect(Enum):
    a: str = 'metric'
    b: str = 'imperial'
    
class WWSettings(BaseModel):
    OpenWeather_api: str = ""
    Temperature_unit: UnitSelect = UnitSelect.b
    city: str = "new york"
    
@plugin
def settings_schema():
    return WWSettings.schema()
