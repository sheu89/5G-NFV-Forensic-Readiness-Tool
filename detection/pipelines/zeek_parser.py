"""
zeek_parser.py

Generic Zeek log parser for the 5G NFV Digital Forensic Readiness Tool (5GDFRT).

Author:
    Sheunesu Makura

Description:
    Parses standard Zeek TSV log files into Python dictionaries or Pandas
    DataFrames for downstream feature extraction and machine learning.

Supported logs:
    - conn.log
    - dns.log
    - http.log
    - ssl.log
    - notice.log
    - and any standard Zeek TSV log.
"""

from pathlib import Path
from typing import List, Dict, Any

import pandas as pd


class ZeekParser:
    

    def __init__(self):

        self.separator = "\t"
        self.empty_field = "(empty)"
        self.unset_field = "-"

    def parse(self, log_file: str | Path) -> List[Dict[str, Any]]:
        """
        Parse a Zeek log into a list of dictionaries.

        Parameters
        ----------
        log_file : str | Path

        Returns
        -------
        List[Dict]
        """

        log_file = Path(log_file)

        if not log_file.exists():
            raise FileNotFoundError(f"{log_file} does not exist.")

        fields = []
        records = []

        with open(log_file, "r", encoding="utf-8") as f:

            for line in f:

                line = line.rstrip("\n")

                if not line:
                    continue

                # Read header definitions
                if line.startswith("#separator"):
                    continue

                elif line.startswith("#set_separator"):
                    continue

                elif line.startswith("#empty_field"):
                    self.empty_field = line.split()[-1]
                    continue

                elif line.startswith("#unset_field"):
                    self.unset_field = line.split()[-1]
                    continue

                elif line.startswith("#path"):
                    continue

                elif line.startswith("#open"):
                    continue

                elif line.startswith("#close"):
                    continue

                elif line.startswith("#fields"):

                    fields = line.split("\t")[1:]
                    continue

                elif line.startswith("#types"):
                    continue

                # Actual data

                values = line.split("\t")

                row = {}

                for field, value in zip(fields, values):

                    if value == self.unset_field:

                        row[field] = None

                    elif value == self.empty_field:

                        row[field] = ""

                    else:

                        row[field] = self._convert(value)

                records.append(row)

        return records

    def to_dataframe(self, log_file: str | Path) -> pd.DataFrame:
        """
        Parse a Zeek log directly into a Pandas DataFrame.
        """

        return pd.DataFrame(self.parse(log_file))

    @staticmethod
    def _convert(value: str):
        """
        Automatically convert values to appropriate Python types.
        """

        if value is None:
            return None

        if value in ("T", "F"):

            return value == "T"

        try:

            if "." in value:

                return float(value)

            return int(value)

        except ValueError:

            return value


def parse_conn_log(log_file: str | Path) -> pd.DataFrame:
    """
    Convenience function for conn.log.
    """

    parser = ZeekParser()

    return parser.to_dataframe(log_file)


def parse_dns_log(log_file: str | Path) -> pd.DataFrame:

    parser = ZeekParser()

    return parser.to_dataframe(log_file)


def parse_http_log(log_file: str | Path) -> pd.DataFrame:

    parser = ZeekParser()

    return parser.to_dataframe(log_file)


def parse_ssl_log(log_file: str | Path) -> pd.DataFrame:

    parser = ZeekParser()

    return parser.to_dataframe(log_file)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Parse Zeek log files."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to Zeek log"
    )

    args = parser.parse_args()

    zeek = ZeekParser()

    df = zeek.to_dataframe(args.input)

    print()

    print("=" * 70)
    print("5GDFRT Parser")
    print("=" * 70)

    print(f"File          : {args.input}")
    print(f"Records       : {len(df)}")
    print(f"Columns       : {len(df.columns)}")

    print()

    print(df.head())

    print()

    print("=" * 70)