from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from tasks.models import TodoItem, Category, Priority
from collections import Counter


def count_prio():
    """
    Функция заполняет счетчики Приоритетов
    """
    # Заполняем нулевыми значениями счетчики всех-всех приоритетов
    prio_counters = {prio.pk: 0 for prio in Priority.objects.all()}

    # И только теперь плюсуем в них задействованные задачи
    for task in TodoItem.objects.all():
        prio_counters[task.priority.pk] += 1

    # Сохраняем счетчики
    for pk, new_count in prio_counters.items():
        Priority.objects.filter(pk=pk).update(todos_count=new_count)


def count_cats():
    """
    Функция заполняет счетчики Категорий
    """
    # Заполняем нулевыми значениями счетчики всех-всех категории
    cat_counter = {cat.slug: 0 for cat in Category.objects.all()}

    # И только теперь плюсуем в них задействованные задачи
    for t in TodoItem.objects.all():
        for cat in t.category.all():
            cat_counter[cat.slug] += 1

    # Сохраняем счетчики
    for slug, new_count in cat_counter.items():
        Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_added(sender, instance, action, model, **kwargs):
    """
    Обрабатываем сигнал добавления привязки Категории к Задаче
    """
    if action != "post_add":
        return

    for cat in instance.category.all():
        slug = cat.slug

        new_count = 0
        for task in TodoItem.objects.all():
            new_count += task.category.filter(slug=slug).count()

        Category.objects.filter(slug=slug).update(todos_count=new_count)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_removed(sender, instance, action, model, **kwargs):
    """
    Обрабатываем сигнал удаления привязки Категории к Задаче
    """
    if action != "post_remove":
        return
    count_cats()


@receiver(post_save, sender=TodoItem)
def task_added(sender, instance, **kwargs):
    """
    Обрабатываем сигнал добавления или изменения Задачи
    """
    count_prio()


@receiver(post_delete, sender=TodoItem)
def task_deleted(sender, instance, **kwargs):
    """
    Обрабатываем сигнал удаления Задачи
    """
    count_prio()
    count_cats()
