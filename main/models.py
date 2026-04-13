from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    intro = models.TextField(max_length=2000)
    cover = models.ImageField(upload_to='articles/', blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)


    views = models.PositiveIntegerField(default=0)
    read_time = models.DurationField(blank=True, null=True)
    puplished = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug

            counter = 1
            while Article.objects.exclude(id=self.id).filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        if self.important:
            Article.objects.exclude(id=self.id).filter(important=True).update(important=False)

        super().save(*args, **kwargs)

class Context(models.Model):
   text = models.TextField(blank=True, null=True)
   image = models.ImageField(upload_to='context/', blank=True, null=True)
   article = models.ForeignKey(Article, on_delete=models.CASCADE)
   def __str__(self):
        return f" Content of {self.article}"

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Moment(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    photo = models.ImageField(upload_to='moments/')
    author = models.CharField(max_length=100, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug

            counter = 1
            while Moment.objects.exclude(id=self.id).filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)

class Newsletter(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if Newsletter.objects.exclude(id=self.id).filter(email=self.email).exists():
            return
        super().save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    seen= models.BooleanField(default=False)

    def __str__(self):
        return f" {self.name}--{self.message}"


