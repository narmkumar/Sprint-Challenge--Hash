#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    route = []
    route_hash_table = {}

    for n in tickets: ## Creating key values in hash table
        route_hash_table[n.source] = n.destination

    key = "NONE"

    ## Iterate through to append the destination to the routes lists
    for i in range(1, length):
        route.append(route_hash_table[key])
        key = route_hash_table[key]

    route.append("NONE")
    return route