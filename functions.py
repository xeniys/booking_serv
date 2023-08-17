import requests

import data
import url


def create_booking(body):
    req = requests.post(url.URL + url.CREATE_BOOKING, json=body)
    return req


def change_booking_body(field, name):
    new_booking_body = data.booking_body.copy()
    new_booking_body[field] = name
    return new_booking_body


def create_token():
    token = requests.post(url.URL + url.AUTH, json=data.auth_body).json()["token"]
    return token


def delete_booking(id_booking):
    headers = data.header.copy()
    headers["Cookie"] = "token=" + create_token()
    req = requests.delete(url.URL + url.DELETE_BOOKING + str(id_booking), headers=headers)
    return req
