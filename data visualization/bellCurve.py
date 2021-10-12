import csv
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("data.csv")
counter=[]
height_list=df["Height(Inches)"].to_list()

#fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)
#fig.show()

#fig2=ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist=False)
#fig2.show()

mean=sum(height_list)/len(height_list)
print(mean)

std_deviation=statistics.stdev(height_list)
print(std_deviation)

median=statistics.median(height_list)
print(median)

mode=statistics.mode(height_list)
print(mode)

first_sd_start=mean-std_deviation
first_sd_end=mean+std_deviation

list_of_data_for_first_std=[result for result in height_list if result>first_sd_start and result<first_sd_end]
print("{}% of data lies within first standard deviation".format(len(list_of_data_for_first_std)*100/len(height_list)))

second_sd_start=mean-2*std_deviation
second_sd_end=mean+2*std_deviation

list_of_data_for_second_std=[result for result in height_list if result>second_sd_start and result<second_sd_end]
print("{}% of data lies within second standard deviation".format(len(list_of_data_for_second_std)*100/len(height_list)))

third_sd_start=mean-3*std_deviation
third_sd_end=mean+3*std_deviation

list_of_data_for_third_std=[result for result in height_list if result>third_sd_start and result<third_sd_end]
print("{}% of data lies within third standard deviation".format(len(list_of_data_for_third_std)*100/len(height_list)))