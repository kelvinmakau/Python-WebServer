from response.requestHandler import RequestHandler

class TemplateHandler():
    def __init__(self):
        super().__init__()
        self.contentType = 'text/html'

    def find(self, routeData):
    # allows template to find the specific file and set the contents so we can get them from the server
        try:
            template_file = open('templates/{}'.format(routeData['template']))
            self.contents = template_file
            self.setStatus(200)
            return True

        except:
            self.setStatus(404)
            return False