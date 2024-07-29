# make_diag_table

Python script to generate a [MOM5](https://github.com/mom-ocean/MOM5) or [MOM6](https://github.com/mom-ocean/MOM6) [`diag_table`](https://mom6.readthedocs.io/en/main/api/generated/pages/Diagnostics.html), for example using a systematic one-file-per-variable naming convention.

Edit `diag_table_source.yaml` and run `make_diag_table.py` to create a `diag_table`. **Warning:** this will overwrite any existing `diag_table`.

Adding or removing diagnostics is as simple as adding or removing their names in the appropriate `fields` section in the `diag_table` part of `diag_table_source.yaml`.

`make_diag_table.py` is very general, so you should be able to generate any `diag_table` you like, with any output file naming convention, entirely by editing `diag_table_source.yaml`. See the comments in `diag_table_source.yaml` for usage instructions.

Note that each of the top-level categories in the `diag_table` part of `diag_table_source.yaml` can have only one instance of each field name, so if you need multiple outputs of the same field (e.g. as both averages and snapshots), you'll need to make additional categories.

An (incomplete) list of MOM5 diagnostics is available [here](https://raw.githubusercontent.com/COSIMA/access-om2/master/MOM_diags.txt), obtained by [this method](https://github.com/COSIMA/access-om2/wiki/Technical-documentation#MOM5-diagnostics-list.).
MOM6 diagnostics are [listed in `available_diags.*`](https://mom6.readthedocs.io/en/main/api/generated/pages/Diagnostics.html#native-diagnostics) following a run of the model.

Also see these discussions on standardized [ACCESS-OM2](https://github.com/COSIMA/access-om2/issues/185) and [ACCESS-OM3](https://github.com/COSIMA/access-om3/issues/191) filenames.
