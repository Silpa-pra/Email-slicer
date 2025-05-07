def main():
    num_tokens = []
    str_tokens = []
    user_data = input("Insert Delimited Data: ")
    split_data = user_data.split(sep = "|")
    for i in split_data:
        if i.strip().isnumeric():
            num_tokens.append(i)
        else:
            str_tokens.append(i)

    print("String Tokens: {} \nNumeric Token: {}".format(len(str_tokens), len(num_tokens))) 

    return

main()