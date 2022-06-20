from requests import Response
from utils.api import GoogleMapsApi
from utils.checking import Checking

"""Создание, измененеи и удаление локации"""


class TestCreatePlace:
    def test_create_new_place(self):
        print("Метод POST")
        post_result: Response = GoogleMapsApi.create_new_place()
        Checking.check_status_code(post_result, 200)
        check_info = post_result.json()
        place_id = check_info.get("place_id")

        print("Метод GET -> POST")
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(get_result, 200)

        print("Метод PUT")
        put_result: Response = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(put_result, 200)

        print("Метод GET -> PUT")
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(get_result, 200)

        print("Метод DELETE")
        delete_result: Response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(delete_result, 200)

        print("Метод GET -> DELETE")
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(get_result, 404)