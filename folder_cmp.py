from filecmp import dircmp


def print_diff_files(dcmp):
    for name in dcmp.diff_files:

        print(f'diff_file {name} found in {dcmp.left} and {dcmp.right}')
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

dcmp = dircmp('/Users/anthlis/Code/diff_tool/folder1', '/Users/anthlis/Code/diff_tool/folder2')

print(print_diff_files(dcmp))
