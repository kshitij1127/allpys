import random
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

diceresult = []
count = []
for i in range(0, 100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1 + dice2)
    count.append(i)

mean = sum(diceresult) / len(diceresult)
std = statistics.stdev(diceresult)
median = statistics.median(diceresult)
mode = statistics.mode(diceresult)
print(mean, std, median, mode)

first_Std_Start, first_Std_End = mean - std, mean + std
second_std_start, second_std_end = mean - (2*std), mean + (2*std)
third_std_start, third_std_end = mean - (3*std), mean + (3*std)
list_of_data_within_1_std_deviation = [result for result in diceresult if result > first_Std_Start and result < first_Std_End]
list_of_data_within_2_std_deviation = [result for result in diceresult if result > second_std_start and result < second_std_end]
list_of_data_within_3_std_deviation = [result for result in diceresult if result > third_std_start and result < third_std_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(diceresult)))
print("{}% of data lies between the second standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(diceresult)))
print("{}% of data lies between third standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(diceresult)))

fig = ff.create_distplot([diceresult], ["result"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode="lines", name="mean",))
fig.add_trace(go.Scatter(x = [first_Std_Start, first_Std_Start], y = [0, 0.17], mode="lines", name="standard deviation 1"))
fig.add_trace(go.Scatter(x = [first_Std_End, first_Std_End], y = [0, 0.17], mode="lines", name="standard deviation 1"))
fig.add_trace(go.Scatter(x = [second_std_start, second_std_start], y = [0, 0.17], mode="lines", name="standard deviation 2"))
fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0, 0.17], mode="lines", name="standard deviation 2"))
fig.add_trace(go.Scatter(x = [third_std_start, third_std_start], y = [0, 0.17], mode="lines", name="standard deviation 3"))
fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0, 0.17], mode="lines", name="standard deviation 3"))

fig.show()


# mean median mode are almost same in a standard data distribution
