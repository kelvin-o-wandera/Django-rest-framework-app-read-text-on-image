from rest_framework.views import APIView
from rest_framework.reverse import reverse as api_reverse
from rest_framework.response import Response


class APIHomeView(APIView):
    def get(self, request):
        data = {
            "Detect Text From Image": {
                "detect_text_from_image": api_reverse("clone:api_create", request=request),
            },
        }
        return Response(data)
