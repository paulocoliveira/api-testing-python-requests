import requests
import json

def create_booking(context, booking):
    url = context.base_url + "booking/"
    data = booking.__dict__
    header = {'Content-Type': 'application/json'}
    response = requests.post(url, data = json.dumps(data), headers = header)
    return response

def get_all_bookings(context):
    url = context.base_url + "booking/"
    response = requests.get(url)
    return response

def delete_bookings(context):
    url = context.base_url + "booking/"
    response = requests.delete(url)
    return response