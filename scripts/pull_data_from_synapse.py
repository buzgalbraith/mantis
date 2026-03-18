"""
Downloads a list of FastQ files from synapse to ./data
Note: Must sign up for an account on synapse and set your auth token to the environmental variable `$SYNAPSE_AUTH_TOKEN`
"""
import csv
import os 
import synapseclient

def main(target_num:int = 750):
    """pull files from synapse"""
    i = 0
    with open('synapse_data/fastq_file_list.tsv', mode = 'r') as f:
        reader = csv.reader(f, delimiter = '\t')
        for _, fid, _ in reader:
            syn.get(fid, downloadLocation = './synapse_data', ifcollision='keep.local')
            i+= 1
            if i >= target_num:
                break

if __name__ == "__main__":
    num_files = 750
    syn = synapseclient.login()
    assert syn._is_logged_in()
    main(num_files)

