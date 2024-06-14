def generator(max_broj):
    for i in range(max_broj):
        if i%2==0:
            yield f"Parni broj:{i}"

        else:
            yield f"Neparni broj:{i}"
max_broj=15
for broj in generator(max_broj):
    print(broj)


                
