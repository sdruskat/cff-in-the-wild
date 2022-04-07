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