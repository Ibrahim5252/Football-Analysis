import pandas as pd
from src.cleaning import load_and_clean_data
import numpy as np
raw_data = load_and_clean_data('/home/ibrahimk/Work/Data_analysis/football_analysis/data/Fifa.csv')



#! Number of countries.
def countries():
    countries = raw_data['Country'].unique()
    return len(countries)




#! top player produce by each country.
def top_country_player():
    tcp = raw_data.groupby('Country')['Overall_Rating'].transform('max')
    tp = raw_data[raw_data['Overall_Rating'] == tcp]

    result = tp.groupby('Country').agg({
        'Name': list,
        'Overall_Rating': 'first'  
    }).reset_index()

    result = result.sort_values("Overall_Rating", ascending=False)
    return result



#! ovr of each countries.
def top_countries_OVR():
    df = raw_data.groupby('Country').agg(
        avg_rating=('Overall_Rating', 'mean'),
        player_count=('Overall_Rating', 'count')
    ).reset_index()

    df["strength_index"] = df["avg_rating"] * np.log1p(df["player_count"])

    return round(df.sort_values("avg_rating", ascending=False),1)



#! which country produce player based on position
def country_pos():
    ps = raw_data.groupby(['Country', 'Position']).size().unstack(fill_value=0).reset_index()

    forwards = ['CF', 'ST', 'LW', 'RW']
    midfielders = ['CAM', 'CM', 'CDM', 'LM', 'RM']
    defenders = ['CB', 'LB', 'RB', 'LWB', 'RWB', 'SW']
    goalkeepers = ['GK']

    ps['Forward'] = ps[forwards].sum(axis=1)
    ps['Midfielder'] = ps[midfielders].sum(axis=1)
    ps['Defender'] = ps[defenders].sum(axis=1)
    ps['Goalkeeper'] = ps[goalkeepers].sum(axis=1)

    position_counts = ps.groupby('Country')[['Forward', 'Midfielder', 'Defender', 'Goalkeeper']].sum().reset_index()
    top_Forward_country = position_counts[['Country', 'Forward']].sort_values('Forward', ascending=False)
    top_Midfielder_country = position_counts[['Country', 'Midfielder']].sort_values('Midfielder', ascending=False)
    top_Defender_country = position_counts[['Country', 'Defender']].sort_values('Defender', ascending=False)
    top_Goalkeeper_country = position_counts[['Country', 'Goalkeeper']].sort_values('Goalkeeper', ascending=False)
    result = pd.merge(top_Forward_country, top_Midfielder_country, on="Country")
    result = pd.merge(result, top_Defender_country, on="Country")
    result = pd.merge(result, top_Goalkeeper_country, on="Country")
    return result
# print(country_pos())

def avg_rating():
    con = round(raw_data.groupby("Country")["Overall_Rating"].mean(), 1).reset_index()
    avg_rating = round(con["Overall_Rating"].mean(), 1)
    return avg_rating

def avg_player_earning():
    con = round(raw_data.groupby("Country")["Value Per M$"].mean(), 1).reset_index()
    avg_earn = round(con["Value Per M$"].mean(), 1)
    return avg_earn


