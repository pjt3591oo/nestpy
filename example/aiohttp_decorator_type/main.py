from nest import NestFactory
from mung_module import MungModule

app = NestFactory(MungModule).create()
app.start(3000)