
class TaskManager:
    def __init__(self):
        self.task_queue = []

    def assign_task(self, unit_id, task):
        self.task_queue.append((unit_id, task))

    def get_tasks_for_unit(self, unit_id):
        return [task for uid, task in self.task_queue if uid == unit_id]

