from django.db import models
from datetime import date

# Create your models here.

class Category(models.Model):
    """Категории"""

    name = models.CharField(max_length=100, verbose_name="Описание")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(max_length=110, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актеры и режиссеры"""

    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.PositiveSmallIntegerField(default=0, verbose_name="Возраст")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="actors/", verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"

class Genre(models.Model):
    """Жанры"""

    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(max_length=110, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    """Фильм"""

    title = models.CharField(max_length=100, verbose_name="Название")
    tagline = models.CharField(max_length=100, default='', verbose_name="Слоган")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="movies/", verbose_name="Постер")
    year = models.PositiveSmallIntegerField(default=2019, verbose_name="Дата выхода")
    country = models.CharField(max_length=30, verbose_name="Страна")
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField(default=date.today, verbose_name="Примьера в мире")
    budget = models.PositiveIntegerField(
                                         default=0,
                                         verbose_name="Бюджет",
                                         help_text="указывать сумму в долларах"
                                         )
    fees_in_usa = models.PositiveIntegerField(
                                              default=0,
                                              verbose_name="Сборы в США",
                                              help_text="указывать сумму в долларах"
                                             )
    fess_in_world = models.PositiveIntegerField(
                                                default=0,
                                                verbose_name="Сборы в мире",
                                                help_text="указывать сумму в долларах"
                                                )
    category = models.ForeignKey(
                                Category,
                                verbose_name="Категория",
                                on_delete=models.SET_NULL,
                                null=True
                                )
    slug = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(default=False, verbose_name="Черновик")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class MovieShots(models.Model):
    """Кадры из фильма"""

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="movie_shots/", verbose_name="Изображение")
    movie = models.ForeignKey(
                              Movie,
                              on_delete=models.CASCADE,
                              verbose_name="Фильм"
                              )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    """Звезда рейтинга"""

    value = models.SmallIntegerField(default=0, verbose_name="Значение")

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""

    ip = models.CharField(max_length=15, verbose_name="IP адрес")
    star = models.ForeignKey(
                              RatingStar,
                              on_delete=models.CASCADE,
                              verbose_name="звезда"
                              )
    movie = models.ForeignKey(
                              Movie,
                              on_delete=models.CASCADE,
                              verbose_name="фильм",
                              related_name="ratings"
                              )

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""

    email = models.EmailField()
    name = models.CharField(max_length=100, verbose_name="Имя")
    text = models.TextField(max_length=5000, verbose_name="Сообщение")
    parent = models.ForeignKey(
                                'self',
                                on_delete=models.SET_NULL,
                                verbose_name="Родитель",
                                blank=True,
                                null=True
                              )
    movie = models.ForeignKey(
                              Movie,
                              on_delete=models.CASCADE,
                              verbose_name="фильм"
                              )

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


