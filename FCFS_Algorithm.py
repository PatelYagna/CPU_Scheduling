import time

#first come first serve algorithm for scheduling process
def fcfs(process):

    # sort the processes bsed on arrival time
    # and use the priority as the arbitration rule
    processes.sort(key=lambda x: (x[1], x[2]))

    current_time = 0
    turnaruond_times = []
    completion_times = []

    print ("Starting the FCFS Scheduling Process... \n")

    for process in processes:
        process_id, arrival_time, burst_time, priority = process # grab the process details
        if current_time < arrival_time: # check if the process is due to schedule
            print(f'Waiting for process {process_id} to arrive at time {arrival_time}')
            time.sleep(arrival_time - current_time) # process will wait
            current_time = arrival_time # update the current time

        # simulate process execution
        print(f'Executing Process {process_id}, CPU Time: {burst_time}')
        time.sleep(burst_time) # sleep to simulate process burst time

        # calculate the completion time for the current process
        process_completion_time = current_time + burst_time
        completion_times.append(process_completion_time)

        # calculate the trunaround time: completion time - arrival time
        process_turnaround_time = process_completion_time - arrival_time
        turnaruond_times.append(process_turnaround_time)

        #curernt_time += burst_time # update the current time
        current_time += burst_time # update the current time

        print(f'Process {process_id} completed. Turnaround Time: {process_turnaround_time}')

    # calculate the average turnaround time
    average_turnaround_time = sum(turnaruond_times) / len(turnaruond_times)
    print(f'\nAll Process Completed. Average Turnaround Time: {average_turnaround_time:.2f} seconds')


# Test the FCFS Algorithm
processes = [[1, 0, 6, 1],
             [2, 1, 3, 1],
             [3, 3, 2, 1]]

fcfs(processes)
