from __future__ import division
__author__ = 'Vladimir Iglovikov'
import re

'''
This script parses output of the QUEST and returns dictionary with key - column name and value from the text
'''

data_file = open("/home/vladimir/workspace/Hubbard_database/data/square_1392060634.5.out").read()

def dqmc_parser(data_file):
    algorithm = "'DQMC'"
    time_slice_l = int(re.search('(?<=Time slice - L :)\s+.?\d+', data_file).group(0))
    seed = int(re.search('(?<=Random seed :)\s+.?\d+', data_file).group(0))
    u = float(re.search('(?<=U :)\s+.?\d+\.\d+', data_file).group(0))
    t_up = float(re.search('(?<=t_up :)\s+.?\d+\.\d+', data_file).group(0))
    t_dn = t_up = float(re.search('(?<=t_dn :)\s+.?\d+\.\d+', data_file).group(0))
    mu_up = float(re.search('(?<=mu_up :)\s+.?\d+\.\d+', data_file).group(0))
    mu_dn = float(re.search('(?<=mu_dn :)\s+.?\d+\.\d+', data_file).group(0))
    number_of_sites = int(re.search('(?<=Number of sites :)\s+.?\d+', data_file).group(0))
    dtau = float(re.search('(?<=dtau :)\s+.?\d+\.\d+', data_file).group(0))
    beta = float(re.search('(?<=beta :)\s+.?\d+\.\d+', data_file).group(0))
    number_of_warmup_sweep = int(re.search('(?<=Number of warmup sweep :)\s+.?\d+', data_file).group(0))
    number_of_measurement_sweep = int(re.search('(?<=Number of measurement sweep :)\s+.?\d+', data_file).group(0))
    frequency_of_recomputing_g = int(re.search('(?<=Frequency of recomputing G :)\s+.?\d+', data_file).group(0))
    global_move_number_of_sites = int(re.search('(?<=Global move number of sites :)\s+.?\d+', data_file).group(0))
    accept_count = int(re.search('(?<=Accept count :)\s+.?\d+', data_file).group(0))
    reject_count = int(re.search('(?<=Reject count :)\s+.?\d+', data_file).group(0))
    approximate_accept_rate = float(re.search('(?<=Approximate accept rate :)\s+.?\d+\.\d+', data_file).group(0))
    gamma = float(re.search('(?<=gamma :)\s+.?\d+\.\d+', data_file).group(0))
    global_move_accept_count = int(re.search('(?<=Global move accept count :)\s+.?\d+', data_file).group(0))
    global_move_reject_count = int(re.search('(?<=Global move reject count :)\s+.?\d+', data_file).group(0))
    global_move_accept_rate = float(re.search('(?<=Global move accept rate :)\s+.?\d+', data_file).group(0))
    type_of_matrix_b = '"' + re.search('(?<=Type of matrix B :)\s+.+\s*\n', data_file).group(0).strip() + '"'
    type_of_matrix_hsf = '"' + re.search('(?<=Type of matrix HSF :)\s+\w+\s*', data_file).group(0).strip() + '"'

    temp = re.search('(?<=Avg sign :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    avg_sign_value = float(temp[0])
    avg_sign_errorbar = float(temp[1])

    temp = re.search('(?<=Avg up sign :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    avg_up_sign_value = float(temp[0])
    avg_up_sign_errorbar = float(temp[1])

    temp = re.search('(?<=Avg dn sign :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    avg_dn_sign_value = float(temp[0])
    avg_dn_sign_errorbar = float(temp[1])

    temp = re.search('(?<=Up spin occupancy :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    up_spin_occupancy_value = float(temp[0])
    up_spin_occupancy_errorbar = float(temp[1])

    temp = re.search('(?<=Down spin occupancy :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',  data_file).groups()
    down_spin_occupancy_value = float(temp[0])
    down_spin_occupancy_errorbar = float(temp[1])

    temp = re.search('(?<= <U\*N_up\*N_dn\>  :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                            data_file).groups()
    u_n_up_n_dn_value = float(temp[0])
    u_n_up_n_dn_errorbar = float(temp[1])

    temp = re.search('(?<=Kinetic energy :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    kinetic_energy_value = float(temp[0])
    kinetic_energy_errorbar = float(temp[1])

    temp = re.search('(?<=Total [e, E]nergy :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                          data_file).groups()
    total_energy_value = float(temp[0])
    total_energy_errorbar = float(temp[1])
    temp = re.search('(?<=Density :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    density_value = float(temp[0])
    density_errorbar = float(temp[1])

    temp = re.search('(?<=Chi_thermal :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    chi_thermal_value = float(temp[0])
    chi_thermal_errorbar = float(temp[1])

    temp = re.search('(?<=XX Ferro structure factor :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                        data_file).groups()
    xx_ferro_structure_factor_value = float(temp[0])
    xx_ferro_structure_factor_errorbar = float(temp[1])

    temp = re.search('(?<=ZZ Ferro structure factor :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                        data_file).groups()
    zz_ferro_structure_factor_value = float(temp[0])
    zz_ferro_structure_factor_errorbar = float(temp[1])

    try:
        temp = re.search('(?<=Potential energy :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    except:
        pass
    else:
        potential_energy_value = float(temp[0])
        potential_energy_errorbar = float(temp[1])

    try:
        temp = re.search('(?<=Hopping energy :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    except:
        pass
    else:
        hopping_energy_value = float(temp[0])
        hopping_energy_errorbar = float(temp[1])

    try:
        temp = re.search('(?<=Double occupancy :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    except:
        pass
    else:
        double_occupancy_value = float(temp[0])
        double_occupancy_errorbar = float(temp[1])

    try:
        temp = re.search('(?<=Magnetizatiion squared :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                              data_file).groups()
    except:
        pass
    else:
        magnetization_squared_value = float(temp[0])
        magnetization_squared_errorbar = float(temp[1])

    temp = re.search('(?<=XX AF structure factor :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                        data_file).groups()
    xx_af_structure_factor_value = float(temp[0])
    xx_af_structure_factor_errorbar = float(temp[1])

    temp = re.search('(?<=Root Mean Square of XX AF :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                     data_file).groups()
    root_mean_square_of_xx_af_value = float(temp[0])
    root_mean_square_of_xx_af_errorbar = float(temp[1])

    temp = re.search('(?<=ZZ AF structure factor :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                        data_file).groups()
    zz_af_structure_factor_value = float(temp[0])
    zz_af_structure_factor_errorbar = float(temp[1])

    temp = re.search('(?<=Root Mean Square of ZZ AF :)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)',
                     data_file).groups()
    root_mean_square_of_zz_af_value = float(temp[0])
    root_mean_square_of_zz_af_errorbar = float(temp[1])

    temp = re.search('(?<=s-wave)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    s_wave_value = float(temp[0])
    s_wave_errorbar = float(temp[1])

    temp = re.search('(?<=s\*-wave)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    s_star_wave_value = float(temp[0])
    s_star_wave_errorbar = float(temp[1])

    temp = re.search('(?<=s\*\*-wave)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    s_star_star_wave_value = float(temp[0])
    s_star_star_wave_errorbar = float(temp[1])

    temp = re.search('(?<=d-wave)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    d_wave_value = float(temp[0])
    d_wave_errorbar = float(temp[1])

    temp = re.search('(?<=d\*-wave)\s+(\-?\d+\.\d+E?-?\+?\d+)\s+\+?-?\s+(\d+\.\d+E?\+?-?\d+)', data_file).groups()
    d_star_wave_value = float(temp[0])
    d_star_wave_errorbar = float(temp[1])

    result = {
        'algorithm': algorithm,
        'time_slice_l': time_slice_l,
        'seed': seed,
        'u': u,
        't_up': t_up,
        't_dn': t_dn,
        'mu_up': mu_up,
        'mu_dn': mu_dn,
        'number_of_sites': number_of_sites,
        'dtau': dtau,
        'beta': beta,
        'number_of_warmup_sweep': number_of_warmup_sweep,
        'number_of_measurement_sweep': number_of_measurement_sweep,
        'frequency_of_recomputing_g': frequency_of_recomputing_g,
        'global_move_number_of_sites': global_move_number_of_sites,
        'accept_count': accept_count,
        'reject_count': reject_count,
        'approximate_accept_rate': approximate_accept_rate,
        'gamma': gamma,
        'global_move_accept_count': global_move_accept_count,
        'global_move_reject_count': global_move_reject_count,
        'global_move_accept_rate': global_move_accept_rate,
        'type_of_matrix_b': type_of_matrix_b,
        'type_of_matrix_hsf': type_of_matrix_hsf,
        'avg_sign_value': avg_dn_sign_value,
        'avg_sign_errorbar': avg_sign_errorbar,
        'avg_up_sign_value': avg_up_sign_value,
        'avg_up_sign_errorbar': avg_dn_sign_errorbar,
        'avg_dn_sign_value': avg_dn_sign_value,
        'avg_dn_sign_errorbar': avg_dn_sign_errorbar,
        'up_spin_occupancy_value': up_spin_occupancy_value,
        'up_spin_occupancy_errorbar': up_spin_occupancy_errorbar,
        'down_spin_occupancy_value': down_spin_occupancy_value,
        'down_spin_occupancy_errorbar': down_spin_occupancy_errorbar,
        'u_n_up_n_dn_value': u_n_up_n_dn_value,
        'u_n_up_n_dn_errorbar': u_n_up_n_dn_errorbar,
        'kinetic_energy_value': kinetic_energy_value,
        'kinetic_energy_errorbar': kinetic_energy_errorbar,
        'total_energy_value': total_energy_value,
        'total_energy_errorbar': total_energy_errorbar,
        'density_value': density_value,
        'density_errorbar': density_errorbar,
        'chi_thermal_value': chi_thermal_value,
        'chi_thermal_errorbar': chi_thermal_errorbar,
        'xx_ferro_structure_factor_value': xx_ferro_structure_factor_value,
        'xx_ferro_structure_factor_errorbar': xx_ferro_structure_factor_errorbar,
        'zz_ferro_structure_factor_value': zz_ferro_structure_factor_value,
        'zz_ferro_structure_factor_errorbar': zz_ferro_structure_factor_errorbar,
        'xx_af_structure_factor_value': xx_af_structure_factor_value,
        'xx_af_structure_factor_errorbar': xx_af_structure_factor_errorbar,
        'root_mean_square_of_xx_af_value': root_mean_square_of_xx_af_value,
        'root_mean_square_of_xx_af_errorbar': root_mean_square_of_xx_af_errorbar,
        'zz_af_structure_factor_value': zz_af_structure_factor_value,
        'zz_af_structure_factor_errorbar': zz_af_structure_factor_errorbar,
        'root_mean_square_of_zz_af_value': root_mean_square_of_zz_af_value,
        'root_mean_square_of_zz_af_errorbar': root_mean_square_of_zz_af_errorbar,
        's_wave_value': s_wave_value,
        's_wave_errorbar': s_wave_errorbar,
        's_star_wave_value': s_star_wave_value,
        's_star_wave_errorbar': s_star_wave_errorbar,
        's_star_star_wave_value': s_star_star_wave_value,
        's_star_star_wave_errorbar': s_star_star_wave_errorbar,
        'd_wave_value': d_wave_value,
        'd_wave_errorbar': d_wave_errorbar,
        'd_star_wave_value': d_star_wave_value,
        'd_star_wave_errorbar': d_star_wave_errorbar,
    }

    if 'potential_energy_value' in locals():
        result['potential_energy_value'] = potential_energy_value
    if 'potential_energy_value' in locals():
        result['potential_energy_errorbar'] = potential_energy_errorbar
    if 'hopping_energy_value' in locals():
        result['hopping_energy_value'] = hopping_energy_value
    if 'hopping_energy_errorbar' in locals():
        result['hopping_energy_errorbar'] = hopping_energy_errorbar
    if 'double_occupancy_value' in locals():
        result['double_occupancy_value'] = double_occupancy_value
    if 'double_occupancy_errorbar' in locals():
        result['double_occupancy_errorbar'] = double_occupancy_errorbar
    if 'magnetization_squared_value' in locals():
        result['magnetization_squared_value'] = magnetization_squared_value
    if 'magnetization_squared_errorbar' in locals():
        result['magnetization_squared_errorbar'] = magnetization_squared_errorbar

    return result

if __name__ == '__main__':
    a = dqmc_parser(data_file).keys()
    a.sort()
    print a

