def calculate_zones(heart_rate_stream):
    try:
        athlete_age = 23
        # Calculate maximum heart rate (V02 max)
        max_heart_rate = 220 - athlete_age

        # Define heart rate zones (percentage ranges of maximum heart rate)
        zones = {
            'Zone_1': (0.5 * max_heart_rate, 0.6 * max_heart_rate),
            'Zone_2': (0.6 * max_heart_rate, 0.7 * max_heart_rate),
            'Zone_3': (0.7 * max_heart_rate, 0.8 * max_heart_rate),
            'Zone_4': (0.8 * max_heart_rate, 0.9 * max_heart_rate),
            'Zone_5': (0.9 * max_heart_rate, 1.0 * max_heart_rate)
        }
        time_in_zones = {zone: 0 for zone in zones}

        for heart_rate in heart_rate_stream:
            for zone, (lower, upper) in zones.items():
                if lower <= heart_rate <= upper:
                    time_in_zones[zone] += 1  # Increment time for the corresponding zone

        # Convert time in each zone to percentages
        time_in_zones_percentage = {}
        total_time = len(heart_rate_stream)  # Total duration of heart rate measurements

        for zone, time in time_in_zones.items():
            time_in_zones_percentage[zone] = (time / total_time) * 100

        # print(time_in_zones_percentage)
        return time_in_zones_percentage

    except Exception as error:
        print(error,'(inside calculate hr zones script)')


if __name__ == "__main__":
    calculate_zones()
