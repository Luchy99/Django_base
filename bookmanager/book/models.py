from django.db import models

# Create your models here.

"""
1. 我们的模型类需要继承自 models。Mocel
2. 系统会自动帮我们添加一个主键（ID）
3. 字段
    字段名 = models.类型（选项）
    
    字段名 其实就是数据表的字段名 
    字段名不要使用关键字
    
    
    char(M)
    varchar(M)
    这个M 就是选项
"""


class BookInfo(models.Model):
    # 创建字段      字段类型
    name = models.CharField(max_length=10)
    # 重写str方法让admin（用户）显示书籍名字
    def __str__(self):
        return self.name
    # 人物先复制过来，后期讲原理


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
