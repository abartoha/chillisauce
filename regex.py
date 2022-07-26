import re 
from pprint import pprint
pprint(re.findall(r'^https://[a-z]*.[a-z]*.[a-z]*/[a-z]*/', "https://cdn.nload.xyz/galleries/2210571/5t.jpg")[0])