#!/usr/bin/env python
"""

Generate MOM5 diag_table file from diag_table_source.yaml
Latest version: https://github.com/COSIMA/make_diag_table

The MOM diag_table format is defined here:
https://github.com/mom-ocean/MOM5/blob/master/src/shared/diag_manager/diag_table.F90
and some of the available diagnostics are listed here:
https://raw.githubusercontent.com/COSIMA/access-om2/master/MOM_diags.txt
https://github.com/COSIMA/access-om2/wiki/Technical-documentation#MOM5-diagnostics-list

"""

from __future__ import print_function
import yaml


def set_filename(indict):
    """
    Create standardised filename as defined in 'file_name' entry.
    """
    fn = indict['file_name']
    if isinstance(fn, list):
        fn = [str(indict[k]) for k in fn]
        fn = [indict['file_name_substitutions'].get(v, v) for v in fn]
        if indict['file_name_omit_empty']:
            fn = [v for v in fn if v != '']
        return indict['file_name_separator'].join(fn)
    else:
        return fn


def strout(v):
    """Return string representation, with double quotes around strings."""
    if isinstance(v, str):
        return '"' + v + '"'
    else:
        return str(v)


indata = yaml.load(open('diag_table_source.yaml', 'r'))
outstrings = []  # strings to write to diag_table
filenames = {}  # diagnostic output filenames

# global section
d = indata['global_defaults']
outstrings.append(d['title'])
outstrings.append(' '.join([str(x) for x in d['base_date']]))
outstrings.append('''
#########################################################################################################
#                                                                                                       #
# DO NOT EDIT! Instead, edit diag_table_source.yaml and run make_diag_table.py to re-generate this file #
#                                                                                                       #
#########################################################################################################''')

# interleaved file and field sections
for k, grp in indata['diag_table'].items():
    # ensure expected entries are present in group
    if grp is None:
        grp = dict()
    grp['defaults'] = grp.get('defaults', dict())
    if grp['defaults'] is None:
        grp['defaults'] = dict()
    grp['fields'] = grp.get('fields', dict())
    if grp['fields'] is None:
        grp['fields'] = dict()

    outstrings.append('\n\n# '+ k)  # use group name as a comment

    for field_name, field_dict in grp['fields'].items():

        if field_dict is None:
            field_dict = {}

        # combine field_dict with defaults into one dict f
        f = {**indata['global_defaults'],
             **grp['defaults'],
             **field_dict,
             'field_name': field_name}

        if f['output_name'] is None:
            f['output_name'] = f['field_name']

        fname = set_filename(f)
        if fname not in filenames:  # to ensure that each filename is specified once only
            fnameline = [fname, f['output_freq'], f['output_freq_units'],
                         f['file_format'], f['time_axis_units'], f['time_axis_name']]
            if 'new_file_freq' in f:
                if f['new_file_freq'] is not None:
                    fnameline.extend([f['new_file_freq'], f['new_file_freq_units']])
                    if 'start_time' in f:
                        if f['start_time'] is not None:
                            fnameline.append(' '.join([str(x) for x in f['start_time']]))
                            if 'file_duration' in f:
                                if f['file_duration'] is not None:
                                    fnameline.extend([f['file_duration'], f['file_duration_units']])
            outstrings.append('')
            outstrings.append(', '.join([strout(v) for v in fnameline]))
            filenames[fname] = None

        if f['reduction_method'] == 'snap':
            f['reduction_method'] = 'none'

        fieldline = [f['module_name'], f['field_name'], f['output_name'],
                     fname, f['time_sampling'], f['reduction_method'],
                     f['regional_section'], f['packing']]
        outstrings.append(', '.join([strout(v) for v in fieldline]))

# output outstrings
with open('diag_table', 'w') as f:
    for line in outstrings:
        f.write('%s\n' % line)
