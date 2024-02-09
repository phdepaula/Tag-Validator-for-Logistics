import os

from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tags_directory = os.path.join(os.getcwd(), "tags")

        if not os.path.exists(tags_directory):
            os.makedirs(tags_directory)

        path_from_tag = os.path.join(tags_directory, product_code)

        tag = Code128(product_code, writer=ImageWriter())
        tag.save(path_from_tag)

        return path_from_tag
