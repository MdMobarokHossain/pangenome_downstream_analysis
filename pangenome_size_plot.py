# Calculate the mean and median of gene counts for each number of genomes sampled
mean_gene_counts = pan_genome_transposed.mean(axis=1)
median_gene_counts = pan_genome_transposed.median(axis=1)

# Number of genomes sampled is just a sequence from 1 to the number of columns
num_genomes_sampled = np.arange(1, pan_genome_transposed.shape[0] + 1)

# Plotting the Heaps' Law plot
plt.figure(figsize=(14, 8))

# Plot all individual gene counts as black dots
for idx in range(pan_genome_transposed.shape[1]):
    plt.plot(num_genomes_sampled, pan_genome_transposed[idx], 'ko', markersize=2, alpha=0.2)

# Plot the mean and median gene counts
plt.plot(num_genomes_sampled, mean_gene_counts, 'bs-', label='Mean - Heaps\'s Law')
plt.plot(num_genomes_sampled, median_gene_counts, 'g^-', label='Median - Heaps\'s Law')

# Add legend and labels
plt.legend()
plt.xlabel('Number of Genomes')
plt.ylabel('Size of Pan-genome (Gene Count)')
plt.title('Heaps\' Law - Pan-genome Growth')
plt.grid(True)

# Show the plot
plt.show()
