#{new_key:new_value for (index,row) in student_data_frame.iterrows()}
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index,row) in df.iterrows()}
# print(nato_dict.keys())
# print(nato_dict.values())
def generate_phonetic():
    name = input("Enter a word: ")
    try:
        nato_list = [nato_dict[key.upper()] for key in name]
    except KeyError:
        print("Sorry ,Only letters are allowed")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()