
import psycopg2

# Establish database connection
try:
    connection = psycopg2.connect(
        dbname='Strava_data',
        user='postgres',
        password='Letscode@123',
        host='localhost',
        port='5432'
    )

    print("Connection established successfully")
    cursor = connection.cursor()

    def insert_data(data):
        try:

            insertion_query = '''    
                INSERT INTO activities (
                    activity_id, activity_name, activity_duration, distance, elevation_gain, activity_type, date_time,
                    avg_speed, max_speed, weight, avg_heart_rate, highest_heart_rate, hr_zone_1,
                    hr_zone_2, hr_zone_3, hr_zone_4, hr_zone_5, calories_burnt
                )
                VALUES (
                    %(activity_id)s, %(name)s, %(activity_time)s, %(distance)s, %(elevation_gain)s, %(type)s,
                    %(date)s, %(avg_speed)s, %(max_speed)s, %(weight)s, %(avg_heartrate)s, %(max_heartrate)s,
                     %(Zone_1)s, %(Zone_2)s, %(Zone_3)s, %(Zone_4)s, %(Zone_5)s, %(calories_burnt)s
                )
            '''
            cursor = connection.cursor()
            cursor.execute(insertion_query, data)




            print('Data inserted successfully')
            connection.commit()  # Commit changes to the database

            cursor.close()

        except psycopg2.Error as e:
            print('Error occurred while inserting data:', e)

    def check_activity_in_db():
        check_acitivity_id = 'select activity_id from activities'
        cursor.execute(check_acitivity_id)
        rows = cursor.fetchall()

        activity_ids = [row[0] for row in rows]
        return activity_ids

    # connection.close()

except psycopg2.Error as error:
    print("Database connection failed:", error)
