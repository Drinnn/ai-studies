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

print(flights[('FCO', 'LIS')])
