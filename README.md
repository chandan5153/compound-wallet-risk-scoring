# Compound Wallet Risk Scoring

This project assigns a **risk score from 0 to 1000** to a set of Ethereum wallet addresses based on their historical behavior within the **Compound V2 lending protocol**.

The risk score is intended to reflect the financial reliability of each wallet, considering their borrowing, repayment, liquidation history, and protocol interaction recency.

---

## 🚀 Features

- Fetch wallet transaction data from the Compound V2 protocol (mocked or via RPC/Graph).
- Extract risk indicators like:
  - Total Borrowed
  - Total Repaid
  - Net Borrowed
  - Number of Liquidations
  - Days Since Last Interaction
- Normalize and weight these features to compute a **composite risk score (0–1000)**.
- Export results to `output_scores.csv`.

---

## 📂 File Structure
├── compound_risk_score.py # Main script to generate risk scores
├── wallets.csv # Input wallet list (100 wallets)
├── output_scores.csv # Final output: wallet_id and score

## Install The Required Dependencies
pip install pandas web3 tqdm numpy

## Run using this command
python problem2.py
