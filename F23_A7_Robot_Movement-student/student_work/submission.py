#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 7
#   References: no one
#   Time: 1 hour

import math

# algorithm 1
def location_decision(battery_level, heat, sensor_reading, current_location, button_state):
    old_x, old_y = current_location
    diff = battery_level - heat
    if button_state == 1:
        new_x = old_x + 5
        new_y = old_y + 5
    else:
        if diff <= -50:
            new_x = old_x + 2
            new_y = old_y + 2
        else:
            new_x = old_x + diff + sensor_reading * 2
            new_y = old_y - diff - sensor_reading * 2
    return [new_x, new_y]

# algorithm 2
def battery_level_change(old_battery_level, distance):
    temp = old_battery_level - 5
    if distance > 10:
        temp = temp - distance * 2
    else: 
        temp = temp - distance * 3
    if temp <= 0:
        new_battery_level = 100
    else:
        new_battery_level = temp
    return new_battery_level

# algorithm 3
def heat_change(old_heat, distance):
    temp = old_heat + 10
    if distance > 10:
        temp = temp + distance * 1.2
    else:
        temp = temp + distance * 1.3
    
    if temp >= 160:
        new_heat = 70
    else:
        new_heat = temp
    return new_heat

# main function
def main():
    heat = 100
    battery_level = 100
    current_location = [0,0]
    for i in range(5):
        sensor_reading, button_state = map(int, input("INPUT> ").split())
        new_location = location_decision(battery_level, heat, sensor_reading, current_location, button_state)
        distance = math.sqrt((new_location[0] - current_location[0]) ** 2 + (new_location[1] - current_location[1]) ** 2)
        new_heat = heat_change(heat, distance)
        new_battery = battery_level_change(battery_level, distance)
        battery_level = new_battery
        heat = new_heat
        current_location = new_location
        if battery_level >= 70:
            new_location = location_decision(battery_level, heat, sensor_reading, current_location, button_state)
            distance = math.sqrt((new_location[0] - current_location[0]) ** 2 + (new_location[1] - current_location[1]) ** 2)
            new_heat = heat_change(heat, distance)
            new_battery = battery_level_change(battery_level, distance)
            battery_level = new_battery
            heat = new_heat
            current_location = new_location   
    print(f"OUTPUT {new_location[0]:.3f} {current_location[1]:.3f} {heat:.3f} {battery_level:.3f}")

if __name__ == "__main__":
    main()