from concurrent.futures import ProcessPoolExecutor

def kuadrat(x):
    return x * x

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    with ProcessPoolExecutor(max_workers=3) as eksekutor:
        hasil = list(eksekutor.map(kuadrat, data))
    print("Hasil :", hasil)