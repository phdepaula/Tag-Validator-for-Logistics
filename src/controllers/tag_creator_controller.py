import os
from typing import Dict

from src.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    """
    Responsability for implementing business rules
    """

    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_from_tag)

        return formatted_response

    def __create_tag(self, product_code: str) -> str:
        tags_directory = os.path.join(os.getcwd(), "tags")
        path_from_tag = os.path.join(tags_directory, product_code)

        if not os.path.exists(tags_directory):
            os.makedirs(tags_directory)

        barcode_handler = BarcodeHandler()
        barcode_handler.create_barcode(path_from_tag)

        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f"{path_from_tag}.png"
            }
        }
