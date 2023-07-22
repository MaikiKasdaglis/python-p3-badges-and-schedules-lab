def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge
    
def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = badge_maker(name)
        badges.append(badge)
    return badges

def assign_rooms(names):
    room_assignments = []
    for i in range(len(names)):
        room_number = i + 1
        assignment = f"Hello, {names[i]}! You'll be assigned to room {room_number}!"
        room_assignments.append(assignment)
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in assignments:
        print(assignment)
