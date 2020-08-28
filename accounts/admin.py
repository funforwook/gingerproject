from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


# 로또 프로젝트에서 썼던 방식으로 유저 밑에 프로필 을 붙여서 보여주려고 이를 상속받음
class ProfileInline(admin.StackedInline):
    model = Profile
    # 프로필을 아예 없앨 수 없게 하는 속성(한번 만들면 지우는건 이상하니까)
    con_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Register your models here.
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

