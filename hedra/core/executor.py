# import asyncio
# from alive_progress import alive_bar
# from easy_logger import Logger
# from .personas import PersonaManager
# from hedra.reporting import Handler, ParallelHandler
# from async_tools.functions import check_event_loop
# from .parsing import ActionsParser
# from .pipelines import Pipeline


# class Executor:

#     def __init__(self, config):
#         self.actions = ActionsParser(config)
#         self.config = config
#         self.has_time_limit = False
#         self.has_action_limit = False
#         self.persona = None
#         self.pipeline = Pipeline(self.config)
#         self._is_parallel = self.config.runner_mode.find('parallel') > -1
#         self._no_run_visuals = self.config.executor_config.get('no_run_visuals', False)

#         if self._is_parallel:
#             self.handler = ParallelHandler(config)
#         else:
#             self.handler = Handler(config)

#         logger = Logger()
#         self.session_logger = logger.generate_logger('hedra')
#         check_event_loop(self.session_logger)

#         try:
#             self._event_loop = asyncio.get_running_loop()

#         except Exception:          
#             self._event_loop = asyncio.get_event_loop()
    
#     def __iter__(self):
#         for event in self.pipeline.results:
#             for result in event.value:
#                 yield result.value

#     async def setup(self, reporter_config=None):

#         if self._is_parallel is False:
#             self.session_logger.info('Initializing reporting...')
#             await self.handler.initialize_reporter()
#             self.session_logger.info('Reporter successfully connected!')

#         await self.actions.parse()

#         persona = PersonaManager(
#             self.config,
#             self.handler
#         )

#         await self.pipeline.initialize(persona, self.actions)
        
#     async def generate_load(self):
        
#         if self._is_parallel is False:
#             self.session_logger.info('Executing load testing...\n')
        
#         await self.pipeline.execute()

#         self._results = self.pipeline.results
#         self._stats = self.pipeline.stats

#     async def calculate_results(self):

#         await self.pipeline.get_results()

#         results = None
#         if self._is_parallel is False:

#             actions_per_second = self.pipeline.stats.get('actions_per_second')
#             completed_actions = self.pipeline.stats.get('completed_actions')
#             total_time = self.pipeline.stats.get('total_time')

#             self.session_logger.info('\n')
#             self.session_logger.info(f'Calculated APS of - {actions_per_second} - actions per second.')
#             self.session_logger.info(f'Total action completed - {completed_actions} over actual runtime of - {total_time} - seconds.')
#             self.session_logger.info('\n')

#             self.session_logger.info(f'Processing - {completed_actions} - action results.')
        
#             with alive_bar(
#                 total=self.pipeline.stats.get('completed_actions'),
#                 title='Processing results...',
#                 bar=None, 
#                 spinner='dots_waves2'
#             ) as bar:
#                 results = await self.handler.aggregate(self.pipeline.results, bar=bar)

#         else:
#             results = await self.handler.aggregate(self.pipeline.results)

#         await self.pipeline.selected_persona.close()

#         return results

#     async def submit_results(self, aggregate_events):
#         await self.handler.merge(aggregate_events)

#         self.session_logger.info('Requesting session summary from reporter...')

#         metrics = await self.handler.get_stats()
#         await self.handler.submit(metrics)
#         self.session_logger.info('Summary generated!')
#         self.session_logger.info('Exiting now. Goodbye!\n')

#     async def get_completed(self):
#         return await self.pipeline.get_completed_count()
