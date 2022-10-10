import pandas as pd
import random
from itertools import combinations

week = "Week X"
date = "11/30"
weekday = "Monday"
team_a = "Mighty Bruins"
team_b = "Cranky Cal"
tipoff = "18:00"

season_schedule = pd.DataFrame(
    {
        "Week": ["{}".format(week)],
        "Date": ["{}".format(date)],
        "Weekday": ["{}".format(weekday)],
        "Home": ["{}".format(team_a)],
        "Away": ["{}".format(team_b)],
        "Game Time": ["{}".format(tipoff)],
    }
)
season_schedule.drop(season_schedule.tail(1).index, inplace=True)


def tipoff_bynight(team_a, team_b):
    dup_team_a = team_a.copy()
    dup_team_b = team_b.copy()

    del dup_team_a["Name"]
    del dup_team_b["Name"]

    teams = [dup_team_a, team_b]
    keys = list(dup_team_a)

    res_2 = {}

    for key in keys:
        temp_res = []
        res = []
        res_1_1 = []
        for team in teams:
            for time_slot in team[key]:
                if time_slot in temp_res:
                    res.append(time_slot)
                else:
                    temp_res.append(time_slot)
            res_2[key] = res
            if len(res) > 1:
                b = random.randint(0, len(res) - 1)
                res_1_1.append(res[b])
                res_2[key] = res_1_1

    if res_2 == {}:
        print(
            "{} and {} do not have overlap in scheduling".format(dup_team_a, dup_team_b)
        )

    res_2_dup = res_2.copy()

    for key in keys:
        if res_2_dup[key] == ["null"]:
            del res_2[key]
        elif res_2_dup[key] == []:
            del res_2[key]

    res_3 = res_2.copy()

    new_keys = list(res_3)
    res_4 = {}

    if len(res_3) != 1:
        a = random.randint(0, len(res_3) - 1)
        res_4[new_keys[a]] = res_3[new_keys[a]].copy()
    else:
        res_4 = res_3.copy()

    return res_4


def what_week(team_a_name, team_b_name):
    this_week = "Week 10"

    if season_schedule.empty:
        this_week = "Week 1"
    else:
        for i in range(1, 11):
            q = season_schedule.loc[
                season_schedule["Week"] == "Week {}".format(i), "Home"
            ].tolist()
            p = season_schedule.loc[
                season_schedule["Week"] == "Week {}".format(i), "Away"
            ].tolist()

            res = any(team_a_name == ele for ele in q)
            res_2 = any(team_b_name == ele for ele in q)
            res_3 = any(team_a_name == ele for ele in p)
            res_4 = any(team_b_name == ele for ele in p)

            if res == True or res_2 == True or res_3 == True or res_4 == True:
                pass
            else:
                this_week = "Week {}".format(i)
                break

    return this_week


def what_date(week, weekday):
    q1_mon = {
        "Week 1": "09/26",
        "Week 2": "10/03",
        "Week 3": "10/10",
        "Week 4": "10/17",
        "Week 5": "10/24",
        "Week 6": "10/31",
        "Week 7": "11/07",
        "Week 8": "11/14",
        "Week 9": "11/21",
        "Week 10": "11/28",
    }
    q1_tues = {
        "Week 1": "09/27",
        "Week 2": "10/04",
        "Week 3": "10/11",
        "Week 4": "10/18",
        "Week 5": "10/25",
        "Week 6": "11/01",
        "Week 7": "11/08",
        "Week 8": "11/15",
        "Week 9": "11/22",
        "Week 10": "11/29",
    }
    q1_wed = {
        "Week 1": "09/28",
        "Week 2": "10/05",
        "Week 3": "10/12",
        "Week 4": "10/19",
        "Week 5": "10/26",
        "Week 6": "11/02",
        "Week 7": "11/09",
        "Week 8": "11/16",
        "Week 9": "11/23",
        "Week 10": "11/30",
    }
    q1_thurs = {
        "Week 1": "09/29",
        "Week 2": "10/06",
        "Week 3": "10/13",
        "Week 4": "10/20",
        "Week 5": "10/27",
        "Week 6": "11/03",
        "Week 7": "11/10",
        "Week 8": "11/17",
        "Week 9": "11/24",
        "Week 10": "12/01",
    }
    q1_fri = {
        "Week 1": "09/30",
        "Week 2": "10/07",
        "Week 3": "10/14",
        "Week 4": "10/21",
        "Week 5": "10/28",
        "Week 6": "11/04",
        "Week 7": "11/11",
        "Week 8": "11/18",
        "Week 9": "11/25",
        "Week 10": "12/02",
    }

    date = "error"

    if weekday == "Monday":
        date = q1_mon[week]
    elif weekday == "Tuesday":
        date = q1_tues[week]
    elif weekday == "Wednesday":
        date = q1_wed[week]
    elif weekday == "Thursday":
        date = q1_thurs[week]
    elif weekday == "Friday":
        date = q1_fri[week]

    return date


def add_game(team_a, team_b):
    team_a_name = team_a["Name"]
    team_b_name = team_b["Name"]

    entry = tipoff_bynight(team_a, team_b)
    key = list(entry)

    week = what_week(team_a_name, team_b_name)
    weekday = key[0]
    date = what_date(week, weekday)
    tip_off = (
        str(entry[key[0]]).replace("['", "").replace("-", ":00 - ").replace("']", ":00")
    )

    season_schedule.loc[len(season_schedule.index)] = [
        week,
        date,
        weekday,
        team_a_name,
        team_b_name,
        tip_off,
    ]

    return season_schedule


def optimized_season_schedule(team_a, team_b, team_c, team_d):
    all_team_names = [team_a["Name"], team_b["Name"], team_c["Name"], team_d["Name"]]
    index = {
        "Mighty Bruins": team_a,
        "Cranky Cal": team_b,
        "Tacky Trojans": team_c,
        "Silly Stanford": team_d,
    }

    combs = list(combinations(all_team_names, 2))

    for i in range(len(combs)):
        a = random.randint(0, 1)
        if a == 0:
            add_game(index[combs[i][0]], index[combs[i][1]])
        elif a == 1:
            add_game(index[combs[i][1]], index[combs[i][0]])

    return season_schedule.sort_values(by="Date").to_string(index=False)


team_1 = {
    "Name": "Mighty Bruins",
    "Monday": ["3-4", "5-6", "6-7"],
    "Tuesday": ["4-5"],
    "Wednesday": ["null"],
    "Thursday": ["null"],
    "Friday": ["8-9"],
}
team_2 = {
    "Name": "Cranky Cal",
    "Monday": ["2-3", "5-6", "7-8"],
    "Tuesday": ["4-5", "5-6"],
    "Wednesday": ["null"],
    "Thursday": ["null"],
    "Friday": ["null"],
}
team_3 = {
    "Name": "Tacky Trojans",
    "Monday": ["3-4", "null"],
    "Tuesday": ["4-5", "null"],
    "Wednesday": ["4-5"],
    "Thursday": ["6-7"],
    "Friday": ["null"],
}
team_4 = {
    "Name": "Silly Stanford",
    "Monday": ["2-3", "7-8", "null"],
    "Tuesday": ["5-6", "null"],
    "Wednesday": ["4-5"],
    "Thursday": ["6-7"],
    "Friday": ["8-9"],
}

print(optimized_season_schedule(team_1, team_2, team_3, team_4))
