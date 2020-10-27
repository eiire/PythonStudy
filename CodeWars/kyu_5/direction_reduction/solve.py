def dir_reduc(arr):
    while(True):
        position = 0
        check = False
        for sub_path in list(zip(arr, arr[1:])):
            if (sub_path[0] == 'NORTH' and sub_path[1] == 'SOUTH') or (sub_path[0] == 'SOUTH' and sub_path[1] == 'NORTH'):
                check = True
                arr.pop(position)
                arr.pop(position)
                break

            if (sub_path[0] == 'WEST' and sub_path[1] == 'EAST') or (sub_path[0] == 'EAST' and sub_path[1] == 'WEST'):
                check = True
                arr.pop(position)
                arr.pop(position)
                break

            position += 1

        if not (check):
            break

    return arr
