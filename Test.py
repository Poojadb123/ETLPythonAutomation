# test if there are any duplicate records/rows in target system
def test_checkDuplicates():
    target_df = pd.read_csv("target.csv", sep=",")
    count = target_df.duplicated().sum()
    assert count == 0 , "Duplication found - please verify the target"