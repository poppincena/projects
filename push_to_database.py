import psycopg2
from psycopg2 import extras
import json
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


    def insert_activity_data(activity_data):
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
            cursor.execute(insertion_query, activity_data)

            print('Activity Data inserted successfully')
            connection.commit()  # Commit changes to the database

            cursor.close()

        except psycopg2.Error as e:
            print('Error occurred while inserting data:', e)


    def check_activity_in_db():
        try:
            check_acitivity_id = 'select activity_id from activities'
            cursor.execute(check_acitivity_id)
            rows = cursor.fetchall()

            activity_ids = [row[0] for row in rows]
            return activity_ids

        except Exception as error:
            print(error)


    def insert_hr_stream_data(activity_id,stream_data):

        try:
            insertion_query = '''    
                            INSERT INTO hr_stream_data (
                                activity_id, time_stream, hr_stream
                            )
                            VALUES (%s, %s, %s)
                        '''

            # stream_data_tuple = tuple(zip(activity_id,stream_data['heartrate']['data'], stream_data['time']['data']))
            # stream_data_tuple = tuple(
            #     zip([activity_id] * len(stream_data['heartrate']['data']), stream_data['heartrate']['data'],
            #         stream_data['time']['data']))

            time_stream_json = json.dumps(stream_data['time']['data'])
            hr_stream_json = json.dumps(stream_data['heartrate']['data'])

            cursor.execute(insertion_query, (activity_id, time_stream_json, hr_stream_json))
            print("hr stream data inserted")
        except Exception as error:
            print(error)


    # connection.close()


except psycopg2.Error as error:
    print("Database connection failed:", error)
