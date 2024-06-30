## Change Room Status Use Case Specification

### Use Case Name
Change Room Status

### Brief Description
This use case manages the status changes of hotel rooms among four possible states: Free, Occupied, Maintenance, and Dirty. It ensures that room statuses are updated according to operational needs, except for transitions involving Occupied statuses, which are managed exclusively by the Check-in and Check-out processes.

### Actors
- **User**: Initiates status changes.
- **Employee**: Executes status changes based on operational requirements.

### Preconditions
- The hotel management application is operational.
- Rooms have been correctly assigned one of the statuses: Free, Occupied, Maintenance, or Dirty.

### Basic Flow of Events
1. **User requests status change**: The user (such as a hotel receptionist or automated system) initiates a status change request for a specific room.
2. **Verify current status**: The application checks the current status of the room.
3. **Perform status update**: 
   - If the room is currently Free, Maintenance, or Dirty:
     - The status can be changed to any other valid status (Free, Maintenance or Dirty) as needed.
   - **Exceptions**:
     - Rooms currently Occupied cannot have their status changed by this process.
     - No room can be changed to Occupied status through this process; this responsibility lies with the Check-in process.
     
### Alternative Flows
- **Invalid status change request**: If the requested status change violates these rules (e.g., attempting to change an Occupied room status), the system notifies the user and prevents the change.

### Postconditions
- The room status is updated according to the specified use case scenario.

### Business Rules
- Room status changes are restricted to maintain consistency and operational integrity.
- Check-in and Check-out processes manage transitions involving Occupied statuses.

### Notes
- This use case streamlines room status management while ensuring compliance with operational rules.
