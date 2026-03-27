# my_queue = [("xjakub77", 12, 12, 9), ("xchmel22", 10, 64, 10), ("xkolar00", 1, 4, 10)]

# number_of_cluster_threads = 13

def create_cluster(number_of_cluster_threads):
    cluster = []
    remaining_threads = number_of_cluster_threads
    index = 0

    while remaining_threads > 0:
        if remaining_threads == 1:
            cluster.append([f"C{index}", 1, 4])
            remaining_threads -= 1
            index += 1

        threads = remaining_threads // 2

        if threads % 2 != 0:
            threads += 1

        cluster.append([f"C{index}", threads, threads * 4])
        remaining_threads -= threads
        index += 1

    return cluster, len(cluster)

def assign_computer(cluster, queue):
    remaining_threads = len(cluster)

    user_id = queue[0]
    required_threads = queue[1]
    required_memory = queue[2]

    for i in range(remaining_threads - 1, -1, -1):
        computer = cluster[i]

        if computer[1] >= required_threads and computer[2] >= required_memory:
            computer_id = computer[0]

            computer[1] -= required_threads
            computer[2] -= required_memory

            print(f"{user_id} - R ({computer_id})")

            if computer[1] == 0 or computer[2] == 0:
                cluster.pop(i)

            return cluster, (user_id, computer_id)


    print(f"{user_id} - Q")
    return cluster, (user_id, None)

def assign_request(cluster, queue):
    if len(queue) == 0:
        return (None, None), cluster, queue

    max_index = 0
    max_priority = queue[0][3]

    for i in range(1, len(queue)):
        if queue[i][3] > max_priority:
            max_priority = queue[i][0]
            max_index = i

    request = queue[max_index]
    user_id = request[0]
    priority = request[3]

    if priority < 1 or priority > 10:
        print(f"{user_id} - D")
        queue.pop(max_index)
        return (user_id, None), cluster, queue

    cluster, assigned = assign_computer(cluster, request)
    queue.pop(max_index)
    return assigned, cluster, queue


def main(queue, total_threads):
    cluster, pocet_pocitacu = create_cluster(total_threads)

    print(f"Počet počítačů v clusteru: {pocet_pocitacu}")
    print(cluster)

    prirazeni = []

    while len(queue) > 0:
        assigned, cluster, queue = assign_request(cluster, queue)
        prirazeni.append(assigned)

    print("Přiřazení:", prirazeni)
    print("Zbývající zdroje:", cluster)

    return prirazeni, cluster


# final_assignments, rest_of_computer_resources = main(my_queue, number_of_cluster_threads)