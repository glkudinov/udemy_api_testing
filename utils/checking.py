import json
from requests import Response


class Checking:
    """Метод для проверки status code"""
    @staticmethod
    def check_status_code(response: Response, status_code ):
        response_status_code = response.status_code
        assert status_code == response_status_code, f"Status code must be {status_code}, now {response_status_code}"
        print(f"Request is OK, status code is {response_status_code}")

    """Метод для проверки наличия всех полей в ответе"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значения поля в ответе"""
    @staticmethod
    def check_json_value(response: Response, field_name: str, expected_value: str):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Значение поля {field_name} не соответствует {expected_value}"
        print(f"Успех. Значение поля {field_name} соответствует {expected_value}")

    """Метод для проверки по слову в ответе"""
    @staticmethod
    def check_word_in_json_value(response: Response, word_in_text: str, field_name: str):
        check = response.json()
        check_info = check.get(field_name)
        assert word_in_text in check_info, f"В ответе {check_info} отсутствует слово {word_in_text}"
        print(f"В ответе {check_info} есть слово {word_in_text}")
