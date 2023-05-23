from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )

    def __str__(self):
        return f'{self.text[:100]}...' if len(self.text) > 100 else self.text

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        related_query_name='comment')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.text[:50]} ({self.created.strftime("%d.%m.%Y %H:%M")})'

    class Meta:
        verbose_name = 'коммент'
        verbose_name_plural = 'комменты'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following_users"
    )

    def __str__(self):
        return f'{self.user.username} follows {self.following.username}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='follow'
            )
        ]
