"""Selection of functions to generate interesting
stats from CFF file data"""


def created_with_cffinit(cff_data):
    """Calculate how many CFF files were created using
    CFFinit."""
    # Check how many were created using CFFinit
    cffinit = 0
    for cff in cff_data:
        if cff['created_by_cffinit']:
            cffinit = cffinit + 1
    return cffinit


def which_cff_version(cff_data):
    """Calculate which version of CFF was used to created
    CFF files"""
    versions = {}
    for cff in cff_data:
        # First check that there is a CFF version field
        if 'cff-version' in cff:
            # Get the version of this CFF file
            version = cff['cff-version']
            # Increment the number of CFF files with this version
            if version in versions.keys():
                versions[version] = versions[version] + 1
            else:
                versions[version] = 1
    return versions