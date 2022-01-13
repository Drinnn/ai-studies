import mlrose

people = [('Lisboa', 'LIS'), ('Madrid', 'MAD'),
          ('Paris', 'CDG'), ('Dublin', 'DUB'),
          ('Bruxelas', 'BRU'), ('Londres', 'LHR')]  # City name and Airport abbreviation

destination = 'FCO'  # Rome Airport

flights = {}
for line in open('flights.txt'):
    flight_origin, flight_destination, flight_exit_time, flight_arriving_time, flight_price = line.split(
        ',')
    flights.setdefault((flight_origin, flight_destination), [])
    flights[(flight_origin, flight_destination)].append(
        (flight_exit_time, flight_arriving_time, int(flight_price)))


def print_flights(schedule):
    flight_id = -1
    total_price = 0
    for i in range(len(schedule) // 2):
        origin_city = people[i][0]
        origin_airport_abbreviation = people[i][1]
        flight_id += 1
        departure_flight = flights[(
            origin_airport_abbreviation, destination)][schedule[flight_id]]
        total_price += departure_flight[2]
        flight_id += 1
        return_flight = flights[(
            destination, origin_airport_abbreviation)][schedule[flight_id]]
        total_price += return_flight[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' %
              (origin_city, origin_airport_abbreviation, departure_flight[0], departure_flight[1], departure_flight[2],
               return_flight[0], return_flight[1], return_flight[2]))

    print('Total price: {}'.format(total_price))


def fitness_function(schedule):
    flight_id = -1
    total_price = 0
    for i in range(len(schedule) // 2):
        origin_airport_abbreviation = people[i][1]
        flight_id += 1
        departure_flight = flights[(
            origin_airport_abbreviation, destination)][schedule[flight_id]]
        total_price += departure_flight[2]
        flight_id += 1
        return_flight = flights[(
            destination, origin_airport_abbreviation)][schedule[flight_id]]
        total_price += return_flight[2]

    return total_price


schedule = [1, 2, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]
print_flights(schedule)

fitness = mlrose.CustomFitness(fitness_function)
problem_representation = mlrose.DiscreteOpt(
    length=12, fitness_fn=fitness, maximize=False, max_val=10)
