def separate_messages(file_name):
    file = open(file_name, "r+", encoding='utf-8')
    lines_data = file.readlines()
    flow = []
    for current_line in lines_data:
        current_line = current_line.replace(",", "")
        current_line = current_line.replace("#", ",")
        current_line = current_line.strip('\n')
        flow.append(current_line.split(";"))

    file.close()
    return flow 

# print(separate_messages('messages.csv'))