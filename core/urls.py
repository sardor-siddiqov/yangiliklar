
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from main.models import Newsletter
from main.views import HomeView, NewsletterCreate, ArticleDetailsView, CommentCreateView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    path('articles/<slug:slug>', ArticleDetailsView.as_view(), name='article_details'),

    path('newsletter/', NewsletterCreate.as_view(), name='newsletter'),

    path('comment_create/<slug:slug>', CommentCreateView.as_view(), name='comment_create'),

    path('contact-us/', ContactView.as_view(), name='contact_us'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
