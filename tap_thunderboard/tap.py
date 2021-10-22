"""thunderboard tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# Import stream definitions
from tap_thunderboard.streams import (
    thunderboardStream,
    MeasurementsStream,
)
STREAM_TYPES = [
    MeasurementsStream,
]


class Tapthunderboard(Tap):
    """thunderboard tap class."""
    name = "tap-thunderboard"

    # configuration
    config_jsonschema = th.PropertiesList(
        th.Property(
            "mode",
            th.StringType,
            required=True,
            description="dump | file - 'dump' mode scans for devices and dumps measurements continuously."
        ),
        th.Property(
            "dataDirectory",
            th.StringType,
            required=True,
            description="The local directory where thunderboard data can be found"
        ),
        th.Property(
            "filename",
            th.StringType,
            required=True,
            description="The name of the file in the data directory to be processed"
        ),
        th.Property(
            "truncate",
            th.BooleanType,
            required=False,
            description="Optionally cleanup the file contents after processing (Default: True)",
            default=True
        ),
        th.Property(
            "deviceId",
            th.StringType,
            required=False,
            description="An optional device id to limit output from discovered thunderboards"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
    