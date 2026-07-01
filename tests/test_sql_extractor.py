import unittest

from app.utils.sql_extractor import extract_sql_query


class SqlExtractorTests(unittest.TestCase):
    def test_extract_sql_query_without_semicolon(self):
        text = "Here is the SQL query:\nSELECT * FROM sales LIMIT 10"

        sql = extract_sql_query(text)

        self.assertEqual(sql, "SELECT * FROM sales LIMIT 10")


if __name__ == "__main__":
    unittest.main()
