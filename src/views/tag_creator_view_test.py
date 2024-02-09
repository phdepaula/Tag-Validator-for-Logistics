import os
from unittest.mock import patch

from src.drivers.barcode_handler import BarcodeHandler
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


@patch.object(BarcodeHandler, "create_barcode")
def test_validate_and_create(mock_create_barcode):
    tags_directory = os.path.join(os.getcwd(), "tags")
    mock_value = os.path.join(tags_directory, "image_path")
    mock_create_barcode.return_value = mock_value

    mock_request = MockRequest(json={"product_code": "Primeira_tag"})
    req = HttpRequest(body=mock_request.json)

    tag_creator_view = TagCreatorView()
    http_response = tag_creator_view.validate_and_create(req)

    assert http_response.status_code == 200
