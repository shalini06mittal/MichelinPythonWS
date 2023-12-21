'''
1. read contents from the file
2. display message as follows:
Man says : 'Is this the right room for an argument? '
Other Man says : 'I've told you once.'
3. handle for the sentences that coonot be split on : and
just skip those sentences
'''
data = open('script.txt')
for each_line in data:
	try:
		(role, line_spoken) = each_line.split(':')
		print(role, end='')
		print(' says: ', end='') 
		print(line_spoken, end='')
	except:
		pass 