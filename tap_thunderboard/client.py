"""Custom client handling, including thunderboardStream base class."""

import json
import requests
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.streams import Stream

def readfile(directory, filename):
    data = None
    if directory and filename:
        datafile = os.path.join(directory, filename)
        f = open(datafile, 'rb')
        data = f.read() 
        f.close()
    return data.decode("utf-8") 


class thunderboardStream(Stream):
    """Stream class for thunderboard streams."""

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects."""
        self.logger.info("---------------------------------------------------")
        self.logger.info(f'The file {self.config.get("dataDirectory", None)}/{self.config.get("filename", None)}')
        
        datafile = os.path.join(self.config.get("dataDirectory"), self.config.get("filename"))
        with open(datafile, 'r+', encoding = "utf-8") as f:
            for l in f.readlines():
                data = json.loads(l)
                # naive filtering of specific devices
                deviceId = self.config.get("deviceId")
                if (not deviceId or deviceId == data['deviceId']):
                    yield data
            if (self.config.get("truncate")):
                f.truncate(0)
