import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import random
from src import player_analysis as ps
from src import club_analysis as cs
from src import country_analysis as ca



st.header("The Beautiful Game: A Data-Driven Analysis of Football Players, Clubs, and Countries")
st.set_page_config(layout="wide")
tab1, tab2, tab3 = st.tabs([":red[Player]", ":blue[Club]", ":green[Country]"])
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:2rem;
    }
</style>
'''


st.markdown(css, unsafe_allow_html=True)
with tab1:
    a, b, c, d = st.columns(4)
    a.metric("**Total player**","**19,667**", border=True)
    b.metric("**Avg Player Age**", f"**{ps.avg_age()}**", border=True)
    c.metric("**Avg player Rating**", f"**{ps.avg_ovr()}**", border=True)
    d.metric("**Avg Player Salary**", f"**${ps.avg_sal()} million**", border=True)

# ! /////////////////////////////////////////////////////////

    st.subheader("Among these, the current top 10 playing players have the highest overall ratings are :- ")
    top_spending_club = ps.top_10_OVR_player()
    hover_cols = ['Team', 'Age', 'Country']  
    fig = px.bar(
        top_spending_club,
        x='Overall_Rating',
        y='Name',  
        orientation='h',
        color='Overall_Rating',
        hover_data=hover_cols, 
        
        
    )

    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        hoverlabel=dict(
        font_size=20,      # change this to your desired size
        font_family="Arial"
        )
    )

   

    st.plotly_chart(fig, use_container_width=True)
# ! /////////////////////////////////////////////////////////

    # st.dataframe(
    #     ps.top_10_OVR_player(),
    #     hide_index=True,
        
    #     column_config={
    #         "Name": st.column_config.Column(
    #             "Player Name",
    #             help="football player names"
    #         ),
    #         "Country":st.column_config.Column(
    #             help="place of origin"
    #         ),
    #         "Position":st.column_config.Column(
    #             help="Postion they play on feild"

    #         ),
    #         "Value Per M$": st.column_config.NumberColumn(
    #             help="Money they earn per month from their respective Club",
    #             format=" $%d M"
    #         ),
    #         "Total_Stats Score": st.column_config.Column(
    #             help="No. of **GOALS** they scored"
    #         ),
    #         "Team": st.column_config.Column(
    #             "Club",
    #             help="Club they are currently playing"
    #         )
           
    #     }

    # )
   

# ! /////////////////////////////////////////////////////////

   
    st.subheader("Let’s now focus on a young, talented player aged 25 or younger, with the potential to reach greatness.")
    # ! Create horizontal stacked bar chart
    df = ps.high_potential_player()
    columns_to_plot = df[["Overall_Rating" ,"Future Potential"]]

    fig = go.Figure()

    for col in columns_to_plot:
        fig.add_trace(go.Bar(
            name=col,
            y=df['Name'],  
            x=df[col],         
            orientation='h',  
            customdata=df[['Age', 'Team', 'Country', 'Total_Stats Score']], 
            hovertemplate="<b>%{y}</b><br>" +
                      f"{col}: %{{x}}<br>" +
                      "Age: %{customdata[0]}<br>" +
                      "Club: %{customdata[1]}<br>" +
                      "Country: %{customdata[2]}<br>" +
                      "Total Score: %{customdata[3]}<br>"
        ))

    fig.update_layout(
        barmode='stack', 
        xaxis_title='Rating',
        yaxis_title='Player Name',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18  # Y-axis title
        
    )
    st.plotly_chart(fig)

    # st.dataframe(
    #     ps.high_potential_player(),
    #     hide_index=True,

    #     column_config={
    #         "gap": st.column_config.NumberColumn(
    #             "Expected Growth",
    #             help="Shows how much a player is expected to improve",
    #             format="%d ▲",
    #         ),
    #         "Team": st.column_config.Column(
    #             "Club",
    #             help="Club they are currently playing"
    #         ),
    #         "Name": st.column_config.Column(
    #             "Player Name",
    #             help="football player names"
    #         ),
    #         "Country":st.column_config.Column(
    #             help="place of origin"
    #         ),
    #         "Position":st.column_config.Column(
    #             help="Postion they play on feild"

    #         ),
    #         "Value Per M$": st.column_config.NumberColumn(
    #             help="Money they earn per month from their respective Club",
    #             format=" $%d M"
    #         ),
    #         "Total_Stats Score": st.column_config.Column(
    #             help="No. of **GOALS** they scored"
    #         ),
    #         "Team": st.column_config.Column(
    #             "Club",
    #             help="Club they are currently playing"
    #         )
    #     }
    # )

# ! /////////////////////////////////////////////////////////

    st.subheader("Now lets talk about the most scoring players")
    top_spending_club = ps.H_S_P().head(10)
    hover_cols = ['Team', 'Age', 'Country', 'Position']  
    fig = px.bar(
        top_spending_club,
        x='Total_Stats Score',
        y='Name',  
        color='Total_Stats Score',
        hover_data=hover_cols,       
    )

    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        xaxis_title='Sccores',
        yaxis_title='Player Name',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        
    )



    st.plotly_chart(fig, use_container_width=True)
 # ! /////////////////////////////////////////////////////////

    st.subheader("Now lets talk about the most Earning players")
    top_spending_club = ps.H_S_P().head(10)
    hover_cols = ['Team', 'Age', 'Country', 'Position']  
    fig = px.bar(
        top_spending_club,
        x='Value Per M$',
        y='Name',  
        color='Value Per M$',
        hover_data=hover_cols,       
    )

    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        xaxis_title='$Salary(Mil)',
        yaxis_title='Player Name',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        
    )
    st.plotly_chart(fig, use_container_width=True)
 


# ! /////////////////////////////////////////////////////////



with tab2:
    a,b,c = st.columns(3)
    a.metric("**Total Club**","**1,009**", border=True )
    b.metric("**Avg spending**", f"**${cs.club_avg_spending()} million**", border=True)
    c.metric("**Avg Club Squad rating**", cs.club_avg_squad_rate(), border=True)
# ! /////////////////////////////////////////////////////////

    st.subheader("Let's discuss the clubs with the highest player salary expenditures.")
    top_spending_club = cs.club_total_spending().head(10)
    hover_cols = ['Team', 'Value Per M$']  
    fig = px.bar(
        top_spending_club,
        x='Value Per M$',
        y='Team',  
        orientation='h',
        color='Value Per M$',
        hover_data=hover_cols, 
        
        
    )

    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        yaxis_title='Club Name',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        hoverlabel=dict(
        font_size=20,      # change this to your desired size
        font_family="Arial"
        )
    )

    fig.update_traces(
        text=top_spending_club['Value Per M$'],
        textposition='outside'
    )

    st.plotly_chart(fig, use_container_width=True)

# ! /////////////////////////////////////////////////////////

    st.subheader("Let's discuss the clubs total score.")
    top_spending_club = cs.club_total_goals().head(10)
    hover_cols = ['Team', 'Total_Stats Score']  
    fig = px.bar(
        top_spending_club,
        x='Total_Stats Score',
        y='Team',  
        orientation='h',
        color='Total_Stats Score',
        hover_data=hover_cols, 
        
        
    )

    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        xaxis_title='Total Goals',
        yaxis_title='Club Name',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        hoverlabel=dict(
        font_size=20,      # change this to your desired size
        font_family="Arial"
        )
    )

    fig.update_traces(
        text=top_spending_club['Total_Stats Score'],
        textposition='outside'
    )

    st.plotly_chart(fig, use_container_width=True)



# ! /////////////////////////////////////////////////////////

    st.subheader("Let’s analyze the clubs’ ratings based on the OVR of their players.")
    top_spending_club = cs.club_avg_rated_player().head(10)
    hover_cols = ['Team', 'Overall_Rating']  
    fig = px.bar(
        top_spending_club,
        x='Overall_Rating',
        y='Team',  
        orientation='h',
        color='Overall_Rating',
        hover_data=hover_cols, 
        
        
    )

    fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        xaxis_title='Overall_Rating',
        yaxis_title='Club Name',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        hoverlabel=dict(
        font_size=20,      # change this to your desired size
        font_family="Arial"
        )
    )

    fig.update_traces(
        text=top_spending_club['Overall_Rating'],
        textposition='outside'
    )

    st.plotly_chart(fig, use_container_width=True)
# ! /////////////////////////////////////////////////////////

    st.subheader("lets get an proper full info about club of your choice.")
    # 1. Create a larger, custom label using Markdown (using an HTML tag for precise control)
    st.markdown("<h3 style='margin-bottom: 0px;'>Enter the Club name</h3>", unsafe_allow_html=True)

    # 2. Render the text input, but hide its default label using label_visibility
    club_name = st.text_input(
        label="Club name hidden label", 
        value="type here...", 
        label_visibility="collapsed"
    )
    club_name1 = club_name.lower()
    club_name_final = club_name1.title()
    
    if st.button("submit"):       
        if club_name_final in cs.raw_data["Team"].values:
            df = cs.club_info(club_name_final)
           

            st.dataframe(
                df,use_container_width=True,
                height="auto",
                width='content',
                column_config={
                    "Total_Stats Score": st.column_config.Column(
                        "Goals",
                        help="No. of **GOALS** they scored"
                    ),
                    
                    "Value Per M$" : st.column_config.NumberColumn(
                        "Value",
                        help="Player Monthly Salary",
                        format="$%d Million"
                    ) 
                }
            )
          
        else:
            st.error("Name Not Found.")
# ! /////////////////////////////////////////////////////////

with tab3:
    a,b,c = st.columns(3)
    a.metric("**Total countries**", f"**{ca.countries()}**", border=True)
    b.metric("**Avg Player Earning**", f"**${ca.avg_player_earning()} Million**", border=True)
    c.metric("**Avg countries Rating**", f"**{ca.avg_rating()}**", border=True)

# ! /////////////////////////////////////////////////////////
st.subheader("**The top players produced by each country.**")
df = ca.top_country_player()
df["Name"] = df["Name"].apply(
    lambda x: ", ".join(x) if isinstance(x, list) else x
)

fig = px.scatter(
    df,
    x="Country",
    y="Overall_Rating",
    size="Overall_Rating",
    color="Overall_Rating",
    hover_name="Name",
)
fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        # xaxis_title='Country',
        # yaxis_title='Overall_Rating',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        hoverlabel=dict(
        font_size=20,      # change this to your desired size
        font_family="Arial"
        )
    )
    
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

# ! /////////////////////////////////////////////////////////

st.subheader("**Overall country ratings based on the players produced.**")
df = ca.top_countries_OVR()
hover_cols = ["Country", "avg_rating", "player_count", "strength_index"] 

fig = px.scatter(
    df,
    x="Country",
    y="avg_rating",
    size="avg_rating",
    color="avg_rating",
    hover_data=hover_cols,
)
fig.update_layout(
        yaxis={'categoryorder':'total ascending'},
        template='plotly_dark',
        height=500,
        # xaxis_title='Country',
        # yaxis_title='Overall_Rating',
        xaxis_tickfont_size=16,  # X-axis tick labels
        yaxis_tickfont_size=16,  # Y-axis tick labels
        xaxis_title_font_size=18, # X-axis title
        yaxis_title_font_size=18,  # Y-axis title
        hoverlabel=dict(
        font_size=20,      # change this to your desired size
        font_family="Arial"
        )
    )
    
fig.update_xaxes(tickangle=45)
st.plotly_chart(fig, use_container_width=True)

# ! /////////////////////////////////////////////////////////

st.subheader("**Country-wise Football Strength Analysis Across Positions.**")
df = ca.country_pos()
hover_cols = ["Country", "Forward", "Midfielder", "Defender", "Goalkeeper"] 
z