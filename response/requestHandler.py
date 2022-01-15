class MockFile():
# takes care of requests that do not have .read function
    def read(self):
        return False

class RequestHandler():
# will take care of handling all kinds of requests
    def __init__(self):
        self.contentType = ""
        self.contents = MockFile()

    def getContents(self):
        return self.contents.read()

    def read(self):
        return self.contents

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def getContentType(self):
        return self.contentType

    def getType(self):
        return 'static'
