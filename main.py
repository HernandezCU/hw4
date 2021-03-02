# The Solar Project - (Because its not warm enough outside to be speaking about solar power)
#  You will submit this project individually but work collaboratively. You will also be graded as a team meaning
#  if 1 member does not submit the code to their repository, and response on blackboard
#  but the other 3 team members do both parts perfectly. The final grade project will be a 75% for everyone.
#
#  Black Board Submission
#    Submit a review of each member of the as part of the blackboard submission.
#    1. I am not expecting much here, just 2 or 3 sentences reviewing each team member.
#    2. What did you enjoy about the project?
#    3. What did you not enjoy?

#  Code Submission:
#    Use the data set for creating  /data/756874_system_power_20210207.csv
#    Required functions in the git repository are below and should be located under /homework/hw3.py
from typing import List, Tuple
from datetime import datetime
from typing import Dict


def read_solar_data(p: str = None) -> List[Tuple[datetime, float]]:
    ret = []
    with open(
        "756874_system_power_20210221.csv",
        "r",
    ) as fp:
        data = fp.readlines()
    for idx, row in enumerate(data):
        if idx == 0:
            continue
        date, power = row.split(",")
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S %z")
        ret.append((date, float(power)))
    return ret


def trunc_datetime(dt: datetime):
    return dt.replace(minute=0, second=0, microsecond=0, tzinfo=None)


def round_to_30_minutes(dt: datetime):
    if dt.minute >= 30:
        return dt.replace(minute=30)
    return dt.replace(minute=0)


def hourly_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    ret = {}
    for date, power in data:
        date = trunc_datetime(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power

    return ret


def thirty_minute_demand_summary( data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    ret = {}
    for date, power in data:
        date = round_to_30_minutes(date)
        if date in ret:
            ret[date] += power
        else:
            ret[date] = power

    return ret


def daily_demand_summary(data: List[Tuple[datetime, float]]) -> Dict[datetime, float]:
    daily_totals = {}
    current_day = data[0][0].day
    current_datetime = data[0][0]
    daily_total = 0
    for date, power in data:
        if date.day == current_day:
            daily_total += power
        else:
            daily_totals.update({current_datetime: daily_total})
            current_datetime = date
            current_day = date.day
            daily_total = 0
    return daily_totals


def weekly_power_summary(data: List[Tuple[datetime, float]]) ->List[Tuple[datetime,float]]:
  d = []
  p = []

  for date, power in data:
    d.append(date)
    p.append(power)

  t = sum(p)
  tup = (datetime(2021, 2, 21), t);
  return tup


def maximum_hourly_data(data: List[Tuple[datetime,float]]) -> datetime:
  ret = {}
  for date, power in data:
    date = trunc_datetime(date)
    if date in ret:
        ret[date] += power
    else:
        ret[date] = power

  values = list(ret.values())
  keys = list(ret.keys())
  m = max(values)
  i = values.index(m)

  return keys[i]
  
  
def max_average_power_produced(data: List[Tuple[datetime,float]]) ->Tuple[datetime, float]:
  d = []
  p = []
  for datex, power in data:
    d.append(datex)
    p.append(power)
  
  l = max(p)
  idx = p.index(int(l))
  tup = (d[idx], l);
  return tup


if __name__ == "__main__":
    max_average_power_produced(read_solar_data())
    maximum_hourly_data(read_solar_data())
    weekly_power_summary(read_solar_data())
    daily_demand_summary(read_solar_data())
    thirty_minute_demand_summary(read_solar_data())
    hourly_demand_summary(read_solar_data())