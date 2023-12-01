### SMS Transaction Parser

This repo hosts a [FastAPI](https://fastapi.tiangolo.com/) powered API codebase which accepts SMS messages as an input, auto-detects if a particular message is transactional in nature or not, and then parses out all the transactional meta-data.

The transactional meta-data can then be forwarded to various services for financial processing.

Currently supports: [fireflyIII](https://github.com/firefly-iii/firefly-iii)
