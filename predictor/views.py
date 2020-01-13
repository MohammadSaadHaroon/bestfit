from django.shortcuts import render
from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from . models import approvals
from . serializers import approvalsSerializers
from . forms import ApprovalForm
from django.contrib import messages


class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get sound from request
            sound = request.GET.get('sound')


            # predict based on vector
            prediction = PredictorConfig.model.predict([[90,20]])[0]
            # build response
            response = {'ans': prediction}

            # return response
            return get

    def cxcontact(request):

        if request.method == 'POST':
            form = ApprovalForm(request.POST)
            if form.is_valid():

                Obtainmarks = form.cleaned_data['Obtainmarks']
                Time = form.cleaned_data['Time']

                myDict = (request.POST).dict()
                #df = pd.DataFrame(myDict, index=[0])
                prediction = PredictorConfig.model.predict([[Obtainmarks,Time]])[0]

                response = {'ans': prediction}

                messages.success(request, 'Grade of Student: {}'.format(prediction))
        form = ApprovalForm()

        return render(request, 'myform/cxform.html', {'form': form})