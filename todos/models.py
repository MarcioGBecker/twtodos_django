from django.db import models


class Todo(models.Model):
    title = models.CharField(
        max_length=100, null=False, blank=False
    )  # Titulo da tarefa
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )  # Data em que a tarefa foi criada
    deadLine = models.DateTimeField(
        null=False, blank=False
    )  # Prazo para encerrar a tarefa
    finished_at = models.DateTimeField(null=True)  # Data real de encerramento da tarefa
