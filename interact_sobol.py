import chaospy as cp
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import sobol_seq

f, ax = plt.subplots(1, 2, sharey=True)

u1 = cp.Uniform(0,1)
u2 = cp.Uniform(0,1)
jpdf = cp.J(u1, u2)

f.suptitle('Sobol sequences versus random sampling')

def up_Sobol(N):
    ax[0].clear()
    ax[1].clear()
        
    sample_0 = np.random.rand(2**N, 2)
    samples_1 = jpdf.sample(size=2**N, rule='S')

    ax[0].scatter(sample_0[:,0],sample_0[:,1],s=1,color='b')
    ax[1].scatter(*samples_1,s=1,color='b')
    
    ax[0].set_title('Random')
    ax[1].set_title('Sobol')
    
    plt.show()    
