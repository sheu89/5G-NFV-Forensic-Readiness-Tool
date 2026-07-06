"""
feature_extraction.py

Feature extraction pipeline for the 5G NFV Digital Forensic Readiness Tool.

Author:
    Sheunesu Makura

Description:
    Converts parsed Zeek network logs into machine learning features used by
    the attack detection API.
"""

from typing import Dict, Any

import numpy as np
import pandas as pd


class FeatureExtractor:

    def __init__(self):

        pass

    @staticmethod
    def _safe_mean(series):

        if series.empty:
            return 0.0

        return float(series.mean())

    @staticmethod
    def _safe_sum(series):

        if series.empty:
            return 0.0

        return float(series.sum())

    @staticmethod
    def _safe_std(series):

        if len(series) <= 1:
            return 0.0

        return float(series.std())

    def extract(self, df: pd.DataFrame) -> Dict[str, Any]:

        features = {}

        # --------------------------------------------------
        # General Flow Statistics
        # --------------------------------------------------

        features["total_flows"] = len(df)

        if "duration" in df.columns:

            duration = pd.to_numeric(df["duration"], errors="coerce").fillna(0)

            features["flow_duration_mean"] = self._safe_mean(duration)
            features["flow_duration_std"] = self._safe_std(duration)
            features["flow_duration_max"] = float(duration.max())
            features["flow_duration_min"] = float(duration.min())

        # --------------------------------------------------
        # Bytes
        # --------------------------------------------------

        if "orig_bytes" in df.columns:

            orig = pd.to_numeric(df["orig_bytes"], errors="coerce").fillna(0)

            features["orig_bytes_mean"] = self._safe_mean(orig)
            features["orig_bytes_total"] = self._safe_sum(orig)

        if "resp_bytes" in df.columns:

            resp = pd.to_numeric(df["resp_bytes"], errors="coerce").fillna(0)

            features["resp_bytes_mean"] = self._safe_mean(resp)
            features["resp_bytes_total"] = self._safe_sum(resp)

        # --------------------------------------------------
        # Packets
        # --------------------------------------------------

        if "orig_pkts" in df.columns:

            pkts = pd.to_numeric(df["orig_pkts"], errors="coerce").fillna(0)

            features["orig_packets_mean"] = self._safe_mean(pkts)
            features["orig_packets_total"] = self._safe_sum(pkts)

        if "resp_pkts" in df.columns:

            pkts = pd.to_numeric(df["resp_pkts"], errors="coerce").fillna(0)

            features["resp_packets_mean"] = self._safe_mean(pkts)
            features["resp_packets_total"] = self._safe_sum(pkts)

        # --------------------------------------------------
        # Protocol Distribution
        # --------------------------------------------------

        if "proto" in df.columns:

            proto_counts = df["proto"].value_counts()

            features["tcp_connections"] = int(proto_counts.get("tcp", 0))
            features["udp_connections"] = int(proto_counts.get("udp", 0))
            features["icmp_connections"] = int(proto_counts.get("icmp", 0))

        # --------------------------------------------------
        # Services
        # --------------------------------------------------

        if "service" in df.columns:

            service_counts = df["service"].value_counts()

            features["http_connections"] = int(service_counts.get("http", 0))
            features["dns_connections"] = int(service_counts.get("dns", 0))
            features["ssl_connections"] = int(service_counts.get("ssl", 0))
            features["ssh_connections"] = int(service_counts.get("ssh", 0))

        # --------------------------------------------------
        # Connection State
        # --------------------------------------------------

        if "conn_state" in df.columns:

            states = df["conn_state"].value_counts()

            features["successful_connections"] = int(states.get("SF", 0))
            features["failed_connections"] = int(states.get("REJ", 0))

        # --------------------------------------------------
        # Unique Hosts
        # --------------------------------------------------

        if "id.orig_h" in df.columns:

            features["unique_source_ips"] = int(
                df["id.orig_h"].nunique()
            )

        if "id.resp_h" in df.columns:

            features["unique_destination_ips"] = int(
                df["id.resp_h"].nunique()
            )

        # --------------------------------------------------
        # Ports
        # --------------------------------------------------

        if "id.resp_p" in df.columns:

            features["unique_destination_ports"] = int(
                df["id.resp_p"].nunique()
            )

        # --------------------------------------------------
        # Ratios
        # --------------------------------------------------

        if (
            features.get("orig_bytes_total", 0) > 0 and
            features.get("resp_bytes_total", 0) > 0
        ):

            features["byte_ratio"] = (
                features["orig_bytes_total"] /
                features["resp_bytes_total"]
            )

        else:

            features["byte_ratio"] = 0

        return features


def extract_features(df):

    extractor = FeatureExtractor()

    return extractor.extract(df)


if __name__ == "__main__":

    from zeek_parser import parse_conn_log

    df = parse_conn_log("../../sample_logs/conn.log")

    features = extract_features(df)

    print()

    print("=" * 60)
    print("5GDFRT Feature Extraction")
    print("=" * 60)

    for key, value in features.items():

        print(f"{key:<35} {value}")