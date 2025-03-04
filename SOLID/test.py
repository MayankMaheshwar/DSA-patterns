# Libraries Included:
# Numpy, Scipy, Scikit, Pandas


def best_meeting(schedules):
    """Finds the best meeting that can be scheduled given a list of existing schedules of meetings.
    schedules is a list of schedules.
    A schedule consists of a list of meetings where each meeting is a tuple of [start_hour, end_hour) where end_hour is exclusive.
      So [3, 6] means the meeting lasts from the begining of hour 3 to the beining of hour 6. The person is free in hour 6.
    There are three levels to this function that can be tackled one at a time:
    """

    # 1. Find the largest number of people that can attend a meeting if they're free in that time range. Print the number of people.
    largest_num_people = 0
    # Your code here

    print(
        f"The largest number of people that can attend a meeting is {largest_num_people}"
    )

    # 2. Find the largest meeting and print how many free people can attend as well as the start and end hour of the meeting.
    #    The largest meeting is defined as:
    #    - The meeting that includes the most people
    #    - If there are multiple meetings that tie for the most people chose the meeting that starts the earliest
    largest_num_people = 0
    meeting_start = 0
    meeting_end = 0
    # Your code here

    print(
        f"The largest meeting has {largest_num_people} people attending. It starts at {meeting_start} and ends at {meeting_end}."
    )

    # 3. Find the "largest and longest" meeting and print how many people can attend as well as the start and end hour of the meeting.
    #    The "largest and longest" meeting is defined as:
    #    - The meeting that includes the most people
    #    - If there are multiple meetings that tie for the most people chose the meeting that lasts the longest. Meetings are considered continuous as long as the same people are attending.
    largest_num_people = 0
    meeting_start = 0
    meeting_end = 0
    # Your code here
    print(
        f"The largest and longest meeting has {largest_num_people} people attending. It starts at {meeting_start} and ends at {meeting_end}."
    )


person1_schedule = [[0, 3], [7, 9], [9, 11], [13, 17], [19, 24]]
person2_schedule = [[0, 3], [4, 11], [13, 20], [22, 24]]
person3_schedule = [[0, 4], [9, 11], [13, 20]]
person4_schedule = [[2, 3], [8, 9], [10, 13]]
person5_schedule = [[3, 8], [11, 13], [17, 22]]
best_meeting(
    [
        person1_schedule,
        person2_schedule,
        person3_schedule,
        person4_schedule,
        person5_schedule,
    ]
)
