# make_diag_table

Python script to generate a [MOM5](https://github.com/mom-ocean/MOM5) `diag_table`.

Edit `diag_table_source.yaml`, run `make_diag_table.py` and see a correctly-formatted `diag_table` appear before your very eyes, with standardized filenames as in https://github.com/COSIMA/access-om2/issues/185.

Adding or removing diagnostics is as simple as adding or removing their names in the appropriate `fields` section in the `diag_table` part of `diag_table_source.yaml`.

An (incomplete) list of MOM5 diagnostics is available here:
https://raw.githubusercontent.com/COSIMA/access-om2/master/MOM_diags.txt
obtained by this method:
https://github.com/COSIMA/access-om2/wiki/Technical-documentation#MOM5-diagnostics-list

Note that each of the top-level categories in the `diag_table` part of `diag_table_source.yaml` can have only one instance of each field name, so if you need multiple outputs of the same field (e.g. as both averages and snapshots), you'll need to make additional categories.