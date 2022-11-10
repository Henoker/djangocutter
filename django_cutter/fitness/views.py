from django.shortcuts import render
from rest_framework import viewsets

from .models import Set, Exercise, Workout
from .serializers import SetSerializer, WorkoutSerializer, ExerciseSerializer

# Create your views here.
class SetviewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

class WorkoutviewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class ExcerciseviewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    

