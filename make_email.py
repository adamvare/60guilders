from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import wikipedia

from filter_ipo_calendar import *


def make_email(tables=tuple):

    format_for_plain_text_email(tables)


def transform_string(ipo_data=str) -> tuple:
    ipo_data = ipo_data.split('\n')  # split by all whitespace
    # print(ipo_data)

    # these tables are lists of dicts
    priced_table = make_priced_table(ipo_data)
    upcoming_table = make_upcoming_table(ipo_data)
    filings_table = make_filings_table(ipo_data)
    withdrawn_table = make_withdrawn_table(ipo_data)

    # print('priced table: ', priced_table)
    # print('\n upcoming table: ', upcoming_table)
    # print('\n filings table: ', filings_table)
    # print('\n withdrawn table: ', withdrawn_table)
    return (priced_table, upcoming_table, filings_table, withdrawn_table)


def format_for_plain_text_email(tables: tuple):
    # format plaintext email:
    (priced_table, upcoming_table, filings_table, withdrawn_table) = tables
    plain_text_email_upcoming = []

    for row in upcoming_table:
        try:
            name = row['Company'].upper()
            stopwords = ['CORP', '.', 'CORP.', 'INC.', 'INC', 'LTD', 'Ltd']
            name = name.split()
            new_name = [word for word in name if word.upper()
                        not in stopwords]
            name = ' '.join(new_name)
            name = re.sub(r"[,]*", "", name)
            company_wikipedia_page = wikipedia.page(name)
            email_part = '%s coming out on %s and offering %s shares for %s\n url:\n%s\n' % (
                row['Company'].upper(), row['Expected IPO Date'], row['Shares'], row['Offer Amount'], company_wikipedia_page.url)
        except:
            email_part = '%s coming out on %s and offering %s shares for %s\n\n' % (
                row['Company'].upper(), row['Expected IPO Date'], row['Shares'], row['Offer Amount'])
        plain_text_email_upcoming.append(email_part)

    # print(plain_text_email_upcoming)

    try:
        write_string('./email/email.txt', '\n'.join(plain_text_email_upcoming))
        print('success writing plaintext email')
    except:
        print('failure writing plaintext email')
    # make html content

    # and probably should have plain text backup.

    # format structures into the string I want (maybe even into the html I want for ultimate email). (use wikipedia api too)


# f = open('./email/email_output.html', 'wb')

#     message = """<!DOCTYPE html>
# <html>

# <head>
#     <style>
#         body {
#             background-color: darkkhaki;
#         }
#     </style>
# </head>

# <body>

#     <h1>My First Heading</h1>
#     <p>My first paragraph.</p>

# </body>

# </html>"""

#     f.write(message)
#     f.close()

# possibly for later:
## ipo_data = re.sub(r"[\n]*", "", ipo_data)
    # ipo_data = ipo_data.split([sep=None[, maxsplit]])
  # for row in priced_table:
    #     for k, v in row.items():
    #         print(k, '\t', v)
