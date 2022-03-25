import unittest

import sqlite3  as sql

class testing_mobile_nameDB(unittest.TestCase):

    def setUp(self):
        self.Mobile_Name1 = "Iphone"
        # self.Mobile_Name2 = "Samsung"
        self.Serial_Number = "12"

        self.connection = sql.connect("mobile.db")

    def tearDown(self):

        self.Mobile_Name = " "
        self.Serial_Number = " "
        self.connection.close()


    def test_verify_mobilName(self):

        result = self.connection.execute("Select Brand_Name From Smart_phones Where Serial_Number=" + self.Serial_Number)

        for i in result:
            fetch_mobile_name = i[0]

        self.assertEqual(self.Mobile_Name1, fetch_mobile_name)

    # def test_verify_mobilName2(self):
    #
    #     result = self.connection.execute("Select Brand_Name From Smart_phones Where Serial_Number=" + self.Serial_Number)
    #
    #     for i in result:
    #         fetch_mobile_name = i[0]
    #
    #     self.assertEqual(self.Mobile_Name2, fetch_mobile_name)


if __name__ == "__main__":
    unittest.main()