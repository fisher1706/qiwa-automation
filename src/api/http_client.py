from json import JSONDecodeError
from json import dumps as json_dumps
from urllib.parse import urlparse

import allure
import requests
from requests import Response
from requests.adapters import HTTPAdapter


class ReportedRequest(requests.Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hooks = {"response": self.attach_json}

    def attach_json(self, rsp: Response, *args, **kwargs):  # pylint: disable=unused-argument
        url = urlparse(self.url)
        step_name = (
            f"[{rsp.status_code}] {self.method} {url.path}{'?' + url.query if url.query else ''}"
        )
        with allure.step(step_name):
            # If the request content exists, attach it to the Allure report as a JSON attachment
            request_body = (
                self.json or self.data
            )  # TODO: parse data to json or update usage to json
            if request_body:
                allure.attach(
                    json_dumps(request_body, indent=2, ensure_ascii=False).encode("utf8").decode(),
                    "JSON Request body",
                    allure.attachment_type.JSON,
                )
            # If the response content exists, attach it to the Allure report as a JSON attachment
            if rsp.content:
                try:
                    body = (
                        json_dumps(rsp.json(), indent=2, ensure_ascii=False)
                        .encode("utf8")
                        .decode()
                    )
                except JSONDecodeError:
                    body = rsp.text
                allure.attach(
                    body,
                    "JSON Response body",
                    allure.attachment_type.JSON,
                )


class HTTPClient:
    def __init__(self):
        self.session = requests.session()
        self.session.mount("https://", HTTPAdapter(max_retries=10))

    def __request(
        self, method: str, host: str, endpoint: str, allow_redirects: bool = False, **kwargs
    ) -> Response:
        # Create an HTTP request with the given method, host, endpoint, and any additional arguments
        request = ReportedRequest(
            method,
            url=host + endpoint,
            **kwargs,
        )
        # Prepare the request for sending and attach the request method and URL to the Allure report
        prepared = self.session.prepare_request(request)
        # Send the prepared request using the current session and store the response
        return self.session.send(prepared, timeout=16, allow_redirects=allow_redirects)

    def get(self, url, endpoint="", **kwargs) -> Response:
        return self.__request(
            "GET",
            host=url,
            endpoint=endpoint,
            **kwargs,
        )

    def post(self, url, endpoint="", json=None, **kwargs) -> Response:
        return self.__request(
            "POST",
            host=url,
            endpoint=endpoint,
            json=json,
            **kwargs,
        )

    def delete(self, url, endpoint="", **kwargs) -> Response:
        return self.__request("DELETE", host=url, endpoint=endpoint, **kwargs)

    def patch(self, url, endpoint="", json=None, **kwargs) -> Response:
        return self.__request("PATCH", host=url, endpoint=endpoint, json=json, **kwargs)

    def put(self, url, endpoint="", json=None, **kwargs) -> Response:
        return self.__request("PUT", host=url, endpoint=endpoint, json=json, **kwargs)
