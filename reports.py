from datetime import datetime


def import_data(filename='booking.txt'):
    """
    Import data from a file to a list. The columns are marked as follows:
    hotel;arrival_date;booked_nights;adults;children;babies;meal;country;reservation_status;reservation_status_date
    Expected returned data format:
        [["Resort Hotel", "01/22/2017", 4, 2, 0, 0, "YES", "PL", "Check-Out", "09/20/2022"],
        ["City Hotel", "01/22/2017", 2, 2, 0, 0, "NO", "FR", "Cancelled", "09/20/2022"],
        ...]

    :param str filename: optional, name of the file to be imported

    :returns: list of lists representing accomodation booking data
    :rtype: list
    """
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            line = line.strip()
            data = line.split(';')

            file_content.append(data)

        return file_content
    

# print(import_data())

def export_data(bookings, filename='booking.txt', mode='a'):
    """
    Export data from a list to file. If called with mode 'w' it should overwrite
    data in file. If called with mode 'a' it should append data at the end.

    :param list booking: booking data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    with open(filename, mode) as write_to_file:

        for book in bookings:
            write_to_file.write(book)



def get_rows_by_booking_status(rows, status):
    """
    Get booking rows by status

    :param list: booking data
    :param str status: status to filter by e.g. Canceled, Checked-out

    :raises ValueError: if given status is not present in the list. Error message: 'Status is not present in list'
    :returns: all rows of given status
    :rtype: list
    """
    for row in rows:
        if row[8].upper() == status.upper():
            print(row)

    
    


def get_rows_by_date(rows, date_in, date_out):
    """
    Get rows filtred by specific date

    :param list rows: rows data, date in, date out
    :returns: list of booking in date range betwee date_in and date_out
    :rtype: list
    """
    date_in = todatatype(date_in)
    # print(date_in)
    date_out = todatatype(date_out)
    # print(date_in)
    for row in rows:
        checkin = todatatype(row[1])
        # print(checkin)
        checkout = todatatype(row[9])
        # print(checkout)
        if checkin == date_in and checkout == date_out:
            return row


def main():
    rows = import_data()
    # get_rows_by_booking_status(rows, 'Canceled')
    # children_number_in_date()
    # print(todatatype('25/09/2022'))
    # print(children_number_in_date(rows , '09/20/2022', 'Resort Hotel'))
    print(get_rows_by_date(rows,'09/10/2022','09/08/2022'))

def children_number_in_date(rows, date, hotel):
    """
    Thos method should return amount of children in selected date and specific hotel

    :param list rows: booking data, date, hotel name
    :returns: number of chidren
    :rtype: int
    """
    data2 = todatatype(date)
    for row in rows:
        if todatatype(row[1]) == data2 and hotel == row[0]:

            return int(row[3])



def todatatype(data_imput):
    format = '%m/%d/%Y'
    return datetime.strptime(data_imput, format)
   
    
    
    

def display_reservation(rows, date):
    """
    Method return table representation of reservation in format:

    hotel | check in   | check out  | adults | children | babies | status
    Ibis  | 20/09/2022 | 25/09/2022 | 2      | 0        | 0      | checked-in


    Please get check out date based on arrival_date and booked nights
    """
    print('hotel | check in | check out | adults | children | babies | status')
    for row in rows:
        print(row)





if __name__ == '__main__':
    main()