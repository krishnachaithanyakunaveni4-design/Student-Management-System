
def linear_search(students, target_id):
    for student in students:
        if student[0] == target_id:
            return student

    return None


def merge_sort(students):
    if len(students) <= 1:
        return students

    middle = len(students) // 2

    left = merge_sort(students[:middle])
    right = merge_sort(students[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Merge in descending order of marks
    while i < len(left) and j < len(right):
        if left[i][5] >= right[j][5]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining students
    result.extend(left[i:])
    result.extend(right[j:])

    return result

