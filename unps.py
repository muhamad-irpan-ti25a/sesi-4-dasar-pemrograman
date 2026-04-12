words = "UNIVERSITAS NUSA PUTRA SUKABUMI"

#a putra nusa
split_words = words.split() 
print("a. ", split_words[2].lower(), split_words[1].lower())

#b NIVERSITAS NSA PTRA SKABMI
print("b. ",words.replace("U",""))

#c SUKABUMI PUTRA NUSA UNIVERSITAS
print("c. ", split_words[3], split_words[2], split_words[1], split_words[0])

#d UNPS
print("d. ", words.split()[0][0] + words.split()[1][0] + words.split()[2][0] + words.split()[3][0])

#e TAS SAPU BUMI
print("e. ", words.split()[0][-3:], words.split()[1][-2:] + words.split()[2][:2], words.split()[3][-4:] )