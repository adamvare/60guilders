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


def write_string(path=str, ipo_data=str):
    try:
        with open(path, 'w') as the_file:
            the_file.write(ipo_data)

    except IOError:
        sys.stderr.write("[myScript] - Error: Could not write ipo_data\n")
        sys.exit(-1)


def make_priced_table(ipo_data) -> list:
    priced_table = []

    for i, word in enumerate(ipo_data):
        if word == 'Priced':
            j = i
            while ipo_data[j] != 'Upcoming':
                priced_row = {}
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                priced_row['Symbol'] = ipo_data[j]
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                priced_row['Company Name'] = ipo_data[j]
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                priced_row['Exchange/Market'] = ipo_data[j]
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                priced_row['Price'] = ipo_data[j]
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                priced_row['Shares'] = ipo_data[j]
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                priced_row['Date'] = ipo_data[j]
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                priced_row['Offer Amount'] = ipo_data[j]
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break
                j += 1
                if ipo_data[j] == 'Upcoming':
                    break

                priced_table.append(priced_row)
            break

    return priced_table


def make_upcoming_table(ipo_data) -> list:
    upcoming_table = []
    for i, word in enumerate(ipo_data):
        if word == 'Upcoming':
            j = i
            while not 'LAST' in ipo_data[j]:
                upcoming_row = {}
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                upcoming_row['Symbol'] = ipo_data[j]
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                upcoming_row['Company'] = ipo_data[j]
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                upcoming_row['Exchange/Market'] = ipo_data[j]
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                upcoming_row['Price'] = ipo_data[j]
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                upcoming_row['Shares'] = ipo_data[j]
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                upcoming_row['Expected IPO Date'] = ipo_data[j]
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                j += 1
                if 'LAST' in ipo_data[j]:
                    break
                upcoming_row['Offer Amount'] = ipo_data[j]

                upcoming_table.append(upcoming_row)
            break

    return upcoming_table


def make_filings_table(ipo_data) -> list:
    filings_table = []
    for i, word in enumerate(ipo_data):
        if word == 'Filings':
            j = i
            while not 'Withdrawn' in ipo_data[j]:
                filings_row = {}
                j += 1
                if 'Ltd.' in ipo_data[j] or 'ltd' in ipo_data[j] or 'Corp' in ipo_data[j] or 'Co' in ipo_data[j] or 'Inc' in ipo_data[j] or 'CORP' in ipo_data[j] or 'INC' in ipo_data[j]:
                    filings_row['Company Name'] = ipo_data[j]
                    filings_row['Date Filed'] = ipo_data[j+2]
                    filings_row['Offer Amount'] = ipo_data[j+4]
                # due to possibility of no symbol, the below is not possible.
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                # filings_row['Symbol'] = ipo_data[j]
                # j += 1
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                # j += 1
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                # filings_row['Company Name'] = ipo_data[j]
                # j += 1
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                # j += 1
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                # filings_row['Date Filed'] = ipo_data[j]
                # j += 1
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                # j += 1
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                # filings_row['Offer Amount'] = ipo_data[j]
                # j += 1
                # if 'Withdrawn' in ipo_data[j]:
                #     break
                    filings_table.append(filings_row)
            break

    return filings_table


def make_withdrawn_table(ipo_data) -> list:
    withdrawn_table = []
    for i, word in enumerate(ipo_data):
        if word == 'Withdrawn':
            j = i
            while not 'Upcoming' in ipo_data[j]:
                withdrawn_row = {}
                j += 1
                if 'Upcoming' in ipo_data[j]:
                    break
                if 'Ltd' in ipo_data[j] or 'ltd' in ipo_data[j] or 'Corp' in ipo_data[j] or 'Co' in ipo_data[j] or 'Inc' in ipo_data[j] or 'CORP' in ipo_data[j] or 'INC' in ipo_data[j]:
                    withdrawn_row['Company Name'] = ipo_data[j]

                withdrawn_table.append(withdrawn_row)

    # cleanup empty objects inside
    cleaned_withdrawn_table = []
    for row in withdrawn_table:
        if row:
            cleaned_withdrawn_table.append(row)

    return cleaned_withdrawn_table
