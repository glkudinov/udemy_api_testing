from utils.http_methods import HttpMethods

"""Методы для тестирования Google maps api"""

base_url = "https://rahulshettyacademy.com"  # Базовая URL
key = "?key=qaclick123"  # Параметр для всех запросов


class GoogleMapsApi:
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post
        post_json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, post_json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"   # Ресурс метода Get
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения локации"""

    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"    # Ресурс метода Put
        put_url = f"{base_url}{put_resource}{key}"
        put_json_for_update_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(put_url)
        result_put = HttpMethods.put(put_url, put_json_for_update_place)
        print(result_put.text)
        return result_put

    """Метод для удаления локации"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"     # Ресурс метода Delete
        delete_url = f"{base_url}{delete_resource}{key}"
        delete_json_for_del_place = {
            "place_id": place_id
        }
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, delete_json_for_del_place)
        print(result_delete.text)
        return result_delete
