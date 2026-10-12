import pandas as pd
from datetime import datetime

def calculate_priority(days_left):
    if days_left <= 0:
        return "EXPIRED"
    elif days_left <= 14:
        return "CRITICAL"
    elif days_left <= 45:
        return "WARNING"
    else:
        return "OK"

def main():
    # Load document metadata using your specific schema
    df = pd.read_csv("sample_document_expiry.csv")
    df["expiry_date"] = pd.to_datetime(df["expiry_date"])
    
    # Static snapshot date based on your test records (Oct 2026)
    today = datetime(2026, 10, 12)
    alerts = []

    print("=== Processing Compliance Document Expiry Status ===")
    
    for index, row in df.iterrows():
        delta_days = (row["expiry_date"] - today).days
        priority = calculate_priority(delta_days)
        
        # Flag anything expired or expiring within 45 days
        if delta_days <= 45:
            alerts.append({
                "doc_id": row["doc_id"],
                "doc_type": row["doc_type"],
                "owner": row["masked_owner"],
                "expiry_date": row["expiry_date"].date(),
                "days_remaining": delta_days,
                "alert_level": priority
            })

    # Save findings locally to your specified file name
    if alerts:
        alert_df = pd.DataFrame(alerts)
        alert_df = alert_df.sort_values(by="days_remaining")
        alert_df.to_csv("document_expiry_alert_report.csv", index=False)
        print(f"\nAlert report saved locally to 'document_expiry_alert_report.csv'.")
        print(f"Found {len(alerts)} records requiring attention:\n")
        print(alert_df[["doc_id", "doc_type", "alert_level", "days_remaining"]].to_string(index=False))
    else:
        print("All documents are secure. No upcoming expiries discovered.")

if __name__ == "__main__":
    main()
