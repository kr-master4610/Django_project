from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Book name",
        help_text="You must provide specific name of book"
    )
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    discounted_price = models.FloatField(null=True)
    published_date = models.DateField()

    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

gender_choices = [
    ('m', 'Male'),
    ('f', 'Female'),
    ('na', 'N/A'),
]

class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    pseudonym = models.CharField(max_length=20)
    bio = models.TextField(null=True)
    gender = models.CharField(max_length=4, choices=gender_choices, default='na')
    email = models.EmailField(max_length=75, null=True)
    website = models.URLField(null=True)
    age = models.PositiveSmallIntegerField(null=True)
    followers_count = models.PositiveIntegerField(null=True)
    posts_count = models.PositiveIntegerField(null=True)
    comments_count = models.PositiveIntegerField(null=True)
    reputation_score = models.DecimalField(null=True, max_digits=3, decimal_places=2)
    monetisation_income = models.FloatField(null=True)

class Post(models.Model):
    title = models.CharField(max_length=200, unique_for_month='created_at')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reading_time = models.DurationField(null=True)
    posted_at = models.DateTimeField(default=timezone.now)


# МОДЕЛИ ДЛЯ ДОМАШНЕГО ЗАДАНИЯ (Домашнее задание 9)


STATUS_CHOICES = [
    ('new', 'New'),
    ('in_progress', 'In progress'),
    ('pending', 'Pending'),
    ('blocked', 'Blocked'),
    ('done', 'Done'),
]

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Task(models.Model):
    title = models.CharField(max_length=200, unique=True, unique_for_date='created_at')
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class SubTask(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'