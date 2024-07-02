import pytest
from api.usecase.change_room_status import change_room_status, RoomStatusError
from api.model.room import Room

@pytest.fixture
def mock_room_free():
    return Room(
        room_number='100',
        daily_rate=100,
        status="Free"
    )

@pytest.fixture
def mock_room_occupied():
    return Room(
        room_number='101',
        daily_rate=120,
        status="Occupied"
    )

@pytest.fixture
def mock_room_dirty():
    return Room(
        room_number='102',
        daily_rate=90,
        status="Dirty"
    )

def test_change_room_status_from_free_to_dirty(mock_room_free):
    updated_status = 'Dirty'
    updated_mock_room = change_room_status(mock_room_free, {'status': updated_status})

    assert isinstance(updated_mock_room, Room)
    assert updated_mock_room.status == updated_status, (
        f"Expected status {updated_status}, "
        f"but got {updated_mock_room.status}"
    )

def test_change_room_status_from_free_to_occupied_should_raise_exception(mock_room_free):
    with pytest.raises(RoomStatusError, match='the status occupied can\'t be changed'):
        change_room_status(mock_room_free, {'status': 'Occupied'})

def test_change_room_status_from_occupied_to_dirty_should_raise_exception(mock_room_occupied):
    with pytest.raises(RoomStatusError, match='the status occupied can\'t be changed'):
        change_room_status(mock_room_occupied, {'status': 'Dirty'})

def test_change_room_status_from_dirty_to_maintenance(mock_room_dirty):
    updated_status = 'Maintenance'
    updated_mock_room = change_room_status(mock_room_dirty, {'status': updated_status})

    assert isinstance(updated_mock_room, Room)
    assert updated_mock_room.status == updated_status, (
        f"Expected status {updated_status}, "
        f"but got {updated_mock_room.status}"
    )

def test_change_room_status_from_occupied_to_free_should_raise_exception(mock_room_occupied):
    with pytest.raises(RoomStatusError, match='the status occupied can\'t be changed'):
        change_room_status(mock_room_occupied, {'status': 'Free'})
