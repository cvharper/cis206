# this one i referenced off the wikiversity example 
import sqlite3
import sys

# actual database
DATABASE = "Northwind.db"


def get_tables():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # i had an issue where this table kept showing.. :(
    # i now hate this table
    sql = """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    AND name NOT LIKE 'sqlite_%'; 
"""
    cursor.execute(sql)

    tables = [row[0] for row in cursor.fetchall()]

    connection.close()
    return tables


def display_tables(tables):
    print("\nNorthwind Tables")

    for number, table in enumerate(tables, start=1):
        print(number, table)

    print("0. Exit")


def display_table(table):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    sql = f'SELECT rowid, * FROM "{table}"'
    cursor.execute(sql)

    rows = cursor.fetchall()
    columns = ["Row"] + [
        description[0] for description in cursor.description[1:]
    ]

    print("\n", columns)

    for row in rows:
        print(row)

    connection.close()


def insert_record(table):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(f'PRAGMA table_info("{table}")')
    fields = cursor.fetchall()

    columns = []
    values = []

    print("\nEnter new record information.")
    print("Leave a field blank to use its default value.")

    for field in fields:
        name = field[1]
        value = input(name + ": ")

        if value != "":
            columns.append('"' + name + '"')
            values.append(value)

    try:
        if columns:
            sql = (
                f'INSERT INTO "{table}" '
                f'({", ".join(columns)}) '
                f'VALUES ({", ".join("?" for value in values)});'
            )
            cursor.execute(sql, values)
        else:
            cursor.execute(f'INSERT INTO "{table}" DEFAULT VALUES;')

        connection.commit()
        print("Record inserted successfully.")

    except Exception as exception:
        print("Unable to insert record.")
        print(exception)

    finally:
        connection.close()


def update_record(table):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    display_table(table)

    try:
        row_number = int(input("\nEnter row number to update: "))

        cursor.execute(f'PRAGMA table_info("{table}")')
        fields = [field[1] for field in cursor.fetchall()]

        print("\nFields:")
        for number, field in enumerate(fields, start=1):
            print(number, field)

        field_number = int(input("Select field to update: "))

        if field_number < 1 or field_number > len(fields):
            print("Invalid field selection.")
            return

        field = fields[field_number - 1]
        value = input("Enter new value: ")

        sql = (
            f'UPDATE "{table}" '
            f'SET "{field}" = ? '
            f'WHERE rowid = ?;'
        )

        cursor.execute(sql, (value, row_number))

        if cursor.rowcount > 0:
            connection.commit()
            print("Record updated successfully.")
        else:
            print("Record not found.")

    except ValueError:
        print("Please enter a valid number.")

    except Exception as exception:
        print("Unable to update record.")
        print(exception)

    finally:
        connection.close()


def delete_record(table):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    display_table(table)

    try:
        row_number = int(input("\nEnter row number to delete: "))

        confirm = input("Are you sure? (Y/N): ")

        if confirm.upper() == "Y":
            sql = f'DELETE FROM "{table}" WHERE rowid = ?;'
            cursor.execute(sql, (row_number,))

            if cursor.rowcount > 0:
                connection.commit()
                print("Record deleted successfully.")
            else:
                print("Record not found.")

    except ValueError:
        print("Please enter a valid number.")

    except Exception as exception:
        print("Unable to delete record.")
        print(exception)

    finally:
        connection.close()


def main():

    try:
        tables = get_tables()

        while True:
            display_tables(tables)

            choice = input("\nSelect a table: ")

            if choice == "0":
                print("Exiting program.")
                break

            try:
                table = tables[int(choice) - 1]

            except (ValueError, IndexError):
                print("Invalid table selection.")
                continue

            while True:
                display_table(table)
                print("\n1. Insert")
                print("2. Update")
                print("3. Delete")
                print("4. Back to tables")
                print("0. Exit")

                action = input("\nChoose an option: ").upper()

                if action == "1":
                    insert_record(table)

                elif action == "2":
                    update_record(table)

                elif action == "3":
                    delete_record(table)

                elif action == "4":
                    break

                elif action == "0":
                    print("Exiting program.")
                    return

                else:
                    print("Invalid selection.")

    except Exception:
        print("Unexpected error.")
        print("Error:", sys.exc_info()[1])

# main you need to be here or else the program bricks
main()
