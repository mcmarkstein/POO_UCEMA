dataframe_en_dict = {"auto":1,"tiempo_vuelta":"1:36.60",
                     "auto":2,"tiempo_vuelta":"1:36.60",
                        "auto":3,"tiempo_vuelta":"1:36.60"}

import pandas as pd

df = pd.DataFrame(dataframe_en_dict, index=[0,1,2])

def time_to_seconds(time):
    hours_in_seconds = int(time.split(":")[0]) * 3600
    minutes_in_seconds = int(time[0]) * 60
    seconds_in_seconds =  int(time.split(".")[1])
    return hours_in_seconds + minutes_in_seconds + seconds_in_seconds

df["tiempo_vuelta"] = df["tiempo_vuelta"].apply(time_to_seconds)