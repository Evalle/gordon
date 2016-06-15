import sys
import argparse
from splinter import Browser

class Colors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# colors
blue = Colors.BLUE
green = Colors.GREEN
yellow = Colors.YELLOW
red = Colors.RED
end = Colors.END

# argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address',
        help="crowbar address, for example 127.0.0.10")
parser.add_argument( '-p', '--port',
        help = "crowbar port, for example 3000, 8080")
args = parser.parse_args()
user_port = args.port
user_address = args.address

# check that input has an argument
if user_port is None or user_address is None:
    print("You should run this program with an argument, run 'gordon --h' for more information")
    sys.exit(1)

#browser = Browser('phantomjs')
browser = Browser('chrome')

errors = 0

url = "http://crowbar:crowbar@" + user_address + ":" + user_port
browser.visit(url)

# checking existence of nodes
def checktext(text):

    global errors

    if browser.is_text_present(text):
        print(text + ' test ' + green + 'PASSED' + end)
    else:
        print(text + ' test ' + red + 'FAILED' + end)
        errors += 1 

# check that we can create a new_group
browser.find_by_id('group').first.fill('new_group_1')
browser.find_by_name('commit').first.click()


# final output
print("1st group of tests")
print('=========')
print()
checktext('3 nodes')
checktext('crowbar')
checktext('dashboard')
print()
print("2nd group of tests")
print('==========')
checktext('new_group_1')

print()
print('=======')
print(yellow + "Errors: " + str(errors) + end)