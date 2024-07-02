def swap_client_room(reservation, new_room):
    if new_room.status == 'Free':
        if not reservation:
            raise Exception
        old_room = reservation.room
        reservation.room = new_room
        old_room.status = "Dirty"
