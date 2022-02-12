import requests
import pandas as pd
import numpy as np
from PIL import Image
import os
import logging
import random

logging.basicConfig(filename='data-fetcher3.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

df = pd.read_csv("./Data/all_images3.csv", index_col=None)
gold_df = pd.read_csv("./Data/gold_standard_data.csv", index_col=None)

print(gold_df.head())
print(gold_df.shape)

print(df[df['CaptureEventID']==gold_df["CaptureEventID"].iloc[0]].iloc[-1])
print(df.URL_Info[df.CaptureEventID == gold_df["CaptureEventID"].iloc[0]].values[-1])
base_url = "https://snapshotserengeti.s3.msi.umn.edu/"

gold_df1 = gold_df.drop_duplicates(subset=["CaptureEventID"], keep="last")
gold_df1.reset_index(inplace=True)
print(gold_df.shape)

for index, row in gold_df.loc[:].iterrows():
    try:

        url = base_url+df.URL_Info[df.CaptureEventID == row["CaptureEventID"]].values[-1]
        # r = requests.get(url)
        #
        # f = open("./Data/images3/"+str(row["CaptureEventID"])+".JPG", 'wb')
        # f.write(r.content)
        # f.close()
        #
        # im = Image.open("./Data/images3/"+str(row["CaptureEventID"])+".JPG")
        # im = im.resize((224, 224))
        #
        # os.remove("./Data/images3/"+str(row["CaptureEventID"])+".JPG")
        # im = im.save("./Data/images3/"+str(row["CaptureEventID"])+".JPG")
        #
        if index%100 == 0:
            print(index)
    except Exception as e:
        print(index, row["CaptureEventID"])
        logger.error(e)
