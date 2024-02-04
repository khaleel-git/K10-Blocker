# Replace 'bad_words.txt' with the path to your keyword file
keyword_occean = {}
single_keyword_occean = {}
keyword_file_path = 'C:\\Users\\emahkah\\OneDrive - Ericsson\\Documents\\GitHub\\Khaleel_Por_Blocker\\lists\\'
for folder in os.listdir(keyword_file_path):
    print(f"folder: {folder}")
    for file in os.listdir(keyword_file_path + folder):
        with open(keyword_file_path + folder + "\\" + file, "r") as read:
            for line in read:
                keyword = line.strip()
                # Get the first letter of the keyword
                first_letter = keyword[0].lower()
                if ' ' not in keyword and "." not in keyword and len(keyword.split()) == 1:
                    if first_letter not in single_keyword_occean:
                        single_keyword_occean[first_letter] = set()
                    single_keyword_occean[first_letter].add(keyword)
                    continue  # Skip single-word keywords
                
                if first_letter not in keyword_occean:
                    keyword_occean[first_letter] = set()
                keyword_occean[first_letter].add(keyword)

# # Convert set to lists
# for key, value in single_keyword_occean.items():
#     single_keyword_occean[key] = list(value)
# # Save the keyword_occean dictionary to a JSON file
# with open("single_bad_keywords_cloud.json", "w") as fd:
#     json.dump(single_keyword_occean, fd, indent=4)
# # Convert set to lists
# for key, value in keyword_occean.items():
#     keyword_occean[key] = list(value)
# # Save the keyword_occean dictionary to a JSON file
# with open("bad_keywords_cloud.json", "w") as fd:
#     json.dump(keyword_occean, fd, indent=4)