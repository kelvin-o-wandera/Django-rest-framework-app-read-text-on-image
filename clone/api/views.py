import json
import base64
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, response, status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

api_url = "https://vision.googleapis.com/v1/images:annotate?key={}".format(settings.API_KEY)


class Index(APIView):
    # permission_classes = [IsAuthenticated]
    # pagination_class = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Index, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        json_data = request.data

        try:
            encoded_string = base64.encodebytes(json_data['image'].read()).decode("utf-8")
            json_object = {
                "requests": [
                    {
                        "image": {
                            "content": encoded_string
                        },
                        "features": [
                            {
                                "type": "TEXT_DETECTION"
                            }
                        ]
                    }
                ]
            }
            headers = {"Content-Type": "application/json"}

            feedback = requests.post(api_url, json=json_object, headers=headers)

            json_response = json.loads(feedback.text)

            return response.Response({"message": json_response['responses'][0]['textAnnotations'][0]['description']}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:  # Http404:
            print(e)
            return response.Response({"message": "Invalid code"}, status=status.HTTP_202_ACCEPTED)


