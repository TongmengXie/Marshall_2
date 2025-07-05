conda activate marshall_2
cd Marshall_2/codes

sbatch --partition large --cpus-per-task 32 --mem 230G --job-name=get_cosine_sim_matrix --wrap "papermill occ_sim_US_get_cosine_sim_matrix.ipynb outputs/occ_sim_US_get_cosine_sim_matrix_out.ipynb"
