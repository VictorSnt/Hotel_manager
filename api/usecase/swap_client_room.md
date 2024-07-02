## Change Guest Room Use Case Specification

### Use Case Name
Change Guest Room

### Brief Description
This use case manages guest room changes, which can occur for various reasons such as guest dissatisfaction with their current room or issues with room functionality. The guest's room can be changed without issues if the new room's status is Free.

### Actors
- **Guest**: Requests the room change.
- **Employee**: Executes the room change.

### Preconditions
- The hotel management application is operational.
- The new room is Free and has no reservations for the current day.

### Basic Flow of Events
1. **Guest requests room change**: The guest requests a room change, either through an employee (such as a hotel receptionist) or an automated system.

2. **Verify current status of the new room**: The application checks if the current status of the new room is Free.

3. **Perform room swap**:
   - Transfer all data of the guest's reservation to the new room.
   - Change the status of the old room to Dirty to ensure it is not assigned to a new guest before it is ready for use.

4. **Handle exceptions**:
   - If there is no active reservation for the guest requesting the room change, the system notifies the user and prevents the change.
   - If the new room's status is not Free, the system notifies the user and prevents the change.

### Alternative Flows
- **Invalid swap request**: If the requested swap violates any rules (e.g., attempting to change to a room that is not Free), the system notifies the user and prevents the change.

### Postconditions
- The guest's reservation data is transferred to the new room.
- The status of the old room is updated to Dirty.