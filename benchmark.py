import time
import csv
import os

def main():
    cpu_benchmark(50_000_000)

def cpu_benchmark(iterations: int) -> dict:
    procesor: str = input("Procesor name: ")
    ile_razy: int  = int(input("Ile iteracji: "))
    for _ in range(ile_razy):
        file_exists = os.path.exists("wyniki.csv")
    
        start = time.time()
        result = 0
        for i in range(iterations +1):
            result += (i **2 ) % 12345
        end = time.time()
        elapsed_time = end - start

        with open("wyniki.csv", "a") as file:
            fieldnames = ["Procesor", "Iterations", "result", "elapsed_time" , "operations_s"]
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
            if not file_exists:
                csv_writer.writeheader()

            csv_writer.writerow({"Procesor": procesor, "Iterations": iterations, "result": result, "elapsed_time": f"{elapsed_time:.3f}", "operations_s": f"{iterations/elapsed_time:.2f}"})




if __name__ == "__main__":
    main()

