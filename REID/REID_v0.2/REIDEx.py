import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Digest")
sheet.write(0,0,"foobar")
workbook.save("RestrictionDigest.xls")
