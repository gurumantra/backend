from rest_framework import viewsets
from .models import Katha

from .serializer import KathaSerializer


class KathaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Katha.objects.all()
    serializer_class = KathaSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views_count = obj.views_count + 1
        obj.save(update_fields=("views_count", ))
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        # You could also increment the view count if people see the `Notice` in a listing.
        queryset = self.filter_queryset(self.get_queryset())
        for obj in queryset:
            obj.views_count = obj.views_count + 1
            obj.save(update_fields=("views_count", ))
        return super().list(request, *args, **kwargs)

