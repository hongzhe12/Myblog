# 引入path
from django.urls import path
from django.contrib import admin

from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    path('admin/', admin.site.urls),
    # 文章列表
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    # 点赞 +1
    path('increase-likes/<int:id>/', views.IncreaseLikesView.as_view(), name='increase_likes'),
]
