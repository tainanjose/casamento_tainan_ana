import logging

from ..models import Task
from anaetainan.base.exceptions import BusinessError

logger = logging.getLogger(__name__)


def add_task(new_task: str) -> dict:
    logger.info("SERVICE add new task")
    if not isinstance(new_task, str):
        raise BusinessError("Invalid description")

    if not new_task or not new_task.strip():
        raise BusinessError("Invalid description")

    task = Task(description=new_task)
    task.save()
    logger.info(f"SERVICE task created.")
    return task.to_dict_json()


def list_tasks():
    logger.info("SERVICE list tasks")
    tasks_list = Task.objects.all()
    return [item.to_dict_json() for item in tasks_list]
