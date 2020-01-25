from nest import Get, Post, Controller, Response
from aiohttp import web

@Controller('/m')
class MungController2(object):

  def __init__(self):
    pass

  @Get('')
  def my_func_a(self, req):
    return Response('/m get test')

  @Post('')
  def my_func_c(self, req):
    return Response('/m post test')
