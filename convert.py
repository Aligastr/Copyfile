import csv

with open('TAPE.csv', encoding="utf-8") as csv_file:
    for row in csv_file:
        splited = row.split(';')
        with open('text_text_allHDD.csv', encoding="utf-8") as csv_file2:
            for row2 in csv_file2:
                if splited[1] in row2:
                    print(splited) # print dublicates


        #for row2 in csv_file2:
            #    name2, path2, size2, tape2 = row2.split(';')
            #    #print(row2)                      #All HDD = row2
            #    if path != path2: #not in row2 and size not in row2:
            #    #if path not in row2 and size not in row2:
            #        #with open('duplicates.csv', 'a', encoding="utf-8") as dubl:
            #        #    a = []
            #        #    a.append(splited)
            #        #    dubl.write(";".join(a))
            #        #    dubl.write('\n')
            #        print('1', path)
            #        print('2', path2)
            #        pass


Neue

import csv

dict1 = dict()
dict2 = dict()
with open('text_text_allHDD.csv', encoding="utf-8") as csv_file:
    for row in csv_file:                                #Tape = row
        name, path, size, device = row.split(';')          #splited = [tape, tape, tape, tape]
        dict1[path] = (name, size, device)
        

            
with open('TAPE.csv', encoding="utf-8") as csv_file2:      
    for row in csv_file2:                                #Tape = row
        name, path, size, device = row.split(';')          #splited = [tape, tape, tape, tape]
        dict2[path] = (name, size, device)


print("dict1", len(dict1))
print("dict2", len(dict2))

antidub = list()
dub = list()
for key, values in dict1.items():    
    if key not in dict2:
        antidub.append(key)
    else:
        dub.append((key, values[1]))

print(len(antidub))
print(len(dub))

# size check
for elem in dub:
    key = elem[0]
    size = elem[1]
    if dict2[key][1] != size:
        print("size fiffers", key)

