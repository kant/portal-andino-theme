#!coding=utf-8
import getpass

from crontab import CronTab


def search_for_cron_jobs_and_remove(comment_to_search_for):
    # Buscamos y eliminamos los cron jobs que contengan el comment especificado por parámetro
    if comment_to_search_for:
        cron = CronTab(get_current_terminal_username())
        jobs_with_specified_comment = cron.find_comment(comment_to_search_for)
        cron.remove(jobs_with_specified_comment)
        cron.write()


def create_or_update_cron_job(command, hour, minute, comment=''):
    if comment:
        search_for_cron_jobs_and_remove(comment)
    cron = CronTab(get_current_terminal_username())
    job = cron.new(command=command, comment=comment)
    job.hour.on(hour)
    job.minute.on(minute)
    cron.write()


def get_current_terminal_username():
    return getpass.getuser()
