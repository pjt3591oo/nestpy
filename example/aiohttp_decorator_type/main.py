from nest import NestFactory
from app_module import AppModule

app = NestFactory(AppModule).create()
app.start(3000)