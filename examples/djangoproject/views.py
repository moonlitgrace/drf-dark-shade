from rest_framework.response import Response
from rest_framework.views import APIView

class TestAPIView(APIView):
	def get(self, request):
		data =  {
			"id": 1,
			"username": "admin",
			"email": "admin@admin.com",
			"first_name": "Telegram",
			"last_name": "Admin",
			"is_verified": True,
			"avatar": "http://localhost:8000/media/avatar/341062fc-5621-4f39-bfe8-554659542629.jpg",
			"bio": "Admin of Telegram-re application",
			"last_login": "2023-11-21T05:58:44.255930Z",
			"date_joined": "2023-10-12T11:47:51.395512Z"
		}
		return Response(data)