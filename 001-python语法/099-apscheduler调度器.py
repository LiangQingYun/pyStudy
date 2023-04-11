
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


# 定义一个任务
def do_something():
    print("执行任务...")


# 创建一个调度器
scheduler = BlockingScheduler()

# 添加定时任务，使用cron表达式  分钟、小时、月份、月份、星期     时区
trigger = CronTrigger.from_crontab('00 12 * * *')  # 每天中午12点执行任务
scheduler.add_job(do_something, trigger)

# 启动调度器
scheduler.start()
