"""Stream type classes for tap-thunderboard."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_thunderboard.client import thunderboardStream

class MeasurementsStream(thunderboardStream):
    """Define measurements stream."""
    name = "measurements"
    primary_keys = ["deviceId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "deviceId",
            th.IntegerType,
            description="The ID of the device that collected the measurement"
        ),
        th.Property(
            "when",
            th.DateTimeType,
            description="The instant the measurement was taken"
        ),
        th.Property(
            "uvIndex",
            th.IntegerType,
            description="UV strength index"
        ),
        th.Property("temperature", th.NumberType),
        th.Property("humidity", th.NumberType),
        th.Property("ambientLight", th.NumberType),
    ).to_dict()
