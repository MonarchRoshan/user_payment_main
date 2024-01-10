from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CardInformationSerializer
from .models import AppointmentPayment  # Import the Payment model
import stripe

class PaymentAPI(APIView):
    serializer_class = CardInformationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        response = {}
        if serializer.is_valid():
            data_dict = serializer.data
            stripe.api_key = 'sk_test_51OHC65IU8XyoXl3K1K8IYcpImnBySuUxdGXIqVb21M4Yku9ZnVhanTQqzLczHfZ7XaLuPH2e2L5JskFW4AAq6UWO00QHVQzqdp'

            try:
                # Save payment information to the database
                # #payment = Payment.objects.create(
                #     card_number=data_dict['card_number'],
                #     #expiry_month=data_dict['expiry_month'],
                #     #expiry_year=data_dict['expiry_year'],
                #     cvc=data_dict['cvc'],
                #     amount=data_dict['amount'],
                #     currency=data_dict['currency']
                # #)

                # Your existing Stripe payment processing logic goes here...

                # Example response structure (modify based on your requirements)
                response = {
                    'message': "Card Payment Success",
                    'status': status.HTTP_200_OK,
                   # 'payment_id': payment.id,  # Sending back the payment ID as an example
                    'details': {
                        "card_number": data_dict['card_number'],
                        "amount": data_dict['amount'],
                        "currency": data_dict['currency']
                    }
                }
            except Exception as e:
                response = {
                    'message': "Card Payment Failed",
                    'status': status.HTTP_400_BAD_REQUEST,
                    'error': str(e)
                }
        else:
            response = {
                'errors': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
            }
        return Response(response)
