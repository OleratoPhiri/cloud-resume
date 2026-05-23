import zipfile
z = zipfile.ZipFile('lamdba_function.zip', 'w')
z.write('lambda_function.py')
z.close()
print('Zip created successfully')
