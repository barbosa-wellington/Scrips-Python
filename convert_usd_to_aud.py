"""
    Name module: Convert_usd_to_aud
    name: Wellington
    details: Function that is convert the value in US dollar
    for Australia dollar
"""


# This function receive two arguments or parameters
# One parameter was definited that is rate=0.75
def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

# In the same way, we can change the rate value in the moment of called

"""
    convert_uas_to_aud(100)
    133.33333333334

    or

    convert_usd_to_aud(100, rate=0.78)
    128.2051282051282
"""


