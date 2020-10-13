# after putting ctrl a into a text file, this program will be ran.
# I am using firefox
#
#
#

import sys
import re


def get_string() -> str:

    input = './txt_files/input.txt'

    try:
        with open(input) as inputFileHandle:
            return inputFileHandle.read()

    except IOError:
        sys.stderr.write("[myScript] - Error: Could not open %s\n" % (input))
        sys.exit(-1)


def write_string(ipo_data=str):
    try:
        with open('./txt_files/output.txt', 'w') as the_file:
            the_file.write(ipo_data)

    except IOError:
        sys.stderr.write("[myScript] - Error: Could not write ipo_data\n")
        sys.exit(-1)

# each is a table that is an array with many arrays containing dicts
# priced
# Upcoming
# filings


def make_priced_table(ipo_data) -> list:
    priced_table = []

    for i, word in enumerate(ipo_data):
        if word == 'Priced':
            # begin priced section
            j = i
            while not 'Upcoming' in ipo_data[j] and ipo_data[j+1] != 'Upcoming':
                priced_row = {}
                if ipo_data[j] != 'Upcoming':
                    j += 1
                    priced_row['Symbol'] = ipo_data[j]
                if ipo_data[j] != 'Upcoming' and ipo_data[j+1] != 'Upcoming':
                    j += 2
                    priced_row['Company Name'] = ipo_data[j]
                if ipo_data[j] != 'Upcoming' and ipo_data[j+1] != 'Upcoming':
                    j += 2
                    priced_row['Exchange/Market'] = ipo_data[j]
                if ipo_data[j] != 'Upcoming' and ipo_data[j+1] != 'Upcoming':
                    j += 2
                    priced_row['Price'] = ipo_data[j]
                if ipo_data[j] != 'Upcoming' and ipo_data[j+1] != 'Upcoming':
                    j += 2
                    priced_row['Shares'] = ipo_data[j]
                if ipo_data[j] != 'Upcoming' and ipo_data[j+1] != 'Upcoming':
                    j += 2
                    priced_row['Date'] = ipo_data[j]
                if ipo_data[j] != 'Upcoming' and ipo_data[j+1] != 'Upcoming':
                    j += 2
                    priced_row['Offer Amount'] = ipo_data[j]
                j += 2
                priced_table.append(priced_row)
                print('yo')
                print(len(priced_table))

    return priced_table


def make_upcoming_table(ipo_data) -> list:
    upcoming_table = []

    for i, word in enumerate(ipo_data):
        if word == 'Upcoming':
            j = i
            while not 'LAST' in ipo_data[j]:
                upcoming_row = {}
                if 'LAST' in ipo_data[j+1]:
                    break
                upcoming_row['Symbol'] = ipo_data[j+1]
                upcoming_row['Company'] = ipo_data[j+2]
                upcoming_row['Exchange/Market'] = ipo_data[j+3]
                upcoming_row['Price'] = ipo_data[j+4]
                upcoming_row['Shares'] = ipo_data[j+5]
                upcoming_row['Expected IPO Date'] = ipo_data[j+6]
                upcoming_row['Offer Amount'] = ipo_data[j+7]
                upcoming_table.append(upcoming_row)
                j += 7

        return upcoming_table


def make_filings_table(ipo_data) -> list:
    filings_table = []

    j = 0
    for i, word in enumerate(ipo_data):
        if word == 'Filings':
            j = i + 1
            while not 'Upcoming' in ipo_data[j]:
                filing_row = {}
                while not '$' in ipo_data[j]:
                    if ipo_data[j].isupper() is True:
                        filing_row['Symbol'] = ipo_data[j]
                    elif ipo_data[j+1].count("/") == 2:
                        filing_row['Company Name'] = ipo_data[j]
                    elif ipo_data[j].count("/") == 2:
                        filing_row['Date Filed'] = ipo_data[j]

                    j += 1
                filing_row['Offer Amount'] = ipo_data[j]
                filings_table.append(filing_row)
                j += 1

        return filings_table


def transform_string(ipo_data=str) -> str:
    #ipo_data = re.sub(r"[\n]*", "", ipo_data)
    # ipo_data = ipo_data.split([sep=None[, maxsplit]])
    ipo_data = ipo_data.split('\n')  # split by all whitespace

    #print(ipo_data)

    # these tables are lists of dicts
    priced_table = make_priced_table(ipo_data)
    # upcoming_table = make_upcoming_table(ipo_data)
    # filings_table = make_filings_table(ipo_data)

    print(priced_table)

    # for row in priced_table:
    #     for k, v in row.items():
    #         print(k, '\t', v)

    # format structures into the string I want (maybe even into the html I want for ultimate email). (use wikipedia api too)

    return "hey"
