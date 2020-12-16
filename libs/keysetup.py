# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:   
# https://aws.amazon.com/developers/getting-started/python/

import boto3
import base64
import json
from botocore.exceptions import ClientError
from os import environ as env


def get_sender_addr():

    region_name = "ap-northeast-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='ssm',
        region_name=region_name
    )

    try:
        get_parameter_response = client.get_parameter(
            Name='gmail_sender_addr',
            WithDecryption=True
        )
    except ClientError as e:
        raise e
    else:
        if 'Parameter' in get_parameter_response:
            parameter = get_parameter_response['Parameter']
            keyid = parameter['Value']
            return keyid
        else:
            decoded_binary_keyid = base64.b64decode(get_secret_value_response['Parameter'])
            return decoded_binary_keyid


def get_sender_secret():

    region_name = "ap-northeast-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='ssm',
        region_name=region_name
    )

    try:
        get_parameter_response = client.get_parameter(
            Name='gmail_sender_secret',
            WithDecryption=True
        )
    except ClientError as e:
        raise e
    else:
        if 'Parameter' in get_parameter_response:
            parameter = get_parameter_response['Parameter']
            keyid = parameter['Value']
            return keyid
        else:
            decoded_binary_keyid = base64.b64decode(get_secret_value_response['Parameter'])
            return decoded_binary_keyid


def get_receiver_addr():

    try:
        receiver_addr = env['ReciverAddress']
    except:  # Failed to get ReciverAddress from environment var
        receiver_addr = 'sky@nipapa.tw'
    return receiver_addr


def gen_mail_ini():

    with open('users/mail.ini', 'w+', newline='') as f:
        f.write('[DEFAULT]\n')
        f.write('SenderAddress = {}\n'.format(get_sender_addr()))
        f.write('SenderSecret = {}\n'.format(get_sender_secret()))
        f.write('ReciverAddress = {}\n'.format(get_receiver_addr()))
        f.close()


if __name__ == '__main__':
    gen_mail_ini()
