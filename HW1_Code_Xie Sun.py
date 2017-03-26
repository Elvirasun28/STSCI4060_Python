print 'STSCI 4060 HW1'
print 'Name: Sun Xie'
print 'NetID: sx226'
print
print '***** Question 1 *****\n'
print 'This program is to manipulate a string using format string, string method, and tuple.\n'

print 'A. Define a string variable, story, to hold the content of the story including its layout.\n'
story = 'Once upon a time, deep in an ancient\njungle, there lived a tiger. This tiger\nliked to eat fish, but the jungle had\nvery little fish to offer. One day, an\nexplorer found the tiger and discovered\nit liked fish. The explorer took the\ntiger back to NYC, where it could\neat as much fish as it wanted. However,\nthe tiger became homesick, so the\nexplorer brought it back to the jungle,\nleaving a large supply of fish.\n\n-- The End of the Story --\n';
print(story)

print 'B. Change the content of the story into a format string by replacing the words "tiger" and "fish" with a format symbol with the replace() string method.\n'
storyB = story.replace('tiger','%s').replace('fish','%s')
print(storyB)

print 'C. Create a tuple called "t1" to hold the words of "tiger" and "fish" so that the tuple can be used to restore the story to its original condition by using a string format operator (%). Display the story again to show if you have restored the story.\n'
t1 = ('tiger','tiger','fish','fish','tiger','fish','tiger','fish','tiger','fish')
story = storyB %t1
print(story)

print 'D. Now programmatically create a different version of the story by changing the animal and its food from "tiger" and "fish" to "monkey" and "bananas". You should go through similar steps from B to C.\n'
story = story.replace('tiger','%s').replace('fish','%s')
t2 = ('monkey','monkey','bananas','bananas','monkey','bananas','monkey','bananas','monkey','bananas')
storyD = story%t2
print(storyD)

print '***** Question 2 *****\n'
print'Using the final story created in Question1, write a program to use a format string and a dictionary to format and change the story.\n'

print 'A. Using the replace() method, replace the word "monkey" with "%(animal)s", "bananas" with "%(food)s", and NYC with "%(city)s ."\n'
storyD = storyD.replace('monkey','%(animal)s').replace('bananas','%(food)s').replace('NYC','%(city)s')

print 'B. Define a dictionary, myDict, to hold the following keys and values. The keys are animal, food, and city and the values are cat, mice and Beijing respectively. Display the dictionary by starting with "The dictionary is: " to confirm that myDict has been successfully created. Then, use the string format operator and apply the dictionary to the format string. Display the updated story.\n'
myDict = {'animal':'cat','food':'mice','city':'Beijing'}
print 'The dictionary is: ', myDict
print
newStory = storyD %myDict
print(newStory)

print 'C. Using assignment statements ONLY, update the dictionary values with the values of "fox", "rabbits", and "London" respectively, and then display the updated dictionary and the story after you have applied the updated dictionary to the format string.\n'
myDict['animal'] = 'fox'
myDict['food'] = 'rabbits'
myDict['city']='London'
print 'The updated dictionary is: ', myDict
print
newStory2 = storyD %myDict
print(newStory2)

print '***** Question 3 *****\n'
print '3. Write a program to calculate the dot product of two vectors (review your Linear Algebra notes for the definition of dot product of the n-vectors if needed). Lists can be used to represent n-vectors. Suppose you have two 4-vectors u and v below\n'
u = [1,-2,3,4]
v = [2,3,-2,1]
print 'The list representation of vector u is ',u
print
print 'The list representation of vector v is ',v
print
result = 0
for i in range(0,len(u)):
    result += u[i] * v[i]
    

print'The dot product u*v is ', result

    





