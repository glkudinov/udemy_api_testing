import json
import allure
from requests import Response
from utils.api import GoogleMapsApi
from utils.checking import Checking

"""Создание, изменение и удаление локации"""


@allure.epic("Test create place")
class TestCreatePlace:
    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Метод POST")
        post_result: Response = GoogleMapsApi.create_new_place()
        Checking.check_status_code(post_result, 200)
        check_info = post_result.json()
        place_id = check_info.get("place_id")
        Checking.check_json_token(post_result, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(post_result, "status", "OK")
        Checking.check_json_value(post_result, "scope", "APP")

        print("Метод GET -> POST")
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_value(get_result, "address", "29, side layout, cohen 09")

        print("Метод PUT")
        put_result: Response = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(put_result, 200)
        Checking.check_json_token(put_result, ['msg'])
        Checking.check_json_value(put_result, "msg", "Address successfully updated")

        print("Метод GET -> PUT")
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_value(get_result, "address", "100 Lenina street, RU")

        print("Метод DELETE")
        delete_result: Response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_json_token(delete_result, ['status'])
        Checking.check_json_value(delete_result, "status", "OK")

        print("Метод GET -> DELETE")
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(get_result, 404)
        Checking.check_json_token(get_result, ['msg'])
        Checking.check_word_in_json_value(get_result, "failed", "msg")

        print("Тестирование создания, изменения и удаления локации завершено успешно")
