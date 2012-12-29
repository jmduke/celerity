import json
import os
import sys
import urllib2

FILE_DELINEATOR = '!!**!!' # gross, I know.
HASTE_URL = 'http://hastebin.com/'
POST_URL = HASTE_URL + 'documents/'
GET_URL = HASTE_URL + 'raw/'

# Return codes
SUCCESSFUL_ACTION = 1
IMPROPER_FILE_ERROR = 2
FILE_CREATION_ERROR = 3

# given a list of files:
# 1. Open the files and retrieve the contents
# 2. Upload those contents to hastebin.
# 3. Return the URL identifier.
def upload(args):
	
	# if we're supplied filenames, we open them
	if len(args) > 0:
		contents = parse_files(args)
		
	# otherwise, we check STDIN
	else:
		contents = {'piped.txt': sys.stdin.read()}
		
	hastebin_key = post_contents(contents)
	return hastebin_key
	
# given a hastebin URL:
# 1. Retrieve the contents of the URL
# 2. Write the contents to file.
def download(args):
	url = args[0]
	target = './'
	if len(args) > 1:
		target = args[1]
		
		# weird edge case
		if target[-1] != '/':
			target += '/'
	
	contents = get_contents(url)
	successful_files = write_files(contents, target)
	return successful_files

# given a list of local files,
# returns a dictionary of filenames and their contents
def parse_files(filenames):
	try:
		contents = {file: open(file).read() for file in filenames}
	
	# The main thing that I've ran into is file not existing	
	except IOError:
		return IMPROPER_FILE_ERROR
		
	return contents
	
# given a directory of filenames and contents,
# write them to disk
def write_files(contents, target):
	successful_files = []
	
	for file_name in contents:
		file_content = contents[file_name]
		file_pointer = open(target + file_name, 'w')
		file_pointer.write(file_content)
		file_pointer.close()
		successful_files.append(file_name)
	
	return successful_files
	
	
# post file to hastebin.
# returns hastebin_key if successful;
# returns error code otherwise
def post_contents(contents):
	payload = ''
	for header in contents:
		payload += '\n' + FILE_DELINEATOR + header + FILE_DELINEATOR + '\n'
		payload += contents[header]
		
	# Get rid of newline char at beginning of payload due to l.22
	payload = payload[1:]
		
	request = urllib2.Request(POST_URL, payload)
	response = urllib2.urlopen(request).read()
	hastebin_key = json.loads(response)['key']
	return hastebin_key

# downloads files from a given hastebin key
# returns a dictionary of contents
# returns error code otherwise	
def get_contents(url):
	request = urllib2.Request(GET_URL + url)
	response = urllib2.urlopen(request)
	fulltext = response.read()
	
	# Parse the response for separate files, creating a dictionary of the results.
	unsorted_contents = fulltext.split(FILE_DELINEATOR)
	unsorted_contents = unsorted_contents[1:]
	number_of_files = len(unsorted_contents) / 2
	contents = {}
	for file_index in range(number_of_files):
		file_name = unsorted_contents[file_index * 2]
		file_content = unsorted_contents[file_index * 2 + 1][1:]
		contents[file_name] = file_content
	
	return contents		

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	if len(sys.argv) < 2:
		print 'Usage:'
		print 'celerity post <filename>'
		print 'celerity get <url> [target folder]'
		return 0
	

	else:
		command = sys.argv[1]
		signifier = sys.argv[2:]
		
		result = actions = {
			'post': upload,
			'get': download
		}[command](signifier)
		
		if result == IMPROPER_FILE_ERROR:
			print "Unable to upload file. Be sure to make sure it exists!"
			return 0
		elif result == FILE_CREATION_ERROR:
			print "Able to download file but not write it to disk."
			return 0
		else:
			print "Success!"
			print result
			return 1