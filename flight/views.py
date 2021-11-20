from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer
from rest_framework import viewsets, filters
from .permissions import IsStaffOrReadOnly
from datetime import datetime, date


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStaffOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_filter = ('departureCity', 'arrivalCity', 'dateOfDeparture')

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return super().get_serializer_class()
        return FlightSerializer

    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()
        if self.request.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(dateOfDeparture__gte=today).filter(
                estimatedTimeOfDeparture__gte=current_time)
        return queryset


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    seriaizer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
