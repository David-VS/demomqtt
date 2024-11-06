from dataclasses import dataclass

@dataclass
class Sensor:
    name:str
    type:str
    value:int