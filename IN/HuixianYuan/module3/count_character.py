import pprint

message="""Peter picked a peck of pickled peppers
           A peck of pickled pepers Peter Piper 
           If Peter Piper picked a peck of pickled pepers
           where's the peck of pickled pepers Peter Piper picked?"""

count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)