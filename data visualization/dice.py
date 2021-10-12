import random
import plotly_express as px
import plotly.figure_factory as ff
import statistics

counter=[]
sum1=[]

for i in range(1,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum1.append(dice1+ dice2)
    counter.append(i)

mean=sum(sum1)/len(sum1)
print(mean)

std_deviation=statistics.stdev(sum1)
print(std_deviation)

median=statistics.median(sum1)
print(median)

mode=statistics.mode(sum1)
print(mode)

first_sd_start=mean-std_deviation
first_sd_end=mean+std_deviation

list_of_data_for_first_std=[result for result in sum1 if result>first_sd_start and result<first_sd_end]
print("{}% of data lies within first standard deviation".format(len(list_of_data_for_first_std)*100/len(sum1)))

second_sd_start=mean-2*std_deviation
second_sd_end=mean+2*std_deviation

list_of_data_for_second_std=[result for result in sum1 if result>second_sd_start and result<second_sd_end]
print("{}% of data lies within second standard deviation".format(len(list_of_data_for_second_std)*100/len(sum1)))

third_sd_start=mean-3*std_deviation
third_sd_end=mean+3*std_deviation

list_of_data_for_third_std=[result for result in sum1 if result>third_sd_start and result<third_sd_end]
print("{}% of data lies within third standard deviation".format(len(list_of_data_for_third_std)*100/len(sum1)))

#fig=px.bar(x=sum, y=counter)
#fig.show()

#fig2=ff.create_distplot([sum1], ["result"])
#fig2.show()