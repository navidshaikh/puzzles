def calculateTasksCooldown(tasks, wait):
    # to calculate the sequence ordering
    seq = []
    # to keep a record of a task and its weight
    record = {}
    # initialize time unit counter by 0
    time = 0
    for t in tasks:
        if t not in record:
            # add a new task to sequence
            seq.append(t)
            # add weight of task as per current time
            record[t] = time + wait
        else:
            # if task weight is lapsed
            if record[t] == time:
                seq.append(t)
            else:
                # else find the time units needed
                delta = record[t] - time
                # append "_" to sequence for needed time units
                for i in range(delta+1):
                    seq.append("_")
                    # also increase the time unit counter
                    time = time + 1
                # after the weight for earlier identical task is lapsed, add next to sequence
                seq.append(t)
                # update the weight for task in process as per current time
                record[t] = time + wait
        time += 1
    print "Total time: ", time
    print "Sequence: " + " ".join(str(item) for item in seq)

if __name__ == "__main__":
    calculateTasksCooldown([1,2,2,1,1,2,2], 3)
    calculateTasksCooldown(["A", "B", "A", "D"], 3)

