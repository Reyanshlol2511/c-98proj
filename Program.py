def switchFileData():
    firstfile = input("Enter the first file name: ")
    secondfile = input("Enter the second file name: ")


    with open(firstfile, 'r') as xr:
    data_xr = xr.read()

	with open(secondfile, 'r') as xt:
    data_xt = xt.read()

    with open(firstfile, 'w') as xr:    
    xr.write(data_xt)

    with open(secondfile, 'w') as xt:
    xt.write(data_xr)


switchFileData()