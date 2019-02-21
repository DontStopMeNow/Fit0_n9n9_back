from .resources import Resources, Memory, Stack, Output
from config import DevConfig
from . import Interpreter

from aiohttp import web


config = DevConfig().config

class InterpreterView(web.View):
    async def post(self):
        try:
            sources = (await self.request.json())['sources']
        except KeyError as e:
            print(e)
            return web.Response(status=400, reason="Need sources")

        memory = Memory(100)
        stack = Stack(100)
        output = Output(100)
        
        resources = Resources(
            stack,
            memory, 
            output
        )
        
        interpreter = Interpreter(resources)

        try:
            interpreter.programm = sources
            result = interpreter.execute()
        except Exception as e:
            return web.Response(status=400, reason=str(e))

        phrase = "".join(result["output"])

        if phrase == config["SECRET"]:
            result["hint"] = f"Твоя подсказка: \"{config['HINT']}\""
        else:
            result["hint"] = "Нужно чтобы программа вывела слово \"cider\". Попробуй ещё раз! =)"


        return web.json_response(result)
