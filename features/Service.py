# Third-party imports...
import requests
import json
import logging

# Standard library imports...
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

TIMEOUT = 45


def requests_retry_session(retries=3,
                           backoff_factor=0.3,
                           status_forcelist=(500, 502, 504),
                           session=None,
                           ):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


class Services(object):
    def _init_(self, context):
        self.context = context
        self.response = None

    def get_response(self, request_url, headers_content=None, params=None, is_dict=False):
        response = None

        try:
            response = requests_retry_session().get(
                url=request_url, headers=headers_content, params=params, timeout=TIMEOUT
            )
        except Exception as x:
            logging.error('It failed :(', x.__class__.__name__)
        finally:
            self.response = response
            return response

    def post_response(self, request_url, headers_content=None, data=None, json_data=None):
        response = None

        try:
            response = requests_retry_session().post(
                url=request_url, headers=headers_content, data=data, json=json_data, timeout=TIMEOUT
            )
        except Exception as x:
            logging.error('It failed :(', x.__class__.__name__)
        finally:
            self.response = response
            return response

    def delete_response(self, request_url, headers_content=None, data=None, json_data=None):
        response = None

        try:
            response = requests_retry_session().delete(
                url=request_url, headers=headers_content, data=data, json=json_data, timeout=TIMEOUT
            )
        except Exception as x:
            logging.error('It failed :(', x.__class__.__name__)
        finally:
            self.response = response
            return response