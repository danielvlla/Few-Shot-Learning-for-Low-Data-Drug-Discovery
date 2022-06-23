import pandas as pd
import os


def create_dataset(subset, subset_dir, output_dir):
    actives_name = "actives_final.ism"
    decoys_name = "decoys_final.ism"

    subset_df = pd.DataFrame()

    for root, subdirectories, files in os.walk(subset_dir):
        for subdirectory in subdirectories:
            # print(root, subdirectories)
            actives = pd.read_csv(
                f"{os.path.join(root, subdirectory)}/{actives_name}", sep=" ", header=None
            )
            decoys = pd.read_csv(
                f"{os.path.join(root, subdirectory)}/{decoys_name}", sep=" ", header=None
            )

            actives[subdirectory] = 1
            decoys[subdirectory] = 0

            target_df = pd.concat([actives, decoys])

            target_df.columns = ["smiles", "id", "chemid", subdirectory]
            target_df = target_df.drop(["id", "chemid"], axis=1)

            if len(subset_df) == 0:
                subset_df = target_df
            else:
                subset_df = pd.merge(subset_df, target_df, how="outer")

    print(f"SAVING {subset}.csv")
    subset_df.to_csv(f"{output_dir}/{subset}.csv", index=False)


create_dataset("gpcr", "./gpcr", "./")
create_dataset("nuclear", "./nuclear", "./")
