# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import fileinput


def add_currency(file, new_file):
    with open(new_file, 'w+') as file_out:
        for line in fileinput.input(file):
            if '"AT"' in line or '"DE"' in line or '"FR"' in line or '"ES"' in line or '"LU"' in line or '"MT"' in line or '"IT"' in line:
                file_out.write(line.replace('description', 'currency="EUR" description'))
                print(line.replace('description', 'currency="EUR" description'))
            elif '"GB"' in line:
                file_out.write(line.replace('description', 'currency="GBP" description'))
            elif '"US"' in line:
                file_out.write(line.replace('description', 'currency="USD" description'))
            elif '"IL"' in line:
                file_out.write(line.replace('description', 'currency="ILS" description'))
            elif '"CH"' in line:
                file_out.write(line.replace('description', 'currency="CHF" description'))
            elif '"SE"' in line:
                file_out.write(line.replace('description', 'currency="SEK" description'))
            elif '"AU"' in line:
                file_out.write(line.replace('description', 'currency="AUD" description'))
            elif '"CA"' in line:
                file_out.write(line.replace('description', 'currency="CAD" description'))


if __name__ == '__main__':
    # add_currency('/home/dani/Downloads/clients.xml', 'clients_new.xml')
    add_currency('/home/dani/Downloads/accounts.xml', 'accounts_new.xml')
