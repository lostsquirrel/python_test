# Machine Learning in Python

## Classification
Classification of Weather Data 
using scikit-learn 
### weather data 

Each row, or sample, consists of the following variables:

- number: unique number for each row
- air_pressure_9am: air pressure averaged over a period from 8:55am to 9:04am (Unit: hectopascals)
- air_temp_9am: air temperature averaged over a period from 8:55am to 9:04am (Unit: degrees Fahrenheit)
- air_wind_direction_9am: wind direction averaged over a period from 8:55am to 9:04am (Unit: degrees, with 0 means coming from the North, and increasing clockwise)
- air_wind_speed_9am: wind speed averaged over a period from 8:55am to 9:04am (Unit: miles per hour)
- ** max_wind_direction_9am: ** wind gust direction averaged over a period from 8:55am to 9:10am (Unit: degrees, with 0 being North and increasing clockwise*)
- max_wind_speed_9am: wind gust speed averaged over a period from 8:55am to 9:04am (Unit: miles per hour)
- rain_accumulation_9am: amount of rain accumulated in the 24 hours prior to 9am (Unit: millimeters)
- rain_duration_9am: amount of time rain was recorded in the 24 hours prior to 9am (Unit: seconds)
- relative_humidity_9am: relative humidity averaged over a period from 8:55am to 9:04am (Unit: percent)
- relative_humidity_3pm: relative humidity averaged over a period from 2:55pm to 3:04pm (*Unit: percent *)

## Clustering with scikit-learn

### weather data

https://drive.google.com/open?id=0B8iiZ7pSaSFZb3ItQ1l4LWRMTjg

- rowID: unique number for each row (Unit: NA)
- hpwren_timestamp: timestamp of measure (Unit: year-month-day hour:minute:second)
- air_pressure: air pressure measured at the timestamp (Unit: hectopascals)
- air_temp: air temperature measure at the timestamp (Unit: degrees Fahrenheit)
- avg_wind_direction: wind direction averaged over the minute before the timestamp (Unit: degrees, with 0 means coming from the North, and increasing clockwise)
- avg_wind_speed: wind speed averaged over the minute before the timestamp (Unit: meters per second)
- max_wind_direction: highest wind direction in the minute before the timestamp (Unit: degrees, with 0 being North and increasing clockwise)
- max_wind_speed: highest wind speed in the minute before the timestamp (Unit: meters per second)
- min_wind_direction: smallest wind direction in the minute before the timestamp (Unit: degrees, with 0 being North and inceasing clockwise)
- min_wind_speed: smallest wind speed in the minute before the timestamp (Unit: meters per second)
- rain_accumulation: amount of accumulated rain measured at the timestamp (Unit: millimeters)
- rain_duration: length of time rain has fallen as measured at the timestamp (Unit: seconds)
- relative_humidity: relative humidity measured at the timestamp (Unit: percent)
