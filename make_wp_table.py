"""
Format a table for worpdress post.
"""

import csv

data = csv.DictReader(open('data/fbi-planes.csv', 'rb'))

header = """
<table border="0" rules="NONE" cellspacing="0"><colgroup> <col width="297" /> <col width="301" /> <col width="115" /> <col width="47" /> <col width="146" /> <col width="386" /></colgroup>
<tbody>
<tr>
<td align="LEFT" width="297" height="18">Company Name</td>
<td align="LEFT" width="301">Street</td>
<td align="LEFT" width="115">City</td>
<td align="LEFT" width="47">State</td>
<td align="LEFT" width="146">ICAO</td>
<td align="LEFT" width="386">Flight Radar</td>
</tr>
"""

row_tmpl = """
<tr>
<td align="LEFT" height="18">{name}</td>
<td align="LEFT">{street}</td>
<td align="LEFT">{city}</td>
<td align="LEFT">{state}</td>
<td align="LEFT">{mode_s_code_hex}</td>
<td align="LEFT"><a href="http://www.flightradar24.com/data/airplanes/{n_number}">{n_number}</a></td>
</tr>
"""

footer = """
</tbody>
</table>
"""

print header
for row in data:
    print row_tmpl.format(**row)
print footer