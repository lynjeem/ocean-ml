import sys 


# vectorq.exec:
vectorq_file = open('vectorq.exec',"w")
vectorq_file.write("#!/bin/csh\n\n")
vectorq_file.write("set dir = ./test/\n")
vectorq_file.write("set fileinfo = {$dir}info_pr.dat\n")
vectorq_file.write("set filedh =  {$dir}dh_" + str(example_date) + ".gr\n")
vectorq_file.write("set filest =  {$dir}density_" + str(example_date) + ".gr\n")
vectorq_file.write("set filestm = {$dir}ss1_st0.dat\n")
vectorq_file.write("set filequ =  {$dir}ss1a2qu.gr\n")
vectorq_file.write("set fileqv =  {$dir}ss1a2qv.gr\n")
vectorq_file.write("set fileqdi = {$dir}ss1a2qdi.gr\n")
vectorq_file.write("./vectorq.exe << !\n")
vectorq_file.write("'$fileinfo'	#>>>>>Escribe info file info.dat:\n")
vectorq_file.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:\n")
vectorq_file.write("'$filest'	#>>>>>Escribe fichero de densidad:\n")
vectorq_file.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:\n")
vectorq_file.write("'$filequ'	#>>>>>Escribe fichero Qu:\n")
vectorq_file.write("'$fileqv'	#>>>>>Escribe fichero Qv:\n")
vectorq_file.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:\n")

#omegainv.exec:

omegainv_file = open('omegainv.exec',"w")

omegainv_file.write("#!/bin/csh\n")
omegainv_file.write("set dir = ./test/\n")
omegainv_file.write("set fileinfo = {$dir}info_pr.dat\n")
omegainv_file.write("set filestm = {$dir}ss1_st0.dat\n")
omegainv_file.write("set fileqdi = {$dir}ss1a2qdi.gr\n")
omegainv_file.write("set filew =   {$dir}ss1a2ww.gr\n")

omegainv_file.write("./omegainv.exe << !\n")
omegainv_file.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:\n")
omegainv_file.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:\n")
omegainv_file.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:\n")
omegainv_file.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):\n")
omegainv_file.write("'$filew'	#>>>>>Escribe fichero Salida W:\n")
omegainv_file.write("!\n")

example_date = 20031108


example_date = sys.argv[1]



vectorq_file.write



