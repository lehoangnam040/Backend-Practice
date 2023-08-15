from os.path import dirname, join

from starlette.templating import Jinja2Templates

TEMPLATES = Jinja2Templates(directory=join(dirname(__file__), "templates"))
