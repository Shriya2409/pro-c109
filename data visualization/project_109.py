import statistics
import csv
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
score_list=df["math score"].to_list()

mean=sum(score_list)/len(score_list)
print(mean)

std_deviation=statistics.stdev(score_list)
print(std_deviation)

median=statistics.median(score_list)
print(median)

mode=statistics.mode(score_list)
print(mode)

first_sd_start=mean-std_deviation
first_sd_end=mean+std_deviation

list_of_data_for_first_std=[result for result in score_list if result>first_sd_start and result<first_sd_end]
print("{}% of data lies within first standard deviation".format(len(list_of_data_for_first_std)*100/len(score_list)))

second_sd_start=mean-2*std_deviation
second_sd_end=mean+2*std_deviation

list_of_data_for_second_std=[result for result in score_list if result>second_sd_start and result<second_sd_end]
print("{}% of data lies within second standard deviation".format(len(list_of_data_for_second_std)*100/len(score_list)))

third_sd_start=mean-3*std_deviation
third_sd_end=mean+3*std_deviation

list_of_data_for_third_std=[result for result in score_list if result>third_sd_start and result<third_sd_end]
print("{}% of data lies within third standard deviation".format(len(list_of_data_for_third_std)*100/len(score_list)))