import random

def frac_part(v):
	v = str(v)
	i,f = v.split('.')
	return f

results = []
for i in range(20):
	r = random.random()*100		#generate random num
	r_str = str(r)				#typecast into a str
	r_frac = frac_part(r_str)
	r_out = float('0.'+r_frac)
	results.append(r_out)

print(results)

rand_gen = ( random.random() * 100 for i in range(20))
str_gen = ( str(r) for r in rand_gen)
frac_gen = ( frac_part(r) for r in str_gen)
out_gen = ( float('0.'+r) for r in frac_gen)

results = list(out_gen)
print(results)