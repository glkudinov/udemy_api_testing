from requests import Response


class Checking:
    """Метод для проверки status code"""
    @staticmethod
    def check_status_code(response: Response, status_code ):
        response_status_code = response.status_code
        assert status_code == response_status_code, f"Status code must be {status_code}, now {response_status_code}"
        print(f"Request is OK, status code is {response_status_code}")