'''
PLEASE TRY THIS JOSH - maybe txblob will help!!! :)
try making model that fills in an part of speech sequence with Obama terms
steps:
1. find common pos sequences either from tagging Obama sequences or online
2. for each tag, store Obama words with that pos tag
3. when generating sentence, go through pos tag sequence and at each step pick
a word with that pos tag (ideally weighed more heavily based on topic)

we can compare this model to our markov n-gram model
'''
