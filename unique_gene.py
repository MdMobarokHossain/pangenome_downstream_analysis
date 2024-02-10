# To find genes uniquely present in "KPN_NRICh_004_contigs", we'll look for rows where this column has a value
# but other isolate columns do not.

# Identifying other isolate columns to exclude "KPN_NRICh_004_contigs" from the comparison
other_isolate_columns = [col for col in column_names if col != "KPN_NRICh_004_contigs" and 'ERR' in col or 'SRR' in col]

# Checking for unique presence: A gene is considered uniquely present in "KPN_NRICh_004_contigs" if it has a value in
# that column but NaNs (or possibly some consistent indicator of absence) in all other isolate columns.
unique_genes_mask = data["KPN_NRICh_004_contigs"].notna() & data[other_isolate_columns].isna().all(axis=1)

# Extracting the unique genes
unique_genes = data.loc[unique_genes_mask, "Gene"]

unique_genes_list = unique_genes.tolist()
unique_genes_list

output:
group_4086
group_5349
umuD_4
bcr_3
group_113
group_12838
group_12839
group_12841
group_12842
group_12843
group_12845
group_12846
group_12847
group_12848
group_12849
group_12850
group_12851
hdfR_6
group_12853
group_12854
group_12855
group_12856
group_12857
group_12858
group_12859
group_131
group_3242
group_385
group_386
group_603
group_604