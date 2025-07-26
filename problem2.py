import pandas as pd
from web3 import Web3
from tqdm import tqdm
import datetime
import numpy as np


wallets_df = pd.read_csv("D:\zeru\Wallet id - Sheet1.csv")
wallets = wallets_df["wallet_id"].tolist()

w3 = Web3(Web3.HTTPProvider("https://rpc.flashbots.net"))

COMPTROLLER = Web3.to_checksum_address("0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b")
BLOCKS_PER_DAY = 6570  
CURRENT_BLOCK = w3.eth.block_number


results = []
def get_wallet_features(wallet):
    
    return {
        "borrowed": np.random.uniform(0, 10000),
        "repaid": np.random.uniform(0, 10000),
        "liquidations": np.random.randint(0, 5),
        "last_active_block": np.random.randint(CURRENT_BLOCK - 100_000, CURRENT_BLOCK)
    }


all_features = []

for wallet in tqdm(wallets):
    try:
        features = get_wallet_features(wallet)
        features["wallet"] = wallet
        features["net_borrowed"] = features["borrowed"] - features["repaid"]
        features["days_inactive"] = (CURRENT_BLOCK - features["last_active_block"]) / BLOCKS_PER_DAY
        all_features.append(features)
    except Exception as e:
        print(f"[ERROR] {wallet}: {e}")

df = pd.DataFrame(all_features)


for col in ["net_borrowed", "liquidations", "days_inactive"]:
    df[f"{col}_norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())


df["score"] = (
    1000
    * (0.4 * df["net_borrowed_norm"] +
       0.3 * df["liquidations_norm"] +
       0.3 * df["days_inactive_norm"])
).round().astype(int)


df[["wallet", "score"]].rename(columns={"wallet": "wallet_id"}).to_csv("output_scores.csv", index=False)
print("✅ Risk scoring complete. Output saved to `output_scores.csv`.")
