def seconds_to_human(full_sec):
    ans_time_list = []
    if not full_sec:
        return "now"
    seconds = full_sec % 60
    if seconds:
        ans_time_list.append(("seconds" if seconds - 1 else "second", seconds))
    full_sec = full_sec // 60

    minutes = full_sec % 60
    if minutes:
        ans_time_list.append(("minutes" if minutes - 1 else "minute", minutes))
    full_sec = full_sec // 60

    hours = full_sec % 24
    if hours:
        ans_time_list.append(("hours" if hours - 1 else "hour", hours))
    full_sec = full_sec // 24

    days = full_sec % 365
    if days:
        ans_time_list.append(("days" if days - 1 else "day", days))
    years = full_sec // 365
    if years:
        ans_time_list.append(("years" if years - 1 else "year", years))
    ans = ""
    for i, count in enumerate(ans_time_list):
        addition_phrase = ""
        if i == 1:
            addition_phrase = " and "
        if i > 1:
            addition_phrase = ", "
        ans = f'{count[1]} {count[0]}' + addition_phrase + ans
    return ans


# seconds_to_human(1231214)
full_sec = 61
ans_time_list = []


seconds = full_sec % 60
if seconds:
    ans_time_list.append(("seconds" if seconds - 1 else "second", seconds))
full_sec = full_sec // 60

minutes = full_sec % 60
if minutes:
    ans_time_list.append(("minutes" if minutes - 1 else "minute", minutes))
full_sec = full_sec // 60

hours = full_sec % 24
if hours:
    ans_time_list.append(("hours" if hours - 1 else "hour", hours))
full_sec = full_sec // 24

days = full_sec % 365
if days:
    ans_time_list.append(("days" if days - 1 else "day", days))
years = full_sec // 365
if years:
    ans_time_list.append(("years" if years - 1 else "years", years))
ans = ""
for i, count in enumerate(ans_time_list):
    addition_phrase = ""
    if i == 1:
        addition_phrase = " and "
    if i > 1:
        addition_phrase = ", "
    ans = f'{count[1]} {count[0]}' +addition_phrase+ ans

