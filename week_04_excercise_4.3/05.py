def reset_dict(dict):
    
    for k, v in dict.items():
        dict.pop(k)
    print(dict)
    # return cleared_dict


color_dict = reset_dict({"Name": [], "Address": [], "Age": []})
Learn
