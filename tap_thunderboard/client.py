"""Custom client handling, including thunderboardStream base class."""

import json
import requests
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.streams import Stream
import tap_thunderboard.scan as scan 

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
        if self.config.get("mode") == 'dump':
            self.logger.info(f'DUMP mode - scanning for devices and dumping.')
            scan.run()
        elif self.config.get("mode") == 'file':
            self.logger.info(f'FILE mode - processing file {self.config.get("dataDirectory", None)}/{self.config.get("filename", None)}')
            
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
        else:
            self.logger.error(f'Invalid mode - must be \'dump\' or \'file\'')
