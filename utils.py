def write_results_to_csv_file(text):
    with open('result.csv','wb') as file:
        for line in text:
            file.write(line)
            file.write('\n')