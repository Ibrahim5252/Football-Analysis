import pandas as pd
from .cleaning import load_and_clean_data
raw_data = load_and_clean_data('/home/ibrahimk/Work/Data_analysis/football_analysis/data/Fifa.csv')

print(len(raw_data["Name"]))

# ! avg player age.
def avg_age():
    avg_age = round(raw_data["Age"].mean(), 1)
    return avg_age

# ! avg ovr.
def avg_ovr():
    avg_ovr = round(raw_data["Overall_Rating"].mean(), 1)
    return avg_ovr

# ! avg player salary.
def avg_sal():
    avg_sal = round(raw_data["Value Per M$"].mean(), 1)
    return avg_sal

#! Player with highest Overall_rating.
def top_10_OVR_player():
    sorted_OVR = raw_data.sort_values('Overall_Rating', ascending=False)
    top_10_OVR_player = sorted_OVR[:10]
    return top_10_OVR_player
# print(top_10_OVR_player())


#! player with no futuer potential.
def no_potential_player():
    E_OVR = raw_data[raw_data['Overall_Rating'] == raw_data['Future Potential']]
    return E_OVR



#! Top 10 Young Player(>=25) with good potential.
def high_potential_player():
    Young_Player = raw_data[raw_data['Age'] <= 25 ]
    high_potential_player = (
        Young_Player
        .assign(gap=Young_Player['Future Potential'] - Young_Player['Overall_Rating'])
        .query("gap != 0")
        .sort_values(by="gap", ascending=False)
    )
    return high_potential_player[["Name", "Position", "Overall_Rating", "Future Potential", "gap" , "Country",   "Age", "Team", "Value Per M$", "Total_Stats Score"]].head(10)

#! Highest scoring palyer of all time.
def H_S_P():
    H_S_P = raw_data.sort_values("Total_Stats Score", ascending=False)
    return H_S_P



#! highest earning players.
def highest_earning_players():
    H_E_P = raw_data.sort_values("Value Per M$", ascending=False)
    return H_E_P.head(10)








