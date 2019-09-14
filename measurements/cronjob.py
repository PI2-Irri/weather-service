from django_cron import CronJobBase, Schedule

from .utils import DataCollector


class CollectMeasurementCronJob(CronJobBase):
    RUN_EVERY_MINS = 0
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'measurements.cronjob.CollectMeasurementCronJob'

    def do(self):
        data_collector = DataCollector()
        data_collector.collect_minutely_measurements()

class CollectForecastCronJob(CronJobBase):
    RUN_EVERY_MINS = 0
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'measurements.cronjob.CollectForecastCronJob'

    def do(self):
        data_collector = DataCollector()
        data_collector.collect_forecast_measurements()
