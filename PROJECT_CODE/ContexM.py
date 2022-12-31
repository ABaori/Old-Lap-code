"""
These are block of codes which run when a certain code is running and
 perform some action when we enter and exit that block of code.
"""
## A context manager for sqlite 3 block of code

import sqlite3

class DatabaseConnection:
    def __init__(self,host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_tb or exc_val or exc_type:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
# Main reason to do this is it leaves our file in an inconsistent status thus we close first then error pops up
# and do not commit anything.




class CustomFileOpen:
    """Custom context manager for opening files."""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        self.f.close()
#You can use the above class just like a regular context manager.

with CustomFileOpen("file.txt", "wt") as file:
    file.write("contents go here")