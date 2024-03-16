"""
    Programer: Wellington
    Date: 03/10
    Details: Leearnig Defense programming
"""

#x = 2
#assert x < 1, 'Falied error assertion - Wb'

def avg(marks):
    assert len(marks) != 0, 'Lenght of the marks list cannot be 0.'
    return round(sum(marks) / len(marks), 2)

sem1_marks = [62, 65, 75]
ranks = []
print('Average marks for semester 1:', avg(ranks))
