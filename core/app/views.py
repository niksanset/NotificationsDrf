from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


class NotificationView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id
            notifications = get_notifications_for_user(user_id)

            data_to_sign = "Данные для подписи"
            signature = sign_data(data_to_sign)

            context = {
                'notifications': notifications,
                'signature': signature,
                'message': 'Уведомления успешно загружены.'
            }

            return render(request, 'app/index.html', context)
        else:
            return Response({'error': 'Пользователь не авторизован'}, status=status.HTTP_401_UNAUTHORIZED)
        
def get_notifications_for_user(user_id):
        notifications = 'Вам пришло уведомление!'
        
        return notifications
    
def sign_data(data):
        return 'Данные подписаны'



