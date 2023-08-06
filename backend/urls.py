from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from team import views as team_view
from speakers import views as speakers_view
from episodes import views as episodes_view
from links import views as links_view
from newsletter import views as newsletter_view

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'episodes', episodes_view.EpisodesView, 'episodes')
router.register(r'speakers', speakers_view.SpeakersView, 'speakers')
router.register(r'team', team_view.TeamView, 'team')
router.register(r'podcast_links', links_view.PodcastLinksView, 'podcast_links')
router.register(r'social_media_links', links_view.SocialMediaLinksView, 'social_media_links')
router.register(r'newsletter', newsletter_view.NewsletterView, 'newsletter')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
