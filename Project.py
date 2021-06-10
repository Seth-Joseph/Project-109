import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics as st

df = pd.read_csv('StudentsPerformance.csv')
fig = ff.create_distplot([df['reading score']],['reading score'],show_hist = False,curve_type = 'normal'  )
fig.show()

reading_list = df['reading score'].tolist()
writing_list = df['writing score'].tolist()

reading_mean = st.mean(reading_list)
writing_mean = st.mean(writing_list)

reading_mode = st.mode(reading_list)
writing_mode = st.mode(writing_list)

reading_median = st.median(reading_list)
writing_median = st.median(writing_list)

print('Mean,Mode,Median of Height is {},{},{}'.format(reading_mean,reading_mode,reading_median))
print('Mean,Mode,Median of Weight is {},{},{}'.format(writing_mean,writing_mode,writing_median))

reading_stdev = st.stdev(reading_list)
writing_stdev = st.stdev(writing_list)

reading_first_stdev_start,reading_first_stdev_end = reading_mean - reading_stdev,reading_mean - reading_stdev
reading_second_stdev_start,reading_second_stdev_end = reading_mean - (2*reading_stdev),reading_mean - (2*reading_stdev)
reading_third_stdev_start,reading_third_stdev_end = reading_mean - (3*reading_stdev),reading_mean - (3*reading_stdev)

writing_first_stdev_start,writing_first_stdev_end = writing_mean- writing_stdev,writing_mean - writing_stdev
writing_second_stdev_start,writing_second_stdev_end = writing_mean - (2*writing_stdev),writing_mean - (2*writing_stdev)
writing_third_stdev_start,writing_third_stdev_end = writing_mean - (3*writing_stdev),writing_mean - (3*writing_stdev)

reading_list_of_data_within_1_std_deviation = [result for result in reading_list if result > reading_first_stdev_start and result > reading_first_stdev_end]
reading_list_of_data_within_2_std_deviation = [result for result in reading_list if result > reading_second_stdev_start and result > reading_second_stdev_end]
reading_list_of_data_within_3_std_deviation = [result for result in reading_list if result > reading_third_stdev_start and result > reading_third_stdev_end]

writing_list_of_data_within_1_std_deviation = [result for result in writing_list if result > writing_first_stdev_start and result > writing_first_stdev_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result > writing_second_stdev_start and result > writing_second_stdev_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_list if result > writing_third_stdev_start and result > writing_third_stdev_end]

print('{}% data of reading within 1 standard deviation'.format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(reading_list)))
print('{}% data of reading within 2 standard deviation'.format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(reading_list)))
print('{}% data of reading within 3 standard deviation'.format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(reading_list)))
print('{}% data of writing within 1 standard deviation'.format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_list)))
print('{}% data of writing within 2 standard deviation'.format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_list)))
print('{}% data of writing within 3 standard deviation'.format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_list)))


