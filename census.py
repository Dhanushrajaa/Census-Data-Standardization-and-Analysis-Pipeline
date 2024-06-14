import streamlit as st
import psycopg2
import pandas as pd

# Connect to PostgreSQL database
def get_connection():
    conn = psycopg2.connect(
        dbname="census_db",
        user="postgres",
        password="postgresql",
        host="localhost",
        port="5432"
    )
    return conn

# Execute a query and return a DataFrame
def execute_query(query):
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Streamlit 
st.title('Census Data Analysis')

# 1. Total population of each district
st.subheader('Total Population of Each District')
query = """
    SELECT district, SUM(population) AS total_population
    FROM census
    GROUP BY district
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

#2. Literate males and females in each district
st.subheader('Literate Males and Females in Each District')
query = """
    SELECT district, SUM(literate_male) AS literate_males, SUM(literate_female) AS literate_females
    FROM census
    GROUP BY district
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

# 3. Percentage of workers (both male and female) in each district
st.subheader('Percentage of Workers in Each District')
query = """
    SELECT district,
           (SUM(male_workers)::FLOAT / SUM(population) * 100) AS male_workers_percentage,
           (SUM(female_workers)::FLOAT / SUM(population) * 100) AS female_workers_percentage
    FROM census
    GROUP BY district
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

# 4. Households with access to LPG or PNG as cooking fuel in each district
st.subheader('Households with Access to LPG or PNG as Cooking Fuel in Each District')
query = """
    SELECT district, SUM(lpg_or_png_households) AS households_with_lpg_png
    FROM census
    GROUP BY district
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

# 5. Religious composition of each district
st.subheader('Religious Composition of Each District')
query = """
     SELECT district,SUM(hindus) AS hindus,SUM(muslims) AS muslims,SUM(christians) AS christians,
        SUM(sikhs) AS sikhs,SUM(buddhists) AS buddhists,SUM(jains) AS jains,SUM(Others_Religions
) AS others,
        SUM(religion_not_stated) AS religion_not_stated
FROM census
GROUP BY district;
"""
df = execute_query(query)
st.write(df)

# 6. Households with internet access in each district
st.subheader('Households with Internet Access in Each District')
query = """
    SELECT district, SUM(households_with_internet) AS households_with_internet
    FROM census
    GROUP BY district
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

# 7. Educational attainment distribution in each district
st.subheader('Educational Attainment Distribution in Each District')
query = """
    SELECT district,SUM(Below_Primary_Education) AS below_primary,SUM(Primary_Education) AS primary,SUM(Middle_Education) AS middle,
           SUM(Secondary_Education) AS secondary
    FROM census
    GROUP BY district;
"""
df = execute_query(query)
st.write(df)

# 8. Households with access to various modes of transportation in each district
st.subheader('Households with Access to Various Modes of Transportation in Each District')
query = """
    SELECT district, 
           SUM(Households_with_Bicycle) AS households_with_bicycle,
           SUM(Households_with_Car_Jeep_Van) AS households_with_car,
           SUM(Households_with_Radio_Transistor) AS households_with_radio,
           SUM(households_with_television) AS households_with_television
    FROM census
    GROUP BY district
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

# 9. Condition of occupied census houses in each district
st.subheader('Condition of Occupied Census Houses in Each District')
query = """
    SELECT district, 
           SUM(Condition_of_occupied_census_houses_Dilapidated_Households) AS houses_dilapidated,
           SUM(Households_with_separate_kitchen_Cooking_inside_house) AS houses_with_separate_kitchen,
           SUM(Having_bathing_facility_Total_Households) AS houses_with_bathing_facility,
           SUM(Having_latrine_facility_within_the_premises_Total_Households) AS houses_with_latrine_facility
    FROM census
    GROUP BY district
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

# 10. Household size distribution in each district

st.subheader('Household Size Distribution in Each District')
query = """
    SELECT district,
           SUM(Household_size_1_person_Households) AS Household_size_1_person_Households,
           SUM(Household_size_2_persons_Households) AS Household_size_2_persons_Households,
           SUM(Household_size_3_to_5_persons_Households) AS Household_size_3_to_5_persons_Households
    FROM census
    GROUP BY district 
    ORDER BY district;
