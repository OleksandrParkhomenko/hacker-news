from __future__ import absolute_import, unicode_literals
from celery.task import periodic_task
from celery.schedules import crontab

from datetime import timedelta

from . import models

# @periodic_task(
# 	run_every=(timedelta(seconds=5)), 
# 	name="test_task"
# 	)
# def test_task():
# 	print("test task")


@periodic_task(
	run_every=(timedelta(seconds=10)), 
	name="reset_upvotes"
	)
def reset_upvotes():
	posts =models. Post.objects.all()
	posts.update(upvotes_amount=models.Post.upvotes_amount.field.default)
	print("INFO: UPVOTES RESETED")
	

