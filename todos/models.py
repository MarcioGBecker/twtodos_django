from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Título",
        max_length=100, null=False, blank=False
    )  # Titulo da tarefa
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )  # Data em que a tarefa foi criada
    deadLine = models.DateField(verbose_name="Data de entrega",
        null=False, blank=False
    )  # Prazo para encerrar a tarefa
    finished_at = models.DateField(null=True)  # Data real de encerramento da tarefa
