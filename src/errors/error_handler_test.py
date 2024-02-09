from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.error_handler import handle_errors


def test_tag_handle_errors_500():
    message = "General Error"
    error = Exception(message)

    response = handle_errors(error)

    assert response.status_code == 500
    assert response.body["errors"][0]["title"] == "Server Error"
    assert response.body["errors"][0]["detail"] == message

def test_tag_handle_errors_422():
    message = "Http Unprocessable Entity Error"
    error = HttpUnprocessableEntityError(message)

    response = handle_errors(error)

    assert response.status_code == 422
    assert response.body["errors"][0]["title"] == "UnprocessableEntity"
    assert response.body["errors"][0]["detail"] == message
