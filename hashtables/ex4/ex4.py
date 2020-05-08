def has_negatives(a):

    result = []
    numbers_hash_table = dict()

    ## Iterating through the hash table and finding if absolute values exist
    for i in a:
        value = i * -1
        if value in numbers_hash_table:
            result.append(abs(value))
        else:
            numbers_hash_table[i] = i

    return result

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
