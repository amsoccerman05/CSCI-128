    #   Aiden Morrison
    #   CSCI 128 – Section J
    #   Assessment 12
    #   References: no one
    #   Time: 2 hours

def parse_price_file(filename):
    plane_info = []
    ticket_info = open(filename, 'r')
    plane_parts = []
    for line in ticket_info:
        line = line[:-1]
        plane_parts = []
        plane_parts = line.split()
        plane_info.append(plane_parts)
    number_of_seats = int(plane_info[0][0])
    plane_info = plane_info[1:]
    return [plane_info, number_of_seats]

def ticket_pricing(price_data, week, num_seats):
    if week < 1 or num_seats < 1:
        return 0
    most_revenue = []
    seats_taken = 0
    for option in price_data[len(price_data) - week]:
        seating = option.split(",")
        price = int(seating[0])
        seats = int(seating[1])
        seats_taken = min(seats, num_seats)
        most_revenue.append(
            ticket_pricing(price_data, week - 1, num_seats - seats_taken)
            + (price * seats_taken)
        )
    return max(most_revenue)

if __name__ == '__main__':
    filename = input("DATA_FILE> ")
    file_data = parse_price_file(filename)
    price_data = file_data[0]
    num_seats = file_data[1]
    max_possible_revenue = ticket_pricing(price_data, len(price_data), num_seats)
    print(f"OUTPUT {max_possible_revenue}")
    # print(parse_price_file("one_week_1.txt"))
    # print(parse_price_file("two_weeks_1.txt"))
    # print(ticket_pricing([['10,999', '100,999', '1000,999']], 1, 5))
    # print(ticket_pricing([['375,5', '676,15', '830,6'], ['45,57', '355,20', '575,8']], 2, 13))
    # print(ticket_pricing([['375,5', '676,15', '830,6'],['45,57', '355,20', '575,8']], 1, 7))
    # print(ticket_pricing([['375,5', '676,15', '830,6'],['45,57', '355,20', '575,8']], 0, 1000))
    # print(ticket_pricing([['375,5', '676,15', '830,6'],['45,57', '355,20', '575,8']], 2, 0))
