# FileFactory
Merge/unmerge text files

# Baking A File
`bake <blueprint> <output>`

`<blueprint>` A file containing file segment references in each line. 
A file segment reference consists of a file name and optionally a file section (seperated by `#`).

`<output>` File name to the resulting baked file. It is built in the order, how it is specified in `<blueprint>`.
Each file segment is prepended by a comment in the form `#[file] <filename>[#<section>]`

Input files (specified by `<blueprint>`) can consist of multiple sections. 
Each section is prepended by a comment in the form `#[section] <section>`.
The unnamed section starts at the top of each file until the first `#[section] <file>` appears.
The unnamed section can be prepended by just `#[section]`, when nothing appears before the first `#[section] <file>`.
This allows the unnamed section to be moved away from the top of the file.
A section should not appear twice neither in the blueprint nor file represented in the blueprint.


# Unbaking A File
`unbake <input> <blueprint>`

Does the baking process backwards.

`<input>` The baked file to unbake. It contains file segment comments in the form `#[file] <filename>[#<filesection>]`.

It writes to the files referred by the file segment comments and updates the blueprint-file.
Unnamed sections are always written at the start of a file.
A section of the same file should not appear twice in `<input>`.