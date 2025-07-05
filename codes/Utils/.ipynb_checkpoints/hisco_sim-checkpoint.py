

import numpy as np
import recordlinkage as rl
from recordlinkage.base import BaseCompareFeature
import pandas as pd

class HiscoSimilarity(BaseCompareFeature):
    '''
    HiscoSimilarity is a class that inherits from BaseCompareFeature. It is used to compare two records based on their
    '''
    def __init__(self, left_on, right_on, hisco_sim_table, *args, **kwargs):
        print("init")
        super(HiscoSimilarity, self).__init__(left_on, right_on, *args, **kwargs)
        
        self.hisco_sim_table = hisco_sim_table # The table records aggregated Cosine similarity (3-digits). Should be a df
        # values range from -1 to 1, where 1 indicates identical orientation (maximum similarity), 0 indicates orthogonality (no similarity), and -1 indicates opposite orientation.
        print("init finished")
    
    # def _compute_vectorized(self, hisco_code1, hisco_code2):
    #     print(type(hisco_code1))
    #     # if parID_1 == parID_2: return True
    #     # if parID_1 in self.pairs_within_10km.keys():
    #     #     return self.pairs_within_10km[parID_1] == parID_2
    #     # else: return False
        
    #     if ((not hisco_code1) | (not hisco_code2)):  
    #         return None
    #     if hisco_code1 == hisco_code2:
    #         return 1  # identical, even if hisco code is not in distance table
    #     else:
    #         if (not hisco_code1 in self.hisco_sim_table.occ_i.tolist()) | (not hisco_code2 in self.hisco_sim_table.occ_i.tolist()): 
    #             # hisco codes in distance table should be a subset of that in hisco_table
    #             # hisco_sim_table.occ_i is a super-set of hisco_sim_table.occ_j
    #             return None
    #         return self.hisco_sim_table.loc[(self.hisco_sim_table.occ_i == hisco_code1) & (self.hisco_sim_table.occ_j == hisco_code2)]['Value']

    def _compute_vectorized(self, hisco_codes1, hisco_codes2):
        # Ensure that hisco_codes1 and hisco_codes2 are pandas Series
        # hisco_codes1 = pd.Series(hisco_codes1)
        # hisco_codes2 = pd.Series(hisco_codes2)
        print("computing")
        # Step 1: Handle missing values with pd.isna
        mask_missing = pd.isna(hisco_codes1) | pd.isna(hisco_codes2)
        print(mask_missing)
        # Step 2: Identical values comparison
        mask_identical = (hisco_codes1 == hisco_codes2) & ~mask_missing
        print("step 2")
        # Step 3: Vectorized lookup to check if codes are in occ_i
        mask_in_occ_i_1 = hisco_codes1.isin(self.hisco_sim_table['occ_i'])
        mask_in_occ_i_2 = hisco_codes2.isin(self.hisco_sim_table['occ_i'])
        print("step 3")
        # Step 4: Create mask for codes not in occ_i
        mask_not_in_occ_i = ~(mask_in_occ_i_1 & mask_in_occ_i_2)
        print("step 4")
        # Initialize result array with None values
        results = np.full(hisco_codes1.shape, None)
        print("step 5")
        # Step 5: Assign 1 for identical hisco_codes
        results[mask_identical] = 1
        print("step 6")
        # Step 6: For remaining, perform lookup in similarity table for non-missing and valid codes
        valid_indices = ~(mask_missing | mask_identical | mask_not_in_occ_i)
        print("step 7")
        # Perform a vectorized merge with the similarity table to get the corresponding 'Value'
        merged_table = pd.DataFrame({
            'hisco_code1': hisco_codes1[valid_indices],
            'hisco_code2': hisco_codes2[valid_indices]
        }).merge(
            self.hisco_sim_table, 
            left_on=['hisco_code1', 'hisco_code2'], 
            right_on=['occ_i', 'occ_j'], 
            how='left'
        )
        print("step 8")
        # Assign the result values where available
        results[valid_indices] = merged_table['Value'].values
        print("step 9")
        return results

# use

if __name__  == "__main__":
    import pandas as pd
    import numpy as np
    
    # Generate sample hisco codes and similarity values
    hisco_code_values = ['100', '200', '300', '400', '500']
    
    # Create a DataFrame representing the hisco_sim_table
    hisco_sim_table = pd.DataFrame({
        'occ_i': ['100', '200', '300', '400', '500', '100', '200', '300'],
        'occ_j': ['200', '300', '400', '500', '100', '300', '400', '500'],
        'Value': [0.8, 0.5, 0.6, -0.3, 1, 0.75, 0.9, 0.4]
    })
    
    # Generate a DataFrame for test data (hisco_code1 and hisco_code2)
    test_data = pd.DataFrame({
        'hisco_code1': np.random.choice(hisco_code_values, size=10),
        'hisco_code2': np.random.choice(hisco_code_values, size=10)
    })
    
    # Print out the sample data
    print("Sample Hisco Similarity Table:")
    print(hisco_sim_table)
    
    print("\nGenerated Test Data:")
    print(test_data)

    patent = pd.DataFrame({
        'state': ['0', '1', '1', '1', '2'],
        'hisco_code1': ['100', '200', '300', '400', '500']
    })

    census = pd.DataFrame({
        'state': ['1', '1', '2', '1', '0'],
        'hisco_code2': ['500', '100', '300', '400', '500']
    })
    
    instance = HiscoSimilarity(patent, census, hisco_sim_table)
    # Example: Using the previously defined class and method
    indexer = rl.Index()
    blocking_columns = ['state']
    indexer.block(left_on=blocking_columns, right_on=blocking_columns)
    candidates = indexer.index(patent, census)
    comparer = rl.Compare()
    print("comparer")
    comparer.add(HiscoSimilarity(left_on = 'hisco_code1', right_on = 'hisco_code2', hisco_sim_table = hisco_sim_table, label='occ_similarity_HISCO'))
    results = comparer.compute(candidates, patent, census)
    
    # results = instance._compute_vectorized(test_data['hisco_code1'], test_data['hisco_code2'])
    # test_data['similarity'] = results
    
    print("\n Result Data with Similarity Results:")
    print(results)

