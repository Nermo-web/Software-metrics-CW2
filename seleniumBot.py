from selenium import webdriver
import json

metrics_values = {}  # Dictionary for getting total values of metrics duration respective to url. Its scope is global
with open("Output_metrics.txt", "w") as outfile: # opening a output_metrics.txt file where output of url and duration is save

    chromebrowser = webdriver.Chrome("D:\Metrics Assignment\PerformanceData\drivers\chromedriver.exe") # webdriver of chrome is used

    for metric in range(10): #loop upto 10 times for getting metrics

        chromebrowser.get("https://en.wikipedia.org/wiki/Software_metric") #loading url
        metrics = chromebrowser.execute_script("return window.performance.getEntries()") #javascript command to get metrics entries

        for m in metrics: # nested loop to get values of name as url and duration in a single metrics

            url = m["name"] #getting name from metrics
            metrics_list = metrics_values.get(url, [])
            metrics_list.append(m["duration"]) # get duration of metrics
            metrics_values[url] = metrics_list
            outfile.write(f"{m['name']}, {m['duration']}\n")

            '''
            above is the logic to get values in dictionary for further calculations
            values are also written in Output_metrics.txt file
            '''

with open("average_duration.csv", "w") as avg_file:    # opening csv file and writing average in it along with url which is key and value is duration

    for key, value in metrics_values.items():   # loop for get each item of dictionary metrics values

        average_duration = sum(value) / len(metrics_values) # calculating average by sum of all values and divide it with lenght of dictionary metric value
        avg_file.write(f"{key}, {average_duration}\n") # writing in csv file.

with open("final_json_file" + ".json", "w", encoding="utf-8") as json_file: # writing data in json file

    json.dump(metrics, json_file, ensure_ascii=False, indent=4)  # dump method to put data in json file.

chromebrowser.quit() # closing browser