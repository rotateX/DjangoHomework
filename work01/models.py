from django.db import models
from django.utils.timezone import now
# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name='标签名', max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签名称'
        verbose_name_plural = '标签列表'

# 创建类别模型 Categogy
class Category(models.Model):
    name = models.CharField(verbose_name='类别名称', max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '类别名称'
        verbose_name_plural = '分类列表'

# 创建文章模型 Article
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    title = models.CharField(verbose_name='标题', max_length=100)
    # content = MDTextField(verbose_name='正文', blank=True, null=True)
    content = models.TextField()
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    pub_time = models.DateTimeField(verbose_name='发布时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False, related_name='category_set')
    tag = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)

    def __str__(self):
        return self.title

    # 更新浏览量 view
    def up_view(self):
        self.views += 1
        self.save(update_fields=['views'])
    # 下一篇
    def next_article(self):
        return Article.objects.filter(id__gt=self.id, status='p', pub_time__isnull=False,).order_by('id').first()

    # 上一篇
    def pre_article(self):
        return Article.objects.filter(id__lt=self.id, status='p', pub_time__isnull=False).order_by('-id').first()

    class Meta:
        ordering = ['-pub_time']
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        get_latest_by = 'put_time'
