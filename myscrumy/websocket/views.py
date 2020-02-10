from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from websocket.models import Connection, ChatMessage
import boto3
from django.core.serializers import serialize
# Create your views here.

@csrf_exempt
def test(request):
    return JsonResponse({'message':'hello Daud'}, status=200)


def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']

    the_id = Connection.objects.create(connection_id = connection_id)
    the_id.save()
    return JsonResponse({'message':'connect successfully'}, status=200)

@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']

    the_id = Connection.objects.get(connection_id = connection_id)
    the_id.delete()
    return JsonResponse({'message': 'disconnect successfully'}, status=200)


def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client('apigatewaymanagementapi', endpoint_url = 'https://667kkhuds9.execute-api.us-east-2.amazonaws.com/test/',  region_name =  'us-east-2', aws_access_key_id = 'AKIAIV2WKEVGM7MG5IJA', aws_secret_access_key = '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')
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data = json.dumps(data).encode('utf-8'))

@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    print(body)

    instance = ChatMessage()
    print(body['body']['message'])
    instance.message = body['body']['message']
    instance.username = body['body']['username']
    instance.timestamp = body['body']['timestamp']

    instance.save()

    data = {"messages":[body]}
    connections = Connection.objects.all()
    for connect in connections:
        _send_to_connection(connect.connection_id, data)


    return JsonResponse({"message":"sent successfully"}, status=200)


@csrf_exempt
def get_recentmessages(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']

    for chat in ChatMessage.objects.all():
        the_data = {"message":[{"username":chat.username, "message":chat.message, "timestamp":chat.timestamp}]}
        #data = json.dumps(the_data)
        print(the_data)
        _send_to_connection(connection_id, the_data)
