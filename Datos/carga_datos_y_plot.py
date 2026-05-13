import csv

def cargar_datos_csv_listas(ruta_archivo):
    FSC_A = [] ;     SSC_A = [] ;    FL1_A = [] ;    FL2_A = [];     FL3_A = [] ;     FL4_A = []
    FSC_H = [];    SSC_H = [];    FL1_H = [];    FL2_H = [];    FL3_H = [];    FL4_H = []
    
    Width = [];    Time = []
    
    with open(ruta_archivo, newline='') as archivo:  #
        lector = csv.reader(archivo)
        next(lector)  
        
        for fila in lector:
            FSC_A.append(int(fila[0]))
            SSC_A.append(int(fila[1]))
            FL1_A.append(int(fila[2]))
            FL2_A.append(int(fila[3]))
            FL3_A.append(int(fila[4]))
            FL4_A.append(int(fila[5]))
            FSC_H.append(int(fila[6]))
            SSC_H.append(int(fila[7]))
            FL1_H.append(int(fila[8]))
            FL2_H.append(int(fila[9]))
            FL3_H.append(int(fila[10]))
            FL4_H.append(int(fila[11]))
            Width.append(int(fila[12]))
            Time.append(int(fila[13]))
    
    return (FSC_A, SSC_A, FL1_A, FL2_A, FL3_A, FL4_A,
            FSC_H, SSC_H, FL1_H, FL2_H, FL3_H, FL4_H,
            Width, Time)


glucosa_base = cargar_datos_csv_listas('Datos/Citometro/Osa_Base.csv')  