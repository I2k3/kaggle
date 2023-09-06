def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    num=0
    for num in nums:
        if num % 7 == 0:
            return True

    return False

# Check your answer
q1.check()
