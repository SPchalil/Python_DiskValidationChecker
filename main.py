# -----------------------Welcome Screen------------------------#

print("============================================================")
print("              PythonCo. Disk Validation Checker")
print("============================================================")

true = 1
while (true):

  # ------------------------Disk Title Check---------------------#
  def game_title(disk_name):
      if(str(disk_name) == "Pac Man World" or str(disk_name) == "Game of Life" or str(disk_name) == "Call of Duty: Big Red One" or str(disk_name) == "Cardinal Syn" or str(disk_name) == "NHL ‘99"):
        return True
      else:
        return False
  
  # User Input
  disk_name =  input("Enter in the name of the disk and press ENTER: ") 
  game_title_value = game_title(disk_name)

  
  # ------------------Disk Number Check------------------------------#
  def disk_number(number):
      if 1496833 <= number <= 5930214:
        return True
      else:
        return False
  
  # User Input
  disk_number_value = disk_number(int(input("Enter in the disk number and press ENTER: ")))
  
  
  # ---------------------Disk Serial Number Check---------------------#
  def serial_number(serial_number):
      
      if(str(serial_number) == "40394" and str(disk_name) =="Pac Man World"):
        return True
      elif(str(serial_number) == "69302" and str(disk_name) =="Game of Life"):
        return True
      elif(str(serial_number) == "76034" and str(disk_name) =="Call of Duty: Big Red One"):
        return True
      elif(str(serial_number) == "40395" and str(disk_name) =="Cardinal Syn"):
        return True
      elif(str(serial_number) == "22490" and str(disk_name) =="NHL ‘99"):
        return True
      else:
        return False
  
  
  # User Input
  serial_number_value = serial_number(int(input("Enter in the disk serial number and press ENTER: ")))


 # ---------------------Return Results----------------------------------#
  print("\n")
  print("RESULTS")
  print("========================================================")
  print("On Disk List:                         ", game_title_value)
  print("Disk Number Match:                    ", disk_number_value)
  print("Disk Serial Number Match:             ", serial_number_value)
  print("\n")

  if (str(game_title_value) and str(disk_number_value) and str(serial_number_value) == "True"):
    print("THIS IS A GENUINE DISK.") 
  else:
    print("THIS IS A PIRATED COPY.")

  print("\n")
  continue