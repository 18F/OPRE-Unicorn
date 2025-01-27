import pytest

from models import CANHistory, CANHistoryType
from ops.services.can_history import CANHistoryService

# from sqlalchemy import select


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history(loaded_db):
    test_can_id = 500
    count = loaded_db.query(CANHistory).where(CANHistory.can_id == test_can_id).count()
    can_history_service = CANHistoryService()
    # Set a limit higher than our test data so we can get all results
    response = can_history_service.get(test_can_id, 1000, 0)
    assert len(response) == count


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_custom_length(loaded_db):
    test_can_id = 500
    test_limit = 5
    can_history_service = CANHistoryService()
    # Set a limit higher than our test data so we can get all results
    response = can_history_service.get(test_can_id, test_limit, 0)
    assert len(response) == test_limit


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_custom_offset(loaded_db):
    test_can_id = 500
    can_history_service = CANHistoryService()
    # Set a limit higher than our test data so we can get all results
    response = can_history_service.get(test_can_id, 5, 1)
    offset_first_CAN = response[0]
    offset_second_CAN = response[1]
    # The CAN with ID 500 has ops events with id 1, then starting at ops event id 18 and moving forward
    # Therefore, we expect the ops_event_id to be 18 for the first item in the list offset by 1
    assert offset_first_CAN.ops_event_id == 18
    assert offset_first_CAN.history_type == CANHistoryType.CAN_NICKNAME_EDITED
    assert offset_second_CAN.ops_event_id == 19
    assert offset_second_CAN.history_type == CANHistoryType.CAN_DESCRIPTION_EDITED


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_nonexistent_can():
    test_can_id = 300
    can_history_service = CANHistoryService()
    # Try to get a non-existent CAN and return an empty result instead of throwing any errors.
    response = can_history_service.get(test_can_id, 10, 0)
    assert len(response) == 0


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_list_from_api(auth_client, mocker):
    test_can_id = 500
    mock_can_history_list = []
    for x in range(1, 11):
        # These should be CanHistoryItem objects and not JSON objects ******
        mock_can_history_list.append(
            CANHistory(
                can_id=500,
                ops_event_id=x,
                history_title="CAN Imported!",
                history_message="CAN Imported by Reed on Wednesdsay January 1st",
                timestamp="2025-01-01T00:07:00.000000Z",
                history_type=CANHistoryType.CAN_DATA_IMPORT,
            )
        )

    mocker_get_can_history = mocker.patch("ops_api.ops.services.can_history.CANHistoryService.get")
    mocker_get_can_history.return_value = mock_can_history_list

    response = auth_client.get(f"/api/v1/can-history/?can_id={test_can_id}")
    assert response.status_code == 200
    assert len(response.json) == 10


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_list_from_api_with_params(auth_client, mocker):
    test_can_id = 500
    mock_can_history_list = []
    for x in range(1, 6):
        # These should be CanHistoryItem objects and not JSON objects ******
        mock_can_history_list.append(
            CANHistory(
                can_id=500,
                ops_event_id=x,
                history_title="CAN Imported!",
                history_message="CAN Imported by Reed on Wednesdsay January 1st",
                timestamp="2025-01-01T00:07:00.000000Z",
                history_type=CANHistoryType.CAN_DATA_IMPORT,
            )
        )

    mocker_get_can_history = mocker.patch("ops_api.ops.services.can_history.CANHistoryService.get")
    mocker_get_can_history.return_value = mock_can_history_list

    response = auth_client.get(f"/api/v1/can-history/?can_id={test_can_id}&limit=5&offset=1")
    assert response.status_code == 200
    assert len(response.json) == 5


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_list_from_api_with_bad_limit(auth_client):
    test_can_id = 500
    response = auth_client.get(f"/api/v1/can-history/?can_id={test_can_id}&limit=0")
    assert response.status_code == 400


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_list_from_api_with_bad_offset(auth_client):
    test_can_id = 500
    response = auth_client.get(f"/api/v1/can-history/?can_id={test_can_id}&offset=-1")
    assert response.status_code == 400


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_list_from_api_with_no_can_id(auth_client):
    response = auth_client.get("/api/v1/can-history/")
    assert response.status_code == 400


@pytest.mark.usefixtures("app_ctx")
def test_get_can_history_list_from_api_with_nonexistent_can(auth_client, mocker):
    test_can_id = 400
    mock_can_history_list = []
    mocker_get_can_history = mocker.patch("ops_api.ops.services.can_history.CANHistoryService.get")
    mocker_get_can_history.return_value = mock_can_history_list

    response = auth_client.get(f"/api/v1/can-history/?can_id={test_can_id}&limit=5&offset=1")
    assert response.status_code == 200
    assert len(response.json) == 0
