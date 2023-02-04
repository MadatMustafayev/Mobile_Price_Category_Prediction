from typing import Any, List, Optional

from pydantic import BaseModel
from model.processing.validation import MobileDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]


class MultipleMobileDataInputs(BaseModel):
    inputs: List[MobileDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "battery_power": 563,
                        "blue": 1,
                        "clock_speed": 0.5,
                        "dual_sim": 1,
                        "fc": 2,
                        "four_g": 1,
                        "int_memory": 41,
                        "m_dep": 0.9,
                        "mobile_wt": 145,
                        "n_cores": 5,
                        "pc": 8,
                        "px_height": 263,
                        "px_width": 1716,
                        "ram": 2603,
                        "sc_h": 11,
                        "sc_w": 2,
                        "talk_time": 9,
                        "three_g": 1,
                        "touch_screen": 1,
                        "wifi": 1
                    }
                ]
            }
        }