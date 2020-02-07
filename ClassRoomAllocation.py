"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

The solution below is in O(n^2) time. There are 3 nested for loops, but only n classes are stored
in the nested list of bookings.
"""
classTimes = [(30, 75), (0, 50), (60, 150), (0, 200), (20, 30), (50, 100), (35, 50), (75, 95)]
roomBookings = []


# Finds if the two time slots overlap
def collide(time1, time2):
    return time1[0] < time2[1] and time2[0] < time1[1]


# Allocate a room for the booking: newTime
def allocateRoom(newTime):
    for room in roomBookings:
        collided = False
        for booking in room:
            collided |= collide(newTime, booking)
        # If the new booking does not collide with any of the others
        if not collided:
            room.append(newTime)
            return 0    # No new room is required
    roomBookings.append([newTime])
    return 1    # 1 new room required


# Find the number of rooms required for the the classBookings
def findNumRooms(classes):
    if len(classes) == 0:
        return 0
    numRooms = 0
    for booking in classes:
        numRooms += allocateRoom(booking)
    return numRooms


def main():
    numRooms = findNumRooms(classTimes)
    print("Number of required rooms: " + str(numRooms))
    print("The room bookings are: " + str(roomBookings))


if __name__ == "__main__":
    main()
