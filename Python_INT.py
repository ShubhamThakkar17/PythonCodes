runs_vk = ['ODI-13776','T20-2905','TEST-8416', 'IPL-5586']
teams_vk = ['INDIA','RCB']
runs_msd = ['ODI-10773','T20-1617','TEST-4876', 'IPL-5082']
teams_msd = ['INDIA', 'CSK']
runs_st = ['ODI-18426','T20-10','TEST-15921', 'IPL-2334']
teams_st = ['INDIA', 'MI']
runs_abd = ['ODI-9577','T20-1672','TEST-8765', 'IPL-5162']
teams_abd = ['SOUTH AFRICA', 'RCB']
runs_cg = ['ODI-10480','T20-1899','TEST-7214', 'IPL-4965']
teams_cg = ['WEST INDIES', 'RCB', 'KXIP']
cricket_players = {
    'Virat Kohli':{'Teams Played': teams_vk, 'Runs':runs_vk},
    'MS Dhoni':{'Teams Played': teams_msd, 'Runs':runs_msd},
    'Sachin Tendulkar':{'Teams Played': teams_st, 'Runs':runs_st},
    'AB DeVilliers':{'Teams Played': teams_abd, 'Runs':runs_abd},
    'Chris Gayle':{'Teams Played': teams_cg, 'Runs':runs_cg}
}
print(cricket_players)