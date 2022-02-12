import requests
import pandas as pd
import numpy as np
from PIL import Image
import os
import logging
import random

logging.basicConfig(filename='data-fetcher.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

df = pd.read_csv("./Data/all_images.csv", index_col=None)
consensus_df = pd.read_csv("./Data/consensus_data.csv", index_col=None)

print(df.index[df["CaptureEventID"]=="ASG0002o9c"].tolist())
print(df.head())
print(df.shape)

df = df.drop_duplicates(subset=["CaptureEventID"], keep="last")
df.reset_index(inplace=True)
print(df.index[df["CaptureEventID"]=="ASG0001ahu"].tolist())
print(df.head())
print(df.shape)

base_url = "https://snapshotserengeti.s3.msi.umn.edu/"


for index, row in df.loc[76503:].iterrows():
    # print(index, row["CaptureEventID"], row["URL_Info"])
    try:
        # print(row["CaptureEventID"], row["CaptureEventID"] in consensus_df["CaptureEventID"].values)
        if row["CaptureEventID"] not in consensus_df["CaptureEventID"].values:
            randn = random.random()
            if randn > 0.3:
                if index%100==0:
                    print(index)
                continue
        # print(index, row["CaptureEventID"] in consensus_df["CaptureEventID"].values, randn, row["CaptureEventID"])
        url = base_url+row["URL_Info"]
        r = requests.get(url)

        f = open("./Data/images/"+str(row["CaptureEventID"])+".JPG", 'wb')
        f.write(r.content)
        f.close()

        im = Image.open("./Data/images/"+str(row["CaptureEventID"])+".JPG")
        im = im.resize((224, 224))

        os.remove("./Data/images/"+str(row["CaptureEventID"])+".JPG")
        im = im.save("./Data/images/"+str(row["CaptureEventID"])+".JPG")

        if index%100 == 0:
            print(index)
    except Exception as e:
        logger.error(e)
