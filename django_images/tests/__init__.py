from django.conf import settings


settings.IMAGES_BACKEND = 'django_images.tests.backend.DummyBackend'
