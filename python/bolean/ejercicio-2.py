if total_candies ==1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(1)
to_smash(91)
