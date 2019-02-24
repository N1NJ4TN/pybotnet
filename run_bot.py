import settings

async def infect():
    while True:
        print('infect')
        await asyncio.sleep(settings.INFECTION_CYCLE_TIME)

async def get_and_schedule_job():
    while True:
        print('getting and scheduling job')
        await asyncio.sleep(settings.GET_JOB_CYCLE_TIME)

class BotRunTime:
    def __init__(self, loop, server):
        self.loop = loop
        self.server = server
        loop.create_task(infect())
        self.run()

    def run(self):
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.server.stop()
            self.loop.close()
