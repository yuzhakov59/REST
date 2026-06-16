from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    description = models.TextField(verbose_name='описание',blank=True, null=True)
    picture = models.ImageField(upload_to='photo', verbose_name='превью (картинка)', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание',blank=True, null=True)
    picture = models.ImageField(upload_to='photo', verbose_name='превью (картинка)',blank=True, null=True)
    сourse = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='сour')
    video_url = models.URLField(verbose_name='ссылка на видео', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
