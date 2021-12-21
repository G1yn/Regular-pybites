def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sum = 0
    for i,num in enumerate(sequence,1):
       sum += num
       yield(round(sum/i,2))
