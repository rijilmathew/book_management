from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer,UserProfileSerilaizer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework import generics
from .models import UserProfile,CustomUser


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can log out

    def post(self, request):
        try:
            # Extract the refresh token from the request data
            refresh_token = request.data['refresh']
            print(refresh_token)
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                
            # Return a success response
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:

            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class UserprofileView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerilaizer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]



    def custom_method(self, user_id):
        # Retrieve the CustomUser instance using the user ID
        user = CustomUser.objects.get(pk=user_id)
        
        # Print the details of the CustomUser instance
        print("Details of CustomUser with PK {}: {}".format(user_id, user))

    def perform_create(self, serializer):
        # Get the user ID from the request data
        user_id = self.request.data.get('user')
        
        # Call the custom method with the user ID
        self.custom_method(user_id)
        
        # Continue with regular perform_create logic
        serializer.save(user_id=user_id)  # Pass the user ID to the serializer


class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerilaizer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]


