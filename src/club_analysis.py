import pandas as pd
from src.cleaning import load_and_clean_data

raw_data = load_and_clean_data('/home/ibrahimk/Work/Data_analysis/football_analysis/data/Fifa.csv')

#! clubs info -: spending, players, scores.
def club_info(team):
    team_name = raw_data[raw_data['Team'] == team]


    team_info = pd.pivot_table(
        team_name,
        index='Name',  # player names as rows
        values=['Age', 'Overall_Rating', 'Value Per M$', 'Total_Stats Score'],  
        aggfunc='first'  # just take the value (or use sum, mean, etc. if duplicates)
    )


    total = pd.Series({
        # 'Age' : team_info['Age'].mean(),
        # 'Overall_Rating' : team_info['Overall_Rating'].mean(),
        'Total_Stats Score': team_info['Total_Stats Score'].sum(), 
        'Value Per M$': team_info['Value Per M$'].sum(),          

    })

    Avg = pd.Series({
        'Age' : team_info['Age'].mean(),
        'Overall_Rating' : team_info['Overall_Rating'].mean(),

    })

    total.name = 'Total Scores & Spending' #? giving name to series.
    Avg.name = "avg age and OVR"
    team_info = pd.concat([team_info, total.to_frame().T]) #? total is a Series (one-dimensional), to_frame() converts it into a DataFrame with one column:
    team_info = pd.concat([team_info, Avg.to_frame().T])
    #? Set pandas float format to show 1 decimal place
    pd.options.display.float_format = '{:.1f}'.format
    # # print(team_info)
    # highest_scoring_players = team_info.sort_values('Total_Stats Score', ascending=False).head(10)
    # highest_earnig_players = team_info.sort_values('Value Per M$', ascending=False).head(10)
    # highest_rating_players = team_info.sort_values('Overall_Rating', ascending=False).head(10)
    team_info.index.name = "Player Name"
    return team_info




def total_club():
    total_club = len(raw_data['Team'].unique())
    return total_club


def club_total_spending():
    club = raw_data.groupby("Team")["Value Per M$"]
    cl = club.sum()
    club_total_spending = pd.DataFrame(cl).reset_index()
    return club_total_spending.sort_values("Value Per M$", ascending=False)


def club_total_goals():
    club = raw_data.groupby("Team")["Total_Stats Score"]
    cl = club.sum()
    club_total_goals = pd.DataFrame(cl).reset_index()
    return club_total_goals.sort_values("Total_Stats Score", ascending=False)

def club_avg_rated_player():
    cl = raw_data.groupby("Team")["Overall_Rating"]
    cd = round(cl.mean(), 1)
    club_avg_rated_player = pd.DataFrame(cd).reset_index()
    return club_avg_rated_player.sort_values("Overall_Rating", ascending=False)

def club_avg_spending():
    cl = club_total_spending()["Value Per M$"]
    avg = round(cl.mean(), 1)
    return avg

def club_avg_squad_rate():
    cl = club_avg_rated_player()["Overall_Rating"]
    cd = round(cl.mean(), 1)
    return cd







