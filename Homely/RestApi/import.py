import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("parkingreport.xls")
sheet = book.sheet_by_name("parkingreport.csv")

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "admin", passwd = "fred1", db = "parkingvision")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO parkingzones (zid, primecontrol, NoS, street, origins, start, finish, control1, control2, control3, lat, lng) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
count=0
for r in range(2, sheet.nrows):
      zid      = sheet.cell(r,0).value
      primecontrol = sheet.cell(r,1).value
      NoS          = sheet.cell(r,2).value
      street     = sheet.cell(r,3).value
      origins       = sheet.cell(r,4).value
      start = sheet.cell(r,5).value
      finish        = sheet.cell(r,6).value
      control1       = sheet.cell(r,7).value
      control2     = sheet.cell(r,8).value
      control3        = sheet.cell(r,9).value
      lat          = sheet.cell(r,12).value
      lng   = sheet.cell(r,13).value

      # Assign values from each row
      values = (zid, primecontrol.strip(), NoS, street.strip(), origins.strip(), start, finish, control1.strip(), control2.strip(), control3.strip(), lat, lng)

      # Execute sql Query
      cursor.execute(query, values)
      # try:
      #     cursor.execute(query, values)
      # except:
      #     count+=1
      #     pass
# Close the cursor
cursor.close()
print count
# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done! Bye, for now."
print ""