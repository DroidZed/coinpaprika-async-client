from httpx import Response, Request, DecodingError


class ApiException(Exception):
    def __init__(self, response: Response):

        self.status_code: int = response.status_code
        self.response: Response = response
        self.request: Request = response.request

        try:
            json_response = response.json()

        except DecodingError:
            self.message = f"JSON error message from Coinpaprika: {response.text}"

        else:
            self.message = json_response["error"]

    def __str__(self):
        return f"CoinpaprikaAPIException(status_code: {self.status_code}): {self.message}"
