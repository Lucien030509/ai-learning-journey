course_status = {"COMP9001": "Python basics", "COMP9120": "SQL basics", "COMP5310": "Data science foundations", "INFO5990": "Professional practice"}
def show_course_status(statuses):
    for course in statuses:
        print(f"{course}: {statuses[course]}")
def update_course_status(statuses, course_code, new_status):
    statuses[course_code] = new_status
course_code = input("Enter course code:")
if course_code in course_status:
    new_status = input("Enter new course status: ")
    update_course_status(course_status, course_code, new_status)
else:
    print(f"{course_code} is not a valid course code.")
show_course_status(course_status)