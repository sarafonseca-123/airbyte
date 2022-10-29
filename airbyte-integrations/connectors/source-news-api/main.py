#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_news_api import SourceNewsApi

if __name__ == "__main__":
    source = SourceNewsApi()
    launch(source, sys.argv[1:])
