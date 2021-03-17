import httpapiclient
from httpapiclient.mixins import JsonResponseMixin, HelperMethodsMixin


class ApiClient(JsonResponseMixin, HelperMethodsMixin, httpapiclient.BaseApiClient):
    base_url = 'https://www.googleapis.com/youtube/v3/'
