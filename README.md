# Hubbard database
This repository contains database of the measuremnts that were performed on the Hubbard model on the different lattices using:
 * DQMC code of the QUEST project (quest-qmc.googlecode.com)
 * ED code of the ALPS project

QUEST provides text file as an output that can be parsed, but much better to store this in some kind of database.
This package will provide pythonscript that will allow to add data to the database. 

----
Syntax:
```
python add_to_database.py -database <database name> 
                          -folder <folder with files to add> 
                          -file <file to add>
                          -extra <file with extra information that will be added to the database>
```

----

Column names:
 * name_of_the_lattice - name of the lattice (square, triangular, chain, kagome, Lieb, honeycomb, ...)
 * algorithm - algorithm that generates the data (DQMC, Lanczos, ED)
 * time_slice_l - number of layers in temporal direction
 * dtau 
 * bcond - type of the boundary conditions
 * number_of_warmup_sweep
 * number_of_measurement_sweep
 * tausk
 * nbin
 * nhist
 * seed - random number seed
 * north
 * nwrap
 * fixwrap
 * errrate
 * difflim
 * u
 * t_up
 * t_dn
 * mu_up
 * mu_dn
 * nx
 * ny
 * ny
 * number_of_sites - number of sites in the spatial direction
 * beta - inverse temperature
 * frequency_of_recomputing_g
 * global_move_number_of_sites
 * accept_count
 * reject_count
 * approximate_accept_rate
 * gamma
 * global_move_accept_count
 * global_move_reject_count
 * global_move_accept_rate
 * type_of_matrix_b
 * type_of_matrix_hsf
 * avg_sign_value
 * avg_sign_errorbar
 * avg_up_sign_value
 * abd_up_sign_errorbar
 * avg_dn_sign_value
 * avg_dn_sign_errorbar
 * up_spin_occupancy_value
 * up_spin_occupancy_errorbar
 * down_spin_occupancy_value
 * down_spin_occupancy_errorbar
 * u_n_up_n_dn_value - \<U N_up N_dn\>
 * u_n_up_n_dn_errorbar - \<U N_up N_dn\>
 * kinetic_energy_value
 * kinetic_energy_errorbar
 * total_energy_value
 * total_energy_errorbar
 * density_value
 * density_errorbar
 * chi_thermal_value
 * chi_thermal_errorbar
 * xx_ferro_structure_factor_value
 * xx_ferro_structure_factor_errorbar
 * zz_ferro_structure_factor_value
 * zz_ferro_structure_factor_errorbar
 * potential_energy_value
 * potential_energy_errorbar
 * hopping_energy_value
 * hopping_energy_errorbar
 * double_occupancy_value
 * double_occupancy_errorbar
 * magnetization_squared_value
 * magnetization_squared_errorbar
 * xx_af_structure_factor_value
 * xx_af_structure_factor_errorbar
 * root_mean_square_of_xx_af_value
 * root_mean_square_of_xx_af_errorbar
 * zz_af_structure_factor_value
 * zz_af_structure_factor_errorbar
 * root_mean_square_of_zz_af_value
 * root_mean_square_of_zz_af_errorbar
 * s_wave_value
 * s_wave_errorbar
 * s_star_wave_value
 * s_star_wave_errorbar
 * s_star_star_wave_value
 * s_star_star_wave_errorbar
 * d_wave_value
 * d_wave_errorbar
 * d_star_wave_value
 * d_star_wave_errorbar