"""
df = execute_query(query)
st.write(df)

# 11. Total number of households in each state
st.subheader('Total Number of Households in Each State')
query = """
    SELECT State_UT, SUM(Households) AS total_households
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 12. Households with a latrine facility within the premises in each state
st.subheader('Households with Latrine Facility within the Premises in Each State')
query = """
    SELECT State_UT, SUM(Having_latrine_facility_within_the_premises_Total_Households) AS households_with_latrine
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 13. Average household size in each state
st.subheader('Average Household Size in Each State')
query = """
    SELECT State_UT, AVG(Household_size_1_person_Households) AS Household_size_1_person_Households ,
           AVG(Household_size_2_persons_Households) AS Household_size_2_persons_Households,
           AVG(Household_size_1_to_2_persons) AS Household_size_1_to_2_persons,
           AVG(Household_size_3_persons_Households) AS Household_size_3_persons_Households,
           AVG(Household_size_3_to_5_persons_Households) AS Household_size_3_to_5_persons_Households,
           AVG(Household_size_4_persons_Households) AS Household_size_4_persons_Households,
           AVG(Household_size_5_persons_Households) AS Household_size_5_persons_Households,
           AVG(Household_size_6_8_persons_Households) AS Household_size_6_8_persons_Households,
           AVG(Household_size_9_persons_and_above_Households) AS Household_size_9_persons_and_above_Households
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 14. Households owned versus rented in each state
st.subheader('Households Owned versus Rented in Each State')
query = """
    SELECT State_ut, 
           SUM(Ownership_Owned_Households) AS households_owned, 
           SUM(Ownership_Rented_Households) AS households_rented
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 15. Distribution of different types of latrine facilities in each state
st.subheader('Distribution of Different Types of Latrine Facilities in Each State')
query = """
    SELECT State_UT,
           SUM(Type_of_latrine_facility_Pit_latrine_Households) AS Pit_latrine_Households,
           SUM(Type_of_latrine_facility_Other_latrine_Households) AS Other_latrine_Households,
           SUM(Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households) AS Night_soil_disposed_into_open_drain_Households,
           SUM(Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households) AS Flush_pour_flush_latrine_connected_to_other_system_Households
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 16. Households with access to drinking water sources near the premises in each state
st.subheader('Households with Access to Drinking Water Sources near the Premises in Each State')
query = """
    SELECT State_UT, SUM(Location_of_drinking_water_source_Near_the_premises_Households) AS drinking_water_source_Near_the_premises_Households
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 17. Average household income distribution in each state
st.subheader('Average Household Income Distribution in Each State')
query = """
    SELECT State_UT,
        AVG(Power_Parity_Less_than_Rs_45000) AS avg_income_less_than_45000,
        AVG(Power_Parity_Rs_45000_90000) AS avg_income_45000_90000,
        AVG(Power_Parity_Rs_90000_150000) AS avg_income_90000_150000,
        AVG(Power_Parity_Rs_150000_240000) AS avg_income_150000_240000,
        AVG(Power_Parity_Rs_240000_330000) AS avg_income_240000_330000,
        AVG(Power_Parity_Rs_330000_425000) AS avg_income_330000_425000,
        AVG(Power_Parity_Rs_425000_545000) AS avg_income_425000_545000,
        AVG(Power_Parity_Above_Rs_545000) AS avg_income_above_545000
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 18. Percentage of married couples with different household sizes in each state
st.subheader('Percentage of Married Couples with Different Household Sizes in Each State')
query = """
    SELECT State_UT,
         SUM(Married_couples_1_Households) AS married_couples_1,
         SUM(Married_couples_2_Households) AS married_couples_2,
         SUM(Married_couples_3_Households) AS married_couples_3,
         SUM(Married_couples_3_or_more_Households) AS married_couples_3_or_more,
         SUM(Married_couples_4_Households) AS married_couples_4,
         SUM(Married_couples_5__Households) AS married_couples_5,
         SUM(Married_couples_None_Households) AS Married_couples_None_Households,
         SUM(Household_size_1_person_Households) AS household_size_1,
         SUM(Household_size_2_persons_Households) AS household_size_2,
         SUM(Household_size_3_to_5_persons_Households) AS household_size_3_to_5,
         SUM(Household_size_6_8_persons_Households) AS household_size_6_8,
         SUM(Household_size_9_persons_and_above_Households) AS household_size_9_above
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 19. Households below the poverty line in each state
st.subheader('Households Below the Poverty Line in Each State')
query = """
    SELECT State_UT,
        SUM(Power_Parity_Less_than_Rs_45000) AS Below_Rs_45000,
        SUM(Power_Parity_Rs_45000_90000) AS Rs_45000_to_90000,
        SUM(Power_Parity_Rs_90000_150000) AS Rs_90000_to_150000,
        SUM(Power_Parity_Rs_150000_240000) AS Rs_150000_to_240000,
        SUM(Power_Parity_Rs_240000_330000) AS Rs_240000_to_330000,
        SUM(Power_Parity_Rs_330000_425000) AS Rs_330000_to_425000,
        SUM(Power_Parity_Rs_425000_545000) AS Rs_425000_to_545000,
        SUM(Power_Parity_Above_Rs_545000) AS Above_Rs_545000
    FROM census
    GROUP BY State_UT
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)

# 20. Overall literacy rate in each state
st.subheader('Overall Literacy Rate in Each State')
query = """
    SELECT State_UT, 
           (SUM(Literate)::FLOAT / SUM(Population) * 100) AS literacy_rate
    FROM census
    GROUP BY State_UT 
    ORDER BY State_UT;
"""
df = execute_query(query)
st.write(df)






