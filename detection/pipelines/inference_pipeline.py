"""
inference_pipeline.py

5G NFV Digital Forensic Readiness Inference Pipeline

Author:
    Sheunesu Makura

Description:
    End-to-end forensic readiness pipeline:

"""

from pathlib import Path
from datetime import datetime
import json
import requests

from zeek_parser import parse_conn_log
from feature_extraction import extract_features


class ForensicReadinessPipeline:

    def __init__(self,
                 api_url="http://localhost:8000"):

        self.api_url = api_url

    def run(self, conn_log):

        print("\n========================================")
        print("5G Digital Forensic Readiness Pipeline")
        print("========================================\n")

        conn_log = Path(conn_log)

        if not conn_log.exists():

            raise FileNotFoundError(conn_log)

        print("[1/5] Parsing Zeek log...")

        dataframe = parse_conn_log(conn_log)

        print(f"      Records: {len(dataframe)}")

        print("\n[2/5] Extracting forensic features...")

        features = extract_features(dataframe)

        print(f"      Features extracted: {len(features)}")

        print("\n[3/5] Sending features to Attack Detection API...")

        response = requests.post(

            f"{self.api_url}/detect",

            json={
                "features": features
            },

            timeout=30

        )

        if response.status_code != 200:

            raise RuntimeError(response.text)

        detection = response.json()

        print("\n      Attack Type :",
              detection["attack_type"])

        print("      Confidence :",
              f'{detection["confidence"]*100:.2f}%')

        print("\n[4/5] Saving forensic evidence...")

        evidence = {

            "timestamp":

                datetime.utcnow().isoformat(),

            "source":

                str(conn_log),

            "features":

                features,

            "detection":

                detection

        }

        evidence_directory = Path("../reports/evidence")

        evidence_directory.mkdir(

            parents=True,

            exist_ok=True

        )

        evidence_file = (

            evidence_directory /

            f'{detection["id"]}.json'

        )

        with open(

            evidence_file,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                evidence,

                f,

                indent=4

            )

        print("      Saved:", evidence_file)

        print("\n[5/5] Generating forensic report...")

        pdf = requests.get(

            f'{self.api_url}/reports/{detection["id"]}',

            timeout=60

        )

        report_directory = Path("../reports/pdf")

        report_directory.mkdir(

            parents=True,

            exist_ok=True

        )

        pdf_file = (

            report_directory /

            f'{detection["id"]}.pdf'

        )

        with open(pdf_file, "wb") as f:

            f.write(pdf.content)

        print("      Report:", pdf_file)

        print("\n========================================")
        print("Pipeline completed successfully.")
        print("========================================\n")

        return evidence


def main():

    import argparse

    parser = argparse.ArgumentParser(

        description="5GDFRT Inference Pipeline"

    )

    parser.add_argument(

        "--input",

        required=True,

        help="Path to conn.log"

    )

    parser.add_argument(

        "--api",

        default="http://localhost:8000",

        help="Attack Detection API"

    )

    args = parser.parse_args()

    pipeline = ForensicReadinessPipeline(

        api_url=args.api

    )

    pipeline.run(args.input)


if __name__ == "__main__":

    main()