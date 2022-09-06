import matplotlib.pyplot as plt
import numpy

liste1 = []
liste2 = []

for N in numpy.arange(0.1,26) :
    p1 = (0.016 + 0.021/N)**2
    p2 = p1 * 6.8
    p3 = p2/(9/65)
    p4 = p3 * 1000
    print(p4)
    liste1.append(N)
    liste2.append(p4)
    plt.plot(liste1, liste2,":")
    plt.axis([0, 25, 0, 100])
    N += 0.1

plt.xlabel("Reducteur 1:X")
plt.ylabel("Puissance du moteur (en V)")
plt.grid()
plt.show()
