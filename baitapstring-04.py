a= """
	tôi chăm học
	tôi chịu khó
	tôi đẹp zai tôi
	"""
dem=0
for i in range(len(a)):
    if a[i]=="t" and a[i+1]=="ô" and a[i+2]=="i":
        dem=dem+1
print(dem)