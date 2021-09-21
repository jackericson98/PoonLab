"""The point of this code is to allow you to copy and paste the integration data from POKY into the data file and then
receive the data it contains (chemical shifts, line widths, volume, % error?)"""


from data import *

"""This function filters out the string Fit group of _ peaks."""


def clean_data(raw_str):
    clean_str = raw_str.replace("Fit group of 2 peaks.", '')
    clean_str = clean_str.replace("Fit group of 4 peaks.", '')
    return clean_str


"This function takes each peak and returns a volume value for each data point"


def interpret_vol(peak_data):
    index1 = peak_data.find('vol')
    index2 = peak_data.find('rms')
    vol = float(peak_data[index1 + 3:index2])
    return vol


"This function takes each peak and returns a peak value for each data point"


def interpret_peaks(peak_data):
    index1a = peak_data.find('@') + 2
    index1b = peak_data.find(' ', 7, 17)
    w1 = float(peak_data[index1a: index1b])
    index2a = index1b + 1
    index2b = index2a + 6
    w2 = float(peak_data[index2a:index2b])
    return w1, w2


"""This function takes all of the data and separates it into an array of strings. You need to copy and paste the 
first set twice bug """


def separate(my_str):
    data_array = []
    len_between_ps = 0
    str_num = 0
    for char in my_str:
        if char == 'p':
            data_array.append(my_str[str_num - len_between_ps - 1:str_num])
            len_between_ps = 0
        else:
            len_between_ps = len_between_ps + 1
        str_num = str_num + 1
    del data_array[0]
    return data_array


"""This function takes the entire data set and returns an array of volume data points"""


def interpret_all_vol(data_str):
    vol_array = []
    clean_data_str = clean_data(data_str)
    separated_data_str = separate(clean_data_str)
    for element in separated_data_str:
        vol_array.append(interpret_vol(element))
    return vol_array


"""This function takes the entire data set and returns 2 arrays of w1 and w2 chemical shift data points"""


def interpret_all_peaks(dataset):
    peak1_array = []
    peak2_array = []
    clean_data_str = clean_data(dataset)
    sep_clean_data = separate(clean_data_str)
    for element in sep_clean_data:
        w1, w2 = interpret_peaks(element)
        peak1_array.append(w1)
        peak2_array.append(w2)

    return peak1_array, peak2_array


w1 = interpret_all_peaks(data)[0]
w2 = interpret_all_peaks(data)[1]
vol = interpret_all_vol(data)


