def get_indices_of_item_weights(weights, length, limit):

    weights_dictionary = dict()

    for i in range(length):
        ## See if a weight KV is contained in dict that is equal to amount
        ## after subtracing "i" (current value) from the limit
        amount = weights_dictionary.get(limit - weights[i])

        ## Return a tuple and index if the amount exists
        if amount != None:
            print("Successful operation")
            return (i, amount)

        ## If it doesnt exist, then set the key as current value from weight list
        ## and the value as the index at where it's found
        else:
            weights_dictionary[weights[i]] = i

    ## Sum of weights does not equal amount of limit
    print("Non successful operation")
    return None


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
weights_error = [1,2,3,4,5]

get_indices_of_item_weights(weights_4, 9, 21)
get_indices_of_item_weights(weights_error,5,10)