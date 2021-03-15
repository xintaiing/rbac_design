from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="用户id")
    name = models.CharField(max_length=32, verbose_name="用户名", default=None, null=True)
    email = models.CharField(max_length=32, verbose_name="邮箱", default=None, null=True)
    is_admin = models.BooleanField(verbose_name="是否是管理员", default=False, null=True)
    status = models.BooleanField(verbose_name="状态", default=True, null=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", default=None, null=True)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "user"


class UserRole(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="用户id")
    user_id = models.IntegerField(verbose_name="用户id", default=None, null=True)
    role_id = models.IntegerField(verbose_name="角色id", default=None, null=True)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "user_roles"


class Role(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="角色id")
    name = models.CharField(max_length=32, verbose_name="角色名", default=None, null=True)
    status = models.BooleanField(verbose_name="状态", default=True, null=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", default=None, null=True)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "role"


class RoleAuth(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.IntegerField(verbose_name="角色id", default=None, null=True)
    auth_id = models.IntegerField(verbose_name="权限id", default=None, null=True)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "role_auths"


class Auth(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="权限id")
    module_name = models.CharField(max_length=32, verbose_name="权限模块名", default=None, null=True)
    title = models.CharField(max_length=32, verbose_name="权限名", default=None, null=True)
    urls = models.CharField(max_length=128, verbose_name="权限路径", default=None, null=True)
    status = models.BooleanField(verbose_name="状态", default=True, null=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", default=None, null=True)
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        db_table = "auth"
