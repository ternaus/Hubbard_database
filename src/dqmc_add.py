#!/usr/bin/env python
from __future__ import division
import argparse
import sqlite3
import os
import dqmc_parser

__author__ = 'Vladimir Iglovikov'

'''
this script adds file or files to the sqlite database. If database does not exist it creates it.
'''

parser = argparse.ArgumentParser(description='Adds data from the QUEST output to the sqlite database')
parser.add_argument('-database', type=str, help='file that contains the databse')
parser.add_argument('-folder', type=str, help='folder with files that should be added to the database')
parser.add_argument('-file', type=str, help='file that should be added to the database')
parser.add_argument('-extra', type=str, help='file that contains extra information that should be added to the database')
args = parser.parse_args()

column_names = ['name_of_the_lattice',
                'algorithm',
                'time_slice_l',
                'dtau',
                'bcond',
                'number_of_warmup_sweep',
                'number_of_measurement_sweep',
                'tausk',
                'nbin',
                'nhist',
                'seed',
                'north',
                'nwrap',
                'fixwrap',
                'errrate',
                'difflim',
                'u',
                't_up',
                't_dn',
                'mu_up',
                'mu_dn',
                'nx',
                'ny',
                'nz',
                'number_of_sites',
                'beta',
                'frequency_of_recomputing_g',
                'global_move_number_of_sites',
                'accept_count',
                'reject_count',
                'approximate_accept_rate',
                'gamma',
                'global_move_accept_count',
                'global_move_reject_count',
                'global_move_accept_rate',
                'type_of_matrix_b',
                'type_of_matrix_hsf',
                'avg_sign_value',
                'avg_sign_errorbar',
                'avg_up_sign_value',
                'avg_up_sign_errorbar',
                'avg_dn_sign_value',
                'avg_dn_sign_errorbar',
                'up_spin_occupancy_value',
                'up_spin_occupancy_errorbar',
                'down_spin_occupancy_value',
                'down_spin_occupancy_errorbar',
                'u_n_up_n_dn_value',
                'u_n_up_n_dn_errorbar',
                'kinetic_energy_value',
                'kinetic_energy_errorbar',
                'total_energy_value',
                'total_energy_errorbar',
                'density_value',
                'density_errorbar',
                'chi_thermal_value',
                'chi_thermal_errorbar',
                'xx_ferro_structure_factor_value',
                'xx_ferro_structure_factor_errorbar',
                'zz_ferro_structure_factor_value',
                'zz_ferro_structure_factor_errorbar',
                'potential_energy_value',
                'potential_energy_errorbar',
                'hopping_energy_value',
                'hopping_energy_errorbar',
                'double_occupancy_value',
                'double_occupancy_errorbar',
                'magnetization_squared_value',
                'magnetization_squared_errorbar',
                'xx_af_structure_factor_value',
                'xx_af_structure_factor_errorbar',
                'root_mean_square_of_xx_af_value',
                'root_mean_square_of_xx_af_errorbar',
                'zz_af_structure_factor_value',
                'zz_af_structure_factor_errorbar',
                'root_mean_square_of_zz_af_value',
                'root_mean_square_of_zz_af_errorbar',
                's_wave_value',
                's_wave_errorbar',
                's_star_wave_value',
                's_star_wave_errorbar',
                's_star_star_wave_value',
                's_star_star_wave_errorbar',
                'd_wave_value',
                'd_wave_errorbar'
                'd_star_wave_value',
                'd_star_wave_errorbar']



#get connection with database
con = sqlite3.connect(args.database)
#create cursor to the database
cur = con.cursor()

#check if table in the database exists. If it does not we create it
sql = 'create table if not exists  DQMC {column_names}'.format(column_names='(' + ', '.join(column_names) + ')')

cur.execute(sql)

def add_file(file_to):
    file_to_add = open(file_to)
    dict_to_add = dqmc_parser.dqmc_parser(file_to_add.read())
    file_to_add.close()
    result = []
    for column_name in column_names:
        try:
            result += [dict_to_add[column_name]]
        except:
            result += ['']

    result = tuple(result)
    cur.execute("INSERT INTO DQMC VALUES {data}".format(data=result))

#if we add only one file create tuple that describes it
if args.file:
    add_file(args.file)

#if we add folder one file create tuple that describes it
elif args.folder:
    for file_name in os.listdir(args.folder):
        add_file(os.path.join(args.folder,file_name))


con.commit()
cur.close()
con.close()
