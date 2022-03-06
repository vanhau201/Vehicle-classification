from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
import base64
import numpy as np
# import tensorflow as tf
import uuid
from .serializers import VehicleSerializer
from rest_framework import serializers, status
from django.core.files.base import ContentFile
from .models import Vehicle
import datetime
from io import BytesIO
# Create your views here.

# model = tf.keras.models.load_model("./model_DL/model_xception_2.h5")


@api_view(['GET'])
def OverView(request):
    overView = {
        'predict': '/predict/',
        'history': '/history/'
    }
    return Response(overView)

@api_view(['GET'])
def History(request):
    list_history = Vehicle.objects.all()
    serializer = VehicleSerializer(list_history,many=True,context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def Predict(request):
    # labels = {
    #     0: 'Xe đạp',
    #     1: 'Xe xích lô',
    #     2: 'Xe máy',
    #     3: 'Xe ba gác',
    #     4: 'Xe lam',
    #     5: 'Xe hơi',
    #     6: 'Xe tải',
    #     7: 'Xe khách'
    # }

    # try:
    #     string_base64 = request.data['base64']
    #     # img = base64_to_img(string_base64)
    #     # img = cv2.resize(img, (224, 224))
    #     img = Image.open(BytesIO(base64.b64decode(string_base64)))
    #     img = img.resize((224,224))
    #     img = np.array(img)
    #     img = img.reshape(1, 224, 224, 3)
    #     pre = model.predict(img)
    #     # print(img.shape)
    #     list_percent = np.round(np.round(pre[0], 3)*100, 2)
    #     confidence = np.round(np.max(list_percent),2)
    #     result = labels[np.argmax(pre)]

    #     # Save database
    #     image_data = base64.b64decode(string_base64)
    #     image_name = str(uuid.uuid4())+".jpg"
    #     image_vehicle = ContentFile(image_data, image_name)
    #     # Vehicle(image=image_vehicle, result=result, confidence=confidence,
    #     #         date_created=datetime.datetime.now()).save()

    #     serializer = VehicleSerializer(data={
    #         'image':image_vehicle,
    #         'result':result,
    #         'confidence':confidence,
    #         'date_created':datetime.datetime.now()

    #     })

    #     # if serializer.is_valid():
    #     #     serializer.save()
        
    #     # Reponse
    #     percent = {}
    #     for index, value in enumerate(labels.values()):
    #         percent[value] = list_percent[index]
    #     res = {
    #         'percent': percent,
    #         'result': result
    #     }

    #     return Response(res)
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
     return Response("ok")

    


# Hàm phụ trợ
# def base64_to_img(base64_data):
#     im_bytes = base64.b64decode(base64_data)
#     im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
#     img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
#     return img
