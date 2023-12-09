#!/usr/bin/python3

"""load general storage """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
