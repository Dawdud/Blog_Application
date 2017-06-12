from django.conf.urls import url
from first import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^add_category/$', views.add_category, name= 'add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_books/$',views.add_Books, name='add_books'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category, name='show_category'),
    url(r'^book/(?P<id>\d+)/(?P<book_name_slug>[\w\-]+)$',views.show_books, name='show_books'),
    url(r'^about/$', views.about, name= 'about'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view,name='login'),
    url(r'^logout/$', views.logout_view,name='logout'),
    url(r'^password_reset/$',auth_views.password_reset, name='password_reset'),
    url(r'password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm,
        name= 'password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name= 'password_reset_complete'),

]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)