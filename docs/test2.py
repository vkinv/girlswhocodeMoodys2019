import school_scores
list_of_record = school_scores.get_all()
print(list_of_record[0])

#subdata = (list_of_record[0])
for data in list_of_record:
    # print("States:", data["State"]["Name"],"year:", data["Year"])
     print("Test-Takers", data["Gender"]["Female"]["Test-takers"])
