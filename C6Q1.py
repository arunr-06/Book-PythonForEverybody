# extracting portion of a string

dump = 'X-DSPAM-Confidence:0.8475'
position = dump.find(':')
print(position)
extracted = dump[position+1:]
print(extracted)
